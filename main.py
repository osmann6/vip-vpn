import telebot
from telebot import types
import os

TOKEN = os.environ.get("BOT_TOKEN")  # Добавь токен в переменные окружения на Render
bot = telebot.TeleBot(TOKEN)

# --- Команда /start ---
@bot.message_handler(commands=['start'])
def welcome(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("⚡ Купить VIPvpn")
    item2 = types.KeyboardButton("🎁 Пробная версия 10 дней")
    item3 = types.KeyboardButton("👨‍💻 Поддержка")

    markup.add(item1)
    markup.add(item2)
    markup.add(item3)

    bot.send_message(
        message.chat.id,
        "👋 Привет! Добро пожаловать в *VIPvpn* — твой премиум VPN и обход блокировок 🔥\n\n"
        "🌐 Этот VPN не просто защищает соединение — он *обходит блокировки и ограничения операторов!* 🚀\n\n"
        "💎 *С VIPvpn без проблем работает интернет даже при блокировках!* "
        "Работает *YouTube, Instagram и даже TikTok!* (📲 *скачивать моды больше не нужно!*)\n\n"
        "Выбери действие ниже 👇",
        parse_mode="Markdown",
        reply_markup=markup
    )

# --- Обработка кнопок ---
@bot.message_handler(func=lambda message: True)
def handle_buttons(message):
    if message.text == "⚡ Купить VIPvpn":
        bot.send_message(
            message.chat.id,
            "💳 *Тарифы VIPvpn:*\n\n"
            "🧪 10 дней — 299₽ *(пробная версия)*\n"
            "📅 1 месяц — 799₽ *(скидка 200₽)*\n"
            "🕒 2 месяца — 1399₽ *(скидка 200₽)*\n"
            "📆 3 месяца — 1999₽ *(скидка 400₽)*\n"
            "🔥 6 месяцев — 3099₽ *(скидка 1700₽)*\n\n"
            "💬 Для покупки напиши оператору: @vipvpnoperator",
            parse_mode="Markdown"
        )

    elif message.text == "🎁 Пробная версия 10 дней":
        bot.send_message(
            message.chat.id,
            "🎁 *Пробная версия VIPvpn на 10 дней — всего 299₽!*\n\n"
            "Попробуй премиум-качество прямо сейчас 💎\n"
            "Напиши оператору для активации ➡️ @vipvpnoperator",
            parse_mode="Markdown"
        )

    elif message.text == "👨‍💻 Поддержка":
        bot.send_message(
            message.chat.id,
            "👨‍💻 Связь с оператором: @vipvpnoperator\n"
            "📞 Мы на связи 24/7 — по всем вопросам и настройке VPN 💬",
            parse_mode="Markdown"
        )

# --- Запуск ---
bot.polling(none_stop=True)
