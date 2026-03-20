from aiogram import Router, types
from aiogram.filters import Command
import django
import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'telegram_project.settings')
django.setup()

from bot.models import TelegramUser

router = Router()

@router.message(Command("start"))
async def start_command(message: types.Message):
    telegram_id = message.from_user.id
    username = message.from_user.username
    first_name = message.from_user.first_name
    
    user, created = TelegramUser.objects.get_or_create(
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


