from aiogram.types import InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder

def start_kb() -> InlineKeyboardMarkup:
    kb = InlineKeyboardBuilder()
    kb.button(text="🎮 Начать игру", callback_data='start_game')
    kb.button(text="🎵 Добавить напев", callback_data='add_song')
    kb.button(text="📊 Мои рейтинги", callback_data='my_ratings')
    kb.button(text="🏆 Таблица лидеров", callback_data='leader_board')
    kb.button(text="🎯 Ежедневное задание", callback_data='daily_tasks')
    kb.button(text="❓ Помощь", callback_data='help')
    kb.adjust(1)
    return kb.as_markup()
    
