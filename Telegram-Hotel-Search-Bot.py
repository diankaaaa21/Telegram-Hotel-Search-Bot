import logging
import os

import requests
import telebot
from dotenv import load_dotenv

from database import SessionLocal, UserQuery, init_db

init_db()

logging.basicConfig(
    filename="bot.log",
    level=logging.DEBUG,
    format="%(asctime)s - %(levelname)s - %(message)s",
)


load_dotenv()
token = os.getenv("TELEGRAM_BOT_TOKEN")
key = os.getenv("API_KEY")


if not token or not key:
    logging.critical(
        "TELEGRAM_BOT_TOKEN or API_KEY is missing in environment variables."
    )
    raise ValueError("TELEGRAM_BOT_TOKEN or API_KEY is missing")

bot = telebot.TeleBot(token)

user_data = {}


def save_user(chat_id, name, city):
    db = SessionLocal()
    new_user = UserQuery(chat_id=chat_id, name=name, city=city)
    db.add(new_user)
    db.commit()
    db.close()


@bot.message_handler(commands=["start"])
def start(message):
    log_command(message, "start")
    with open("rr.jpg", "rb") as photo:
        bot.send_photo(message.chat.id, photo=photo)
    bot.send_message(
        message.from_user.id,
        "Hello! I'm your Telegram Bot, I can help you to search a hotel for your trip. What is your name?",
    )
    bot.register_next_step_handler(message, ask_name)


def ask_name(message):
    name = message.text
    user_data[message.chat.id] = {"name": name}
    bot.send_message(
        message.chat.id, f"Nice to meet you, {name}! What ciy interests you for travel?"
    )
    bot.register_next_step_handler(message, lambda msg: ask_city(msg, name))


def ask_city(message, name):
    city = message.text
    user_data[message.chat.id]["city"] = city
    save_user(message.chat.id, name, city)
    bot.send_message(message.chat.id, f"Great! I'll search for hotels in {city}.")
    search_and_send_hotels(message.chat.id)


def search_and_send_hotels(chat_id):
    try:
        city = user_data[chat_id]["city"]
        response_data = search_hotels(city)
        if response_data:
            bot.send_message(chat_id, "Hotel data has been succesfully received:")
            for hotel_info in response_data:
                hotel_name = hotel_info.get("name")
                image_url = hotel_info.get("thumbnail_url")
                link = hotel_info.get("link")
                caption = ""
                if hotel_name:
                    caption += f"City name: {hotel_name}\n"
                if link:
                    caption += f"Linkа: {link}"
                if image_url:
                    bot.send_photo(chat_id, image_url, caption=caption)
                else:
                    bot.send_message(chat_id, caption)
        else:
            bot.send_message(chat_id, "An error retrieving hotel data")
    except Exception as e:
        bot.send_message(
            chat_id,
            "An error occurred while processing your request. Please try again.",
        )
        logging.error("An error occurred while processing hotel search: %s", str(e))


def search_hotels(city):
    try:
        url = "https://tripadvisor-scraper.p.rapidapi.com/hotels/search"
        querystring = {"query": city}
        headers = {
            "x-rapidapi-key": key,
            "x-rapidapi-host": "tripadvisor-scraper.p.rapidapi.com",
        }

        response = requests.get(url, headers=headers, params=querystring)
        if response.status_code == 200:
            return response.json()
        else:
            logging.error(
                "Error retrieving response from API. Status code: %d",
                response.status_code,
            )
            return None
    except Exception as e:
        logging.error("Error while making request to API: %s", str(e))
        return None


@bot.message_handler(commands=["history"])
def history(message):
    db = SessionLocal()
    queries = db.query(UserQuery).filter(UserQuery.chat_id == message.chat.id).all()
    db.close()

    if queries:
        history_text = "\n".join(
            [f"{q.timestamp}: {q.name} searched for {q.city}" for q in queries]
        )
        bot.send_message(message.chat.id, f"History of requests:\n{history_text}")
    else:
        bot.send_message(message.chat.id, "History of requests is empty.")


if __name__ == "__main__":
    logging.info("Bot is starting.")
    try:
        bot.polling()
    except Exception as e:
        logging.critical(f"Critical error in polling: {e}")
