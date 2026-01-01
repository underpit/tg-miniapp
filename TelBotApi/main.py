from telegram import Update, KeyboardButton, ReplyKeyboardMarkup, WebAppInfo
from telegram.ext import Application, CommandHandler, ContextTypes

TOKEN = ""

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        KeyboardButton("Открыть Web App", web_app=WebAppInfo(url="https://example.com") )
    ]
    await update.message.reply_text(
        "Нажмите кнопку ниже, чтобы открыть Web App:",
        reply_markup=ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
        )
    
async def web_app_data(update: Update, context: ContextTypes.DEFAULT_TYPE):
    data = update.message.web_app_data
    print("Получены данные из Web App:", data)

    await update.message.reply_text("Данные успешно получены!")

app = Application.builder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("web_app_data", web_app_data))

app.run_polling()