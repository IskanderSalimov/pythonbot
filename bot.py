import telebot
import random
import config  # Ваш файл config.py

# Предполагаем, что в config.py есть строка: TOKEN = "ваш_токен"
bot = telebot.TeleBot(config.TOKEN)

# Класс House
class House:
    def __init__(self, build="Неизвестно", price="Неизвестно"):
        self.build = build
        self.price = price

    def info(self):
        return f"Постройка: {self.build}, Цена: {self.price}"

houses = House(build="Кирпичный", price="10000$")

# Класс Car
class Car:
    def __init__(self, color="Неизвестно", brand="Неизвестно"):
        self.color = color
        self.brand = brand

    def info(self):
        return f"Цвет: {self.color}, Марка: {self.brand}"

# Список шуток
jokes = [
    "Если тебе попало это то ты крутой!",
    "Если тебе попало это то ты жесткий!",
    "Если тебе попало это то ты везучий!"
]

# Обработчик команды '/start' и '/help'
@bot.message_handler(commands=['help', 'start'])
def send_welcome(message):
    bot.reply_to(message, """\
Привет я телеграмм бот.
Я могу делать много команд, введите /info что бы узнать все команды.
fadikCompany©\
""")

# Обработчик команды '/info'
@bot.message_handler(commands=["info"])
def send_info(message):
    bot.reply_to(message, f'Этот бот самый лучший в России {bot.get_me().first_name}, он может выполнять команды: /start /help /info /joke /house /car')

# Обработчик команды '/joke'
@bot.message_handler(commands=["joke"])
def send_joke(message):
    joke = random.choice(jokes)
    bot.reply_to(message, joke)

# Обработчик команды '/house'
@bot.message_handler(commands=["house"])
def send_house(message):
    try:
        # Получение аргументов команды
        ars = message.text.split(maxsplit=2)
        if len(ars) < 3:
            bot.reply_to(message, "Используйте команду так: /house (Постройка (кирпичная и тд.) и цена)")
            return
        
        build = ars[1]
        price = ars[2]

        # Создание экземпляра Car
        house = House(build=build, price=price)
        bot.reply_to(message, house.info())

    except Exception as e:
        bot.reply_to(message, "Произошла ошибка при обработке команды. Проверьте введённые данные.")

# Обработчик команды '/car'
@bot.message_handler(commands=["car"])
def send_car(message):
    try:
        # Получение аргументов команды
        args = message.text.split(maxsplit=2)
        if len(args) < 3:
            bot.reply_to(message, "Используйте команду так: /car цвет марка")
            return
        
        color = args[1]
        brand = args[2]

        # Создание экземпляра Car
        car = Car(color=color, brand=brand)
        bot.reply_to(message, car.info())

    except Exception as e:
        bot.reply_to(message, "Произошла ошибка при обработке команды. Проверьте введённые данные.")

# Обработчик всех остальных сообщений
@bot.message_handler(func=lambda message: True)
def echo_message(message):
    bot.reply_to(message, message.text)

# Запуск бота
bot.infinity_polling()
