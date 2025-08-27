from aiogram import Router, F
from aiogram.filters import Command
from aiogram.types import Message
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext

from utils.resource_loader import load_image, load_prompt
from utils.message_sender import send_text
from services.openai import chatgpt

router = Router()

class ChatGPTDialog(StatesGroup):
    waiting_for_message = State()

@router.message(Command("gpt"))
async def cmd_gpt(message: Message, state: FSMContext):
    gpt_img = load_image("gpt")
    system_prompt = load_prompt("main")
    
    chatgpt.set_prompt(system_prompt)
    await message.answer_photo(gpt_img)
    await send_text(message, "Напишіть повідомлення *ChatGPT*:")
    await state.set_state(ChatGPTDialog.waiting_for_message)

@router.message(ChatGPTDialog.waiting_for_message)
async def process_gpt_message(message: Message, state: FSMContext):
    user_message = message.text
    
    # Отправляем "печатает" статус
    placeholder = await message.answer("Думаю. Очікуйте...")
    
    try:
        response = await chatgpt.add_message(user_message)
        await placeholder.edit_text(response)
    except Exception as e:
        await placeholder.edit_text(f"❌ Помилка: {str(e)}")
        await state.clear()
        return

    # Остаемся в том же состоянии для продолжения диалога
    await state.set_state(ChatGPTDialog.waiting_for_message)

