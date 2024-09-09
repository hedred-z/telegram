import os
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler

TOKEN = os.getenv("TELEGRAM_TOKEN")

# Функция, которая будет отправлять сообщение о техническом обслуживании
async def maintenance_message(update: Update, context):
    await update.message.reply_text("Извините, сейчас ведутся технические работы. Пожалуйста, попробуйте позже.")

if __name__ == '__main__':
    # Инициализация бота
    application = ApplicationBuilder().token(TOKEN).build()

    # Обработчик команды /start и любых других команд
    start_handler = CommandHandler('start', maintenance_message)
    application.add_handler(start_handler)

    # Запуск бота
    application.run_polling()
