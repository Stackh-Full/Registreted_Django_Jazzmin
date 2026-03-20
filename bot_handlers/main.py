import asyncio
import os
import django
from aiogram import Bot, Dispatcher
from aiogram.filters import Command
from aiogram.types import Message
from asgiref.sync import sync_to_async

# Django sozlamalarini yuklash
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'telegram_project.settings')
django.setup()

from bot.models import TelegramUser

# Bot tokeni
BOT_TOKEN = "8553491567:AAGruDlm4chAI76CuKwTSGJiNZxYoHSps44"

# Bot va dispatcher yaratish
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

# /start handler
@dp.message(Command("start"))
async def start_command(message: Message):
    telegram_id = message.from_user.id
    username = message.from_user.username
    first_name = message.from_user.first_name
    
    # Ma'lumotlar bazasiga saqlash
    get_or_create = sync_to_async(TelegramUser.objects.get_or_create)
    
    user, created = await get_or_create(
        telegram_id=telegram_id,
        defaults={
            'username': username,
            'first_name': first_name,
            'is_active': True
        }
    )
    
    if created:
        await message.answer(f"Assalomu alaykum {first_name}! Siz muvaffaqiyatli ro'yxatdan o'tdingiz.")
    else:
        await message.answer(f"Assalomu alaykum {first_name}! Xush kelibsiz.")

# Botni ishga tushirish
async def main():
    print("Bot ishga tushdi...")
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())