from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

# Установите ваш токен напрямую
TOKEN = '7078975365:AAGyaxbZ74ozc1PLQy9tRQNG-vtfZuN2brM'

# Функция, которая отправляет сообщение о представлении игры
async def welcome_message(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    welcome_text = (
        "Welcome to Vortix🌪️! 🎉🎉🎉\n\n"
        "At Vortix, we’re revolutionizing gaming with an exciting new experience in Telegram. Dive into our world where you can:\n\n"
        "💥 **Play and Win**: Engage in thrilling games and challenges to earn exclusive rewards.\n"
        "👫 **Invite Friends**: Bring your friends and family to join the fun. More friends mean more rewards!\n"
        "🏆 **Complete Quests**: Take on various quests and missions to rack up amazing bonuses!\n\n"
        "Get started now and see what incredible rewards await you! 🚀\n\n"
        "Stay tuned and keep exploring! 🌟\n"
        "[Launch Vortix🌪️](#) \n"
        "[Join our Channel](https://t.me/VortixCrypto)"
    )
    await update.message.reply_text(welcome_text, parse_mode='MarkdownV2')

if __name__ == '__main__':
    # Инициализация бота
    application = ApplicationBuilder().token(TOKEN).build()

    # Обработчик команды /start и любых других команд
    start_handler = CommandHandler('start', welcome_message)
    application.add_handler(start_handler)

    # Запуск бота
    application.run_polling()
