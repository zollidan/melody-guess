from aiogram import F, Router
from aiogram.types import Message, CallbackQuery
from sqlalchemy.ext.asyncio import AsyncSession

from bot.base import UserDAO
from bot.keyboards.kbs import main_kb

rating_router = Router()

@rating_router.callback_query(F.data == "leader_board")
async def leader_board(callback: CallbackQuery, session_without_commit: AsyncSession):
    
        leader_board = await UserDAO.find_by_points_desc(session=session_without_commit)
        
        if not leader_board:
            return await callback.message.answer("Таблица лидеров пуста. Будьте первым!", reply_markup=main_kb())
            
        
        leader_board_rows = []
        for i, user in enumerate(leader_board):
            prefix = ""
            if i == 0:
                prefix = "🥇 "  
            elif i == 1:
                prefix = "🥈 "  
            elif i == 2:
                prefix = "🥉 "  
            else:
                prefix = f"{i + 1}. "
                
            leader_board_rows.append(f"{prefix}{user.first_name} — {user.points} очков")
        
        leader_board_table = "\n".join(leader_board_rows)

        leader_board_text = f"🏆 <b>ТАБЛИЦА ЛИДЕРОВ</b> 🏆\n\n{leader_board_table}\n\n<i>Продолжайте зарабатывать очки, чтобы подняться выше!</i>"

        
        return await callback.message.answer(leader_board_text, parse_mode="HTML", reply_markup=main_kb())