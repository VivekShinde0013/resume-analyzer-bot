# bot.py
from email.mime import text
from turtle import update
from urllib import response

from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters
import requests

TOKEN = "7909651802:AAEE9YMNhuQ4u8ZK3gcEMi99GrvrNkbHaZA"

user_data = {}

async def start(update: Update, context):
    await update.message.reply_text("Send Job Description first.")

async def handle_message(update: Update, context):
    user_id = update.message.chat_id

    if user_id not in user_data:
        user_data[user_id] = {"step": 1}

    if user_data[user_id]["step"] == 1:
        user_data[user_id]["job_desc"] = update.message.text
        user_data[user_id]["step"] = 2
        await update.message.reply_text("Now send your resume PDF.")

async def handle_file(update: Update, context):
    user_id = update.message.chat_id

    if user_id not in user_data:
        await update.message.reply_text("Please send job description first.")
        return

    file = await update.message.document.get_file()
    await file.download_to_drive("resume.pdf")

    job_desc = user_data[user_id]["job_desc"]

    await update.message.reply_text("Processing... ⏳")

    response = requests.post(
    "http://127.0.0.1:5000/analyze",
    data={"job_desc": job_desc},
    files={"resume": open("resume.pdf", "rb")}
)

    data = response.json()

# Send analysis text
    def split_text(text, chunk_size=4000):
        return [text[i:i+chunk_size] for i in range(0, len(text), chunk_size)]

    analysis_parts = split_text(data["analysis"])

    for part in analysis_parts:
        await update.message.reply_text(part)   

# Send PDF
    with open(data["pdf_path"], "rb") as f:
        await update.message.reply_document(f)

app = ApplicationBuilder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(MessageHandler(filters.TEXT, handle_message))
app.add_handler(MessageHandler(filters.Document.PDF, handle_file))

app.run_polling()