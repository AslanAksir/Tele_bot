from aiogram import Router, types, F
from aiogram.filters.command import Command
import logging
import random
from keyboards.keyboards import keyboard
from utils.random_fox import fox
from slovar import dict_1

router = Router()

# @router.message(Command(commands=['старт', 'start']))
# async def start(message: types.Message):
#     await message.answer(f'Привет, {message.from_user.full_name}!', reply_markup=keybo

@router.message(Command(commands=['старт!', 'start']))
@router.message(F.text.lower() == 'старт!')
async def start(message: types.Message):
    await message.answer(f'Поехали!, {message.from_user.full_name}!', reply_markup=keyboard)

@router.message(F.text.lower() == 'приветствие гостю!')
async def start(message: types.Message):
    await message.answer(f'Приветствую тебя, {message.chat.first_name}! Как дела!')

@router.message(Command(commands=['прими к сведению!', 'info']))
@router.message(F.text.lower() == 'прими к сведению!')
async def info(message: types.Message):
    number = 'не знаю'
    await message.answer(f'Если ты используешь слова и выражения '
                         f'из моего словарного запаса, то, наверняка, получишь '
                         f'ответ. В противном случае, жди пока он расширится')

@router.message(Command(commands=['обо мне', 'about_me']))
@router.message(F.text.lower() == 'обо мне')
async def about_me(message: types.Message):
    print(message.from_user.full_name)
    await message.answer(f'Привет! Я бот, который еще толком не знает чего хочет! '
                         f'А  чего хочешь ты, {message.chat.first_name}, я тоже не знаю, но догадываюсь. '
                         f'Думаю, ты не откажешься от кофе с пирожным.')

@router.message(Command(commands=['словарный запас', 'dictin']))
@router.message(F.text.lower() == 'словарный запас')
async def dictin(message: types.Message):
    # print(f'У меня пока небольшой словарный запас')
    await message.answer(f'У меня пока небольшой словарный запас. Я распознаю следующие слова и сочетания слов {dict_1}')

@router.message(Command(commands=['угадай мое число от 0 до 10', 'info']))
@router.message(F.text.lower() == 'угадай мое число от 0 до 10')
async def info(message: types.Message):
    number = random.randint(0, 10)
    await message.answer(f'Мое число: {number}! Если ты его угадал, очень возможно, что твое желание сбудется.')

# @router.message(Command(commands=['стоп']))
# @router.message(Command(commands=['stop']))
# async def stop(message: types.Message):
#     print(message.from_user.full_name)
#     await message.answer(f'Привет, {message.chat.first_name}!')
#
#
# @router.message(Command(commands=['инфо', 'info']))
# @router.message(F.text.lower() == 'инфо')
# async def info(message: types.Message):
#     number = random.randint(0, 100)
#     await message.answer(f'Привет, твоё число: {number}!')


@router.message(F.text.lower() == 'покажи лису')
async def info(message: types.Message):
    img_fox = fox()
    await message.answer('Привет, лови лису')
    await message.answer_photo(img_fox)
    # img_fox = fox()
    # await bot.send_photo(message.from_user.id, img_fox)