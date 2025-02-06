# Telegram Hotel Search Bot

This project is a Telegram bot for hotel search. The bot uses an external API service to retrieve hotel information and stores user queries in a database.

## 📌 Features
- Search for hotels based on specified parameters.
- Store user query history in a database.
- Log bot activities for debugging and monitoring.

## 🛠️ Technologies
- Python
- `telebot` (pyTelegramBotAPI)
- `requests`
- `SQLAlchemy`
- `dotenv`

## 📂 Installation and Setup

1. Clone the repository:
   ```sh
   git clone https://github.com/yourusername/Telegram-Hotel-Search-Bot.git
   cd Telegram-Hotel-Search-Bot
   ```

2. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```

3. Create a `.env` file and add your API keys:
   ```env
   TELEGRAM_BOT_TOKEN=your_telegram_bot_token
   API_KEY=your_api_key
   ```

4. Run the bot:
   ```sh
   python Telegram-Hotel-Search-Bot.py
   ```

## 📖 Project Files
- `Telegram-Hotel-Search-Bot.py` — main bot script.
- `database.py` — database settings and models.
- `.env` — configuration file with tokens (must be created manually).
- `bot.log` — log file containing bot activity records.

## 🚀 Running the Bot
After installing dependencies and setting up environment variables, simply run:
```sh
python Telegram-Hotel-Search-Bot.py
```

## 🛠 Development and Testing
If you want to modify the bot, it's recommended to use `virtualenv`:
```sh
python -m venv venv
source venv/bin/activate  # For Windows use venv\Scripts\activate
pip install -r requirements.txt
```

## 📜 License
This project is distributed under the MIT License.
