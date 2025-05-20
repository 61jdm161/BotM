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
    "Ты вдохновляешь меня каждый день ✨",
    "Ты моё лучшее уведомление ❤️",
    "С тобой даже утро понедельника — праздник ☀️",
    "Ты — мой любимый баг, который я никогда не захочу фиксить 🐞",
    "Ты как `git push` — без тебя не работает ❤️",
    "Даже если весь мир будет оффлайн, ты всегда будешь моим онлайн 🌍",
    "Ты — мой главный приоритет в таск-трекере жизни 💼",
    "Твоя улыбка — лучший дебаг моего настроения 😊",
    "Ты как хорошая база данных — всё держишь в порядке 💾",
    "С тобой я чувствую себя как в release version 😎",
    "Ты красива даже без `filters` и `effects` 🎨",
    "Ты как горячий кофе утром — нужна и пробуждаешь ☕",
    "Когда ты рядом — даже боты улыбаются 🤖💘",
    "С тобой хочется делать pull к сердцу каждый день ❤️",
    "Ты — мой бессрочный premium-доступ к счастью ✨",
    "Каждый твой взгляд — как commit в моё сердце 💓",
    "Ты умеешь быть одновременно спокойной и взрывной, как идеально написанный код ⚡",
    "Ты как редкий артефакт в игре — бесценна 🎮",
    "Ты — самый красивый фрейм в моей жизни 📸",
    "В тебе всё — и стиль, и substance 💅",
    "Ты — моё любимое исключение из всех правил 🧠❤️",
    "Ты не просто идеальна — ты стабильна, как сервер в проде 🖥️",
    "Если бы красота была ошибкой, ты была бы только предупреждением 😉",
    "Я бы с радостью завис с тобой в любой сессии 💬",
    "Ты как свежий билд — каждый день удивляешь ✨",
    "Ты — лучший апгрейд моего настроения 💖",
    "Ты как баг, который делать не надо, но он прекрасен 😏",
    "Ты — моё безопасное подключение по HTTPS к счастью 🔐",
    "Ты как уникальный ключ — подходишь только к моему сердцу 🗝️",
    "Ты — главная причина, по которой хочется жить осмысленно 🧭",
    "С тобой каждый день — как новый релиз: лучше и лучше 💌"
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
