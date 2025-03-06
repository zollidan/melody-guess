
from aiogram import Router, F
from aiogram.filters import CommandStart, Command
from aiogram.types import Message, ReplyKeyboardMarkup, KeyboardButton

from app.keyboards.kbs import start_kb

start_router = Router()

@start_router.message(CommandStart())
async def start_command(message: Message):
    
    user = message.from_user.id
    
    # Если пользователя нет, добавляем его в базу
    # if not user:
    #     user = User(
    #         telegram_id=message.from_user.id,
    #         username=message.from_user.username,
    #         first_name=message.from_user.first_name,
    #         last_name=message.from_user.last_name
    #     )
    #     session.add(user)
        
    #     # Создаем запись состояния пользователя
    #     user_state = UserState(
    #         user_id=user.user_id,
    #         current_state="start"
    #     )
    #     session.add(user_state)
    #     session.commit()
    
    # Формируем приветственное сообщение
    greeting_text = f"""
🎵 *Добро пожаловать в игру «Угадай мелодию»!* 🎵

Привет, {message.from_user.first_name}! 

В этой игре пользователи сами создают музыкальную базу, напевая известные треки. 

*Как играть:*
1️⃣ Сначала запишите свой напев для общей библиотеки
2️⃣ Затем угадывайте мелодии, которые напели другие участники
3️⃣ Получайте очки за каждый угаданный трек
4️⃣ Следите за рейтингом своих напевов

*Ваш текущий счёт:* user.points очков

Выберите действие на клавиатуре ниже 👇
"""
    
    # Отправляем сообщение
    await message.answer(greeting_text, reply_markup=start_kb())
    
    # # Обновляем состояние пользователя
    # user_state = session.query(UserState).filter(UserState.user_id == user.user_id).first()
    # if user_state:
    #     user_state.current_state = "main_menu"
    #     user_state.last_interaction = datetime.utcnow()
    #     session.commit()