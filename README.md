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

- git clone https://gitlab.com/your-username/your-project.git
- cd python_basic_diploma

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
pip install pyTelegramBotAPI requests
```
**4. Set up API variables: In the code, specify your Telegram bot token and RapidAPI key:**
```sh
python
Skopiuj kod
bot = telebot.TeleBot('5838654687:AAHmGDtKbuulXupRW8zq3sVj-V-qeykaHnI')
headers = {
    "x-rapidapi-key": "edac2fa23cmsh5279dfb3bc3a1c7p1034e1jsn9e9ee202dec5",
    "x-rapidapi-host": "tripadvisor-scraper.p.rapidapi.com"
}
```
## Usage
**Run the script:**
```sh
bash
python main.py
```
