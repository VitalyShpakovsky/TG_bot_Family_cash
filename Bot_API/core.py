# pip install pytelegrambotapi
import telebot
from telebot import types
from DB.core import crud
import datetime
from settings import BotAPISettings


token = BotAPISettings()
headers = {'Token': token.token_key.get_secret_value()}
bot = telebot.TeleBot(headers['Token'])
create_db = crud.create()
add_user = crud.ad_user()
add_expenses = crud.ad_expenses()
add_income = crud.ad_income()
print_expenses_mount = crud.print_expenses()
print_expenses_year = crud.print_year_expenses()
db = create_db()
category = ''


@bot.message_handler(commands=['user'])
def get_start(message):
    bot.send_message(message.from_user.id, 'Привет как тебя зовут?')
    bot.register_next_step_handler(message, get_user_name)


def get_user_name(message):
    name_user = message.text
    add_user((name_user, message.from_user.id))


@bot.message_handler(commands=['stat'])
def get_expenses(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item10 = types.KeyboardButton("Расходы за год")
    item11 = types.KeyboardButton("Расходы за месяц")
    #item12 = types.KeyboardButton("Детальные расходы за месяц")
    markup.add(item10, item11)
    bot.send_message(message.chat.id, 'Выберите что вам надо', reply_markup=markup)


@bot.message_handler(content_types=['text'])
def get_print_expenses(message):
    if message.text == "Расходы за месяц":
        my_mount = '0' + str(datetime.datetime.now().month)
        result = print_expenses_mount(my_mount)
        for i in result:
            answer = f"{i[0]} потратил(а) за месяц {datetime.datetime.now().strftime('%B')}: {round(i[1], 2)} рублей"
            bot.send_message(message.from_user.id, answer)
    elif message.text == "Расходы за год":
        my_year = str(datetime.datetime.now().year)
        result = print_expenses_year(my_year)
        for i in result:
            answer = f"За {my_year} год {i[0]} потратил(а) в месяце {i[2]}: {round(i[1], 2)} рублей"
            bot.send_message(message.from_user.id, answer)


@bot.message_handler(commands=['add'])
def get_text_command(message):
    bot.send_message(message.from_user.id, 'Welcome to our family')
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("Внести доход")
    item2 = types.KeyboardButton("Внести расход")
    markup.add(item1, item2)
    bot.send_message(message.chat.id, 'Выберите что вам надо', reply_markup=markup)


@bot.message_handler(content_types=['text'])
def get_text_price(message):
    if message.text == "Внести расход":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item3 = types.KeyboardButton("Продукты")
        item4 = types.KeyboardButton("Коммуналка")
        item5 = types.KeyboardButton("Автомобиль")
        item6 = types.KeyboardButton("Транспорт")
        item7 = types.KeyboardButton("Хозтовары")
        item8 = types.KeyboardButton("Одежда и обувь")
        item9 = types.KeyboardButton("Прочие")
        markup.add(item3, item4, item5, item6, item7, item8, item9)
        bot.send_message(message.chat.id, 'Выберите что вам надо', reply_markup=markup)
        bot.register_next_step_handler(message, get_expenses)
    elif message.text == "Внести доход":
        bot.send_message(message.from_user.id, 'Внесите сумму дохода')
        bot.register_next_step_handler(message, get_add_income)


@bot.message_handler(content_types=['text'])
def get_expenses(message):
    global category
    category = message.text
    bot.send_message(message.from_user.id, 'Внесите сумму расходов')
    bot.register_next_step_handler(message, get_add_expenses)


def get_add_expenses(message):
    try:
        expenses = float(message.text)
        add_expenses((message.from_user.id, category, expenses, str(datetime.datetime.now()).split('.')[0]))
        bot.send_message(message.from_user.id, 'Расходы внесены.')
    except ValueError:
        bot.send_message(message.from_user.id, 'Некорректный ввод суммы. Необходимый формат "ХХ.ХХ"')


def get_add_income(message):
    try:
        income = float(message.text)
        add_income((message.from_user.id, income, str(datetime.datetime.now()).split('.')[0]))
        bot.send_message(message.from_user.id, 'Доходы внесены.')
    except ValueError:
        bot.send_message(message.from_user.id, 'Некорректный ввод суммы. Необходимый формат "ХХ.ХХ"')


if __name__ == '__main__':
    bot.polling(none_stop=True, interval=0)