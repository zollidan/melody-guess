
from aiogram import F, Router
from aiogram.types import CallbackQuery, Message
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import selectinload

from bot.base import UserDAO, HummingSampleDAO
from bot.keyboards.kbs import main_kb
from bot.model import User
from bot.schemas import HummingSchema, TelegramIDBase

game_router = Router()

class GameState(StatesGroup):
    waiting_for_voice = State()

@game_router.callback_query(F.data == 'start_game')
async def start_game(callback: CallbackQuery, session_without_commit: AsyncSession, state: FSMContext):
    
    await callback.answer('')
    
    # почему то достается в callback id пользователя только в чате
    user_id = callback.message.chat.id
    
    sample = await HummingSampleDAO.user_has_samples(session_without_commit, user_id)
    
    if not sample:
        await callback.message.answer("Похоже у вас нет напевов(\nСначала вам надо добавить свой напев в базу. Запишите голосовое сообщение с напевом, чтобы другие угадывали вашу песню!")
    
        await state.set_state(GameState.waiting_for_voice)
    else:
        await callback.message.answer("Игра началась!")
    

@game_router.message(GameState.waiting_for_voice)
async def process_voice_message(message: Message, state: FSMContext, session_with_commit: AsyncSession):
    if not message.voice:
        await message.answer("Пожалуйста, отправьте именно голосовое сообщение.")
        return
    
    # проверить наличие напева в сообщении
    
    file_id = message.voice.file_id
    user_id = message.from_user.id
    
    values = HummingSchema(
        user_id=user_id,
        file_id=file_id,
        song_title='title',
        song_artist='artist'
    )

    await HummingSampleDAO.add(session=session_with_commit, values=values)
    
    await state.clear()