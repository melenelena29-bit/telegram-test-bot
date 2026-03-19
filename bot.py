import os
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

BOT_TOKEN = os.getenv("BOT_TOKEN")
CHANNEL_ID = os.getenv("CHANNEL_ID")
IMAGE_URL = os.getenv("IMAGE_URL")


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text="Бот работает 🚀")


async def send_post(context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_photo(
        chat_id=CHANNEL_ID,
        photo=IMAGE_URL,
        caption="Тестовый пост"
    )


if __name__ == "__main__":
    app = ApplicationBuilder().token(BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start))

    app.job_queue.run_repeating(send_post, interval=60, first=10)

    print("Бот запущен...")
    app.run_polling()
