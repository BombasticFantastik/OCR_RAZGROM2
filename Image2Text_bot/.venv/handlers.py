# Основной файл, в котором будет содержать почти весь код бота.
# Будет состоять из функций-обработчиков с декораторами (фильтрами)
import sys
sys.path.insert(0, '/home/artemybombastic/ArtemyBombasticGit/OCR_RAZGROM2/')
from Loop.Out import get_text
import PIL.Image
from aiogram import types, F, Router
from aiogram.types import Message
import requests
import io
import os
import PIL
from aiogram.filters import Command
import text; import language
from aiogram.utils.keyboard import InlineKeyboardBuilder
import yaml
from config import BOT_TOKEN
# router
router = Router()


# option_path='config.yml'
# with open(option_path,'r') as file_option:
#     option=yaml.safe_load(file_option)

#BOT_TOKEN

URI_INFO=f"https://api.telegram.org/bot{BOT_TOKEN}/getFile?file_id="
URI=f"https://api.telegram.org/file/bot{BOT_TOKEN}/"

@router.message(Command("start"))
async def start_handler(msg: Message):
    await msg.answer(text.choose_language, reply_markup=language.keyboard)

@router.message(F.text == "English")
async def hello_message_en(msg: Message):
    await msg.reply(text.hello_message_en, reply_markup=types.ReplyKeyboardRemove())

@router.message(F.text == "Русский")
async def hello_message_ru(msg: Message):
    await msg.reply(text.hello_message_ru, reply_markup=types.ReplyKeyboardRemove())

@router.message(F.text)
async def id_handler(msg: Message):
    await msg.reply("Я обрабатываю только фото, поэтому не отвечаю на сообщения")

@router.message(F.photo)
async def image_handler(msg: Message):
    
    resp=requests.get(URI_INFO + msg.photo[-1].file_id)
    img_path=resp.json()['result']['file_path']
    print(img_path)
    print(f'%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%55')
    img=requests.get(URI+img_path)
    image_pil=PIL.Image.open(io.BytesIO(img.content))
    #image_pil.save('/home/artemybombastic/ArtemyBombasticGit/OCR_RAZGROM2/Image2Text_bot/.venv/users_images/0.jpg')
    text=get_text(None,image_pil,None)
    await msg.answer(text)