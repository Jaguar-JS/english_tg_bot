from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message

from utils.resource_loader import load_message, load_image
from utils.message_sender import send_text
router = Router()


@router.message(Command("profile"))
async def cmd_profile(message: Message):


    msg = load_message("profile")
    profile_img = load_image("profile")
    await message.answer_photo(profile_img)
    await send_text(message, msg)

    # dlg.user.clear()
    # dlg.count = 0
    await send_text(message, "Скільки вам років?")
