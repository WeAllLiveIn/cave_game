from aiogram import Bot, Dispatcher, F
from aiogram.filters import Command
from aiogram.types import Message, ContentType
from random import choice


API_TOKEN: str = '6229545177:AAHTBT9m2CfH_I-RbpI2m1hn5R9H7C3pXtA'
bot: Bot = Bot(API_TOKEN)
dsp: Dispatcher = Dispatcher()


dsp.message.register(process_start, Command(commands=['start']))
dsp.message.register(process_photo, F.content_type == ContentType.PHOTO)
dsp.message.register(process_mes)

if __name__ == "__main__":
    dsp.run_polling(bot)