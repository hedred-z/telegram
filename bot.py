from telegram import Update
from telegram.ext import Application, CommandHandler

TOKEN = '7078975365:AAGyaxbZ74ozc1PLQy9tRQNG-vtfZuN2brM'

# Обработчик команды /start
def start(update: Update, context):
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
    update.message.reply_text(welcome_text, parse_mode='Markdown')

# Основная функция
def main():
    # Инициализация бота
    application = Application.builder().token(TOKEN).build()

    # Обработчик команды /start
    application.add_handler(CommandHandler('start', start))

    # Запуск polling в синхронном режиме
    application.run_polling()

if __name__ == '__main__':
    main()
