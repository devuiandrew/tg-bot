"""Telegram bot that replies to chat join requests with an invitation message."""

import logging
import os

import telebot
from dotenv import load_dotenv

from messages import JOIN_REQUEST_MESSAGE

load_dotenv()

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
)
logger = logging.getLogger(__name__)


def get_config() -> tuple[str, int | None]:
    """Read bot settings from environment variables."""
    token = os.getenv("BOT_TOKEN")
    if not token:
        raise RuntimeError("BOT_TOKEN is not set. Copy .env.example to .env and fill it in.")

    target_chat_id = os.getenv("TARGET_CHAT_ID")
    return token, int(target_chat_id) if target_chat_id else None


BOT_TOKEN, TARGET_CHAT_ID = get_config()
bot = telebot.TeleBot(BOT_TOKEN)


@bot.chat_join_request_handler()
def handle_join_request(request: telebot.types.ChatJoinRequest) -> None:
    """Send the invitation message to a user who asked to join a chat."""
    if request.chat.id == TARGET_CHAT_ID:
        return

    try:
        bot.send_message(request.from_user.id, JOIN_REQUEST_MESSAGE)
        logger.info("Sent invitation to user %s (chat %s)", request.from_user.id, request.chat.id)
    except telebot.apihelper.ApiTelegramException as error:
        logger.warning("Could not message user %s: %s", request.from_user.id, error)


@bot.message_handler(commands=["online"])
def handle_online(message: telebot.types.Message) -> None:
    """Health check: confirm that the bot is running."""
    bot.reply_to(message, "Я онлайн ✅")


if __name__ == "__main__":
    logger.info("Bot started")
    bot.infinity_polling(allowed_updates=["message", "chat_join_request"])
