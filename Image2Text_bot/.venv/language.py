from aiogram.types import ReplyKeyboardMarkup
from aiogram.utils.keyboard import ReplyKeyboardBuilder
from aiogram import types, F, Router
from aiogram.types import Message
from aiogram.filters import Command
import text
from aiogram.utils.keyboard import InlineKeyboardBuilder

kb = [
        [
            types.KeyboardButton(text="Русский"),
            types.KeyboardButton(text="English")
        ],
]
keyboard = types.ReplyKeyboardMarkup(
        keyboard=kb,
        resize_keyboard=True,
        input_field_placeholder="ImageToText_bot"
)