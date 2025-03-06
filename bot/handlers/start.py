
from aiogram import Router, F
from aiogram.filters import CommandStart, Command
from aiogram.types import Message, ReplyKeyboardMarkup, KeyboardButton
from sqlalchemy.ext.asyncio import AsyncSession
from bot.base import UserDAO
from bot.keyboards.kbs import start_kb
from bot.schemas import UserSchema, TelegramIDBase



start_router = Router()

@start_router.message(CommandStart())
async def start_command(message: Message, session_with_commit: AsyncSession):
    
    greeting_text = f"""
🎵 *Добро пожаловать в игру «Угадай мелодию»!* 🎵

Привет, {message.from_user.first_name}! 

В этой игре пользователи сами создают музыкальную базу, напевая известные треки. 

Как играть:
1️⃣ Сначала запишите свой напев для общей библиотеки
2️⃣ Затем угадывайте мелодии, которые напели другие участники
3️⃣ Получайте очки за каждый угаданный трек
4️⃣ Следите за рейтингом своих напевов

Выберите действие на клавиатуре ниже 👇
"""
    

    
    user_id = message.from_user.id
    user_info = await UserDAO.find_one_or_none(
        session=session_with_commit,
        filters=TelegramIDBase(telegram_id=user_id)
    )
    
    if user_info:
        return await message.answer(
            f"👋 Привет, {message.from_user.full_name}! Добро пожаловать! Ваш текущий счет {user_info.points} очков!",
            reply_markup=start_kb()
            )   

    values = UserSchema(
        telegram_id=user_id,
        username=message.from_user.username,
        first_name=message.from_user.first_name,
        last_name=message.from_user.last_name,
    )
    
    await UserDAO.add(session=session_with_commit, values=values)
    await message.answer(greeting_text,
                         reply_markup=start_kb())
   
    