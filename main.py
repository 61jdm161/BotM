from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import random
import os

TOKEN = os.getenv("BOT_TOKEN")
COMPLIMENTS = [
    "Ты сегодня особенно прекрасна 💖",
    "Твоя улыбка способна растопить лёд 🧊😊",
    "Ты как солнечный луч в пасмурный день ☀️",
    "Какая красивая сосочка ❤️",
    "Вот это попка оууу май ❤️",
    "Ты вдохновляешь меня каждый день ✨"
]

GIRLFRIEND_CHAT_ID = 527467559

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Привет! Я бот. Напиши пожалуйста команду /id в чат со мной")

app = ApplicationBuilder().token(TOKEN).build()

async def compliment(update: Update, context: ContextTypes.DEFAULT_TYPE):
    compliment_text = random.choice(COMPLIMENTS)
    try:
        await context.bot.send_message(chat_id=GIRLFRIEND_CHAT_ID, text=compliment_text)
        await update.message.reply_text("Комплимент отправлен!")
    except Exception as e:
        await update.message.reply_text(f"Ошибка: {e}")


async def debug(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(f"Твой chat_id: {update.message.chat_id}")

app.add_handler(CommandHandler("id", debug))
app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("compliment", compliment))
app.run_polling()
