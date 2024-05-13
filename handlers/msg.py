from aiogram import Router, types, F

router = Router()

@router.message(F.text)
async def msg(message: types.Message):
    if 'привет' in message.text.lower() or 'здравствуй' in message.text.lower() or 'здрасте' in message.text.lower():
        await message.reply('И тебе привет!')
    elif 'как дела' in message.text.lower() or 'как жизнь' in message.text.lower():
        await message.reply('Нормально, а у тебя?')
    elif 'хорошо' in message.text.lower() or 'отлично' in message.text.lower() or 'лучше всех' in message.text.lower():
        await message.reply('Вот и замечательно!')
    elif 'хреново' in message.text.lower() or 'плохо' in message.text.lower() or 'хуже некуда' in message.text.lower():
        await message.reply('Очень жаль!')
    elif 'не согласен' in message.text.lower() or 'не буду' in message.text.lower():
        await message.reply('Возможно, зря!')
    elif 'не откажусь' in message.text.lower() or 'согласен' in message.text.lower() or 'буду' in message.text.lower():
        await message.reply('Вот и молодец!')
    elif 'откажусь' in message.text.lower():
        await message.reply('Возможно, зря!')
    else:
        await message.reply('Это сложный запрос для меня"... У меня пока еще небольшой словарный запас')