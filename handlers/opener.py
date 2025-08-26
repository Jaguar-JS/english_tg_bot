from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message

from utils.resource_loader import  load_message, load_image
from utils.message_sender import send_text

router = Router()


@router.message(Command("opener"))
async def cmd_opener(message: Message):
    msg = load_message("opener")
    opener_img = load_image("opener")
    await message.answer(opener_img)
    await send_text(message, msg)

    # dlg.user.clear()
    # dlg.count = 0
    await send_text(message, "Ім'я партнера?")
