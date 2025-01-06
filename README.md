# Telegram Hotel Finder Bot

This project is a Telegram bot that helps users find hotels in cities they are interested in. The bot uses the TripAdvisor API to search for hotel information.

## Getting Started
These instructions will help you clone the project and run it on your local computer for development and testing.

## Prerequisites
What you need to install to run the project:

- Python 3.x
- pyTelegramBotAPI
- requests

## Installation
Follow these steps to set up the project:

**1. Clone the repository:**
```sh
bash
- git clone [https://gitlab.com/your-username/your-project.git](https://github.com/diankaaaa21/Telegram-Hotel-Search-Bot.git)
- cd Telegram-Hotel-Search-Bot
```
**2. Create and activate a virtual environment (recommended):**
```sh
bash
python -m venv env
source env/bin/activate    # For Linux/Mac
env\Scripts\activate       # For Windows
```
**3. Install dependencies:**
```sh
bash
pip install pyTelegramBotAPI requests dotenv
```
**4. Set up API variables: In the code, specify your Telegram bot token and RapidAPI key:**
```sh
python
Skopiuj kod
bot = telebot.TeleBot('TELEGRAM_BOT_TOKEN')
headers = {
    "x-rapidapi-key": "API_KEY",
    "x-rapidapi-host": "tripadvisor-scraper.p.rapidapi.com"
}
```
## Usage
**Run the script:**
```sh
bash
python main.py
```
