import os
import asyncio
from pathlib import Path
from dotenv import dotenv_values
from telebot.async_telebot import AsyncTeleBot
from revChatGPT.ChatGPT import Chatbot

# get config
parent_dir = Path(__file__).resolve().parent
config = dotenv_values(f"{parent_dir}/.env")

# init telegram bot
BOT_TOKEN = config["BOT_TOKEN"]
bot = AsyncTeleBot(BOT_TOKEN)

# init chatbot
chatbot = Chatbot(
    {"session_token": config["SESSION_TOKEN"]}, conversation_id=None, parent_id=None
)
print("Chatbot & TeleBot initialized ")

# define a message handler to send a message when the command /start is issued
@bot.message_handler(commands=["start", "hello"])
async def send_welcome(message):
    await bot.reply_to(message, "Hello, how are you doing?")


# define a message handler to send a message when the command /gpt is issued
@bot.message_handler(commands=["gpt"])
async def send_gpt(message):
    print("Working with chatgpt")
    await bot.send_message(message.chat.id, "Working with chatgpt. Gimme a sec...")
    response = chatbot.ask(message.text.replace("/gpt", ""))
    await bot.reply_to(message, response["message"])


# run the bot
asyncio.run(bot.polling())
