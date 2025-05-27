import sys
sys.path.insert(0, '/home/artemybombastic/ArtemyBombasticGit/OCR_RAZGROM2/Image2Text_bot/.venv')
from Loop.Dataset import Images_Dataset,TestImages_Dataset
from Loop.Model import CRNN
from Loop.Loop import train_loop
from torch.utils.data import DataLoader
from Loop.Out import get_text
import yaml
import torch.nn as nn 
import os
import torch
import torch.optim as optim
import asyncio
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.filters.command import Command
import config
from handlers import router

# Включаем логирование, чтобы не пропустить важные сообщения
logging.basicConfig(level=logging.INFO)
# Объект бота
bot = Bot(
    token = config.BOT_TOKEN,
    default = DefaultBotProperties(
        parse_mode=ParseMode.HTML
    )
)
# Диспетчер
dp = Dispatcher()

# Запуск процесса поллинга новых апдейтов
async def main():
    dp.include_router(router)
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot, allowed_updates=dp.resolve_used_update_types())

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())
