import logging
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import Application, CallbackQueryHandler, CommandHandler, ContextTypes

BOT_TOKEN = "ВСТАВЬТЕ_СЮДА_ТОКЕН"
CHANNEL_ID = "@ваш_канал"

CAPTION = """📌 ТЕСТ: НА ЧТО ВАМ СЕЙЧАС СТОИТ ОБРАТИТЬ ВНИМАНИЕ

Иногда наше подсознание быстрее замечает то, что действительно важно для нас в данный момент.

Посмотрите на изображение и отметьте, что вы увидели первым, не анализируя.

⬇️ Ответы по кнопкам ниже"""

ANSWERS = {
    "cliff": "Если первым вы увидели утес, сейчас вам важно обратить внимание на свою устойчивость и внутренние опоры. Возможно, вы долго держите на себе слишком много ответственности.",
    "cat": "Ваше внимание сейчас стоит направить на свои чувства и внутренние желания. Возможно, вы часто ставите на первое место обязанности или ожидания других людей, забывая о себе.",
    "face": "Сейчас ключевая тема для вас – отношения и общение с людьми. Возможно, в вашей жизни есть разговор, который давно стоит провести, или ситуация, где важно быть более открытым."
}

def build_keyboard():
    return InlineKeyboardMarkup([
        [InlineKeyboardButton("Утес", callback_data="cliff")],
        [InlineKeyboardButton("Кошка", callback_data="cat")],
        [InlineKeyboardButton("Лицо", callback_data="face")],
    ])

async def post(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_photo(
        chat_id=CHANNEL_ID,
        photo="https://i.postimg.cc/your-image.jpg",
        caption=CAPTION,
        reply_markup=build_keyboard()
    )
    await update.message.reply_text("Готово")

async def handle(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer(
        text=ANSWERS[query.data],
        show_alert=True
    )

def main():
    app = Application.builder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("post", post))
    app.add_handler(CallbackQueryHandler(handle))
    app.run_polling()

if __name__ == "__main__":
    main()