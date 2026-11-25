# Telegram Join Request Bot

**English** | [Русский](README.ru.md)

A small Telegram bot that sends a personal invitation message to users who request to join a chat or channel. It was built for a trading community to turn join requests into subscribers of the main channel.

## Features

- Handles `chat_join_request` updates and sends the user a private message with a link to the main channel.
- Skips join requests for a configured target chat, so users who are already joining the main channel don't get the invitation.
- `/online` command to check that the bot is running.
- Configuration through environment variables (`.env`): the token is never stored in the code.
- Logs sent messages and handles users who have blocked the bot or never started it.

## Tech stack

- Python 3.10+
- [pyTelegramBotAPI](https://github.com/eternnoir/pyTelegramBotAPI) (telebot)
- python-dotenv

## How it works

1. The bot is added as an administrator to a channel or group with join requests enabled ("Approve new members").
2. When a user taps "Request to join", Telegram sends the bot a `chat_join_request` update.
3. The bot sends the user a private message with the invitation text from [messages.py](messages.py).

## Getting started

```bash
git clone https://github.com/devuiandrew/tg-bot.git
cd tg-bot

python -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate
pip install -r requirements.txt

cp .env.example .env             # then put your token in .env
python tgbot.py
```

### Environment variables

| Variable         | Required | Description                                                   |
|------------------|----------|---------------------------------------------------------------|
| `BOT_TOKEN`      | yes      | Bot token from [@BotFather](https://t.me/BotFather)            |
| `TARGET_CHAT_ID` | no       | ID of the chat whose join requests the bot ignores            |

## Project structure

```
.
├── tgbot.py           # bot entry point and update handlers
├── messages.py        # message templates
├── requirements.txt
└── .env.example       # configuration template
```

## Customization

To change the invitation, edit `JOIN_REQUEST_MESSAGE` in [messages.py](messages.py).
