from aiogram import types


button1 = types.KeyboardButton(text='Старт!')
button2 = types.KeyboardButton(text='Приветствие гостю!')
button3 = types.KeyboardButton(text='Угадай мое число от 0 до 10')
button4 = types.KeyboardButton(text='Обо мне')
button5 = types.KeyboardButton(text='Прими к сведению!')
button6 = types.KeyboardButton(text='Словарный запас')
button7 = types.KeyboardButton(text='Покажи лису')
button8 = types.KeyboardButton(text='Профессия')
keyboard1 = [
    [button1, button2, button6],
    [button3, button4, button5],
    [button8, button7]
]


keyboard = types.ReplyKeyboardMarkup(keyboard=keyboard1, resize_keyboard=True)
