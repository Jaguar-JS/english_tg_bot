from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message

from utils.resource_loader import load_message
# from utils.message_sender import send_text_buttons

router = Router()


@router.message(Command("message"))
async def cmd_message(message: Message):

    txt = load_message("message")
    message_img = load_message("message_img")
    await message.answer_photo(message_img)

    # await send_text_buttons(
    #     message
    #     txt,
    #     {
    #         "message_next": "Написати повідомлення",
    #         "message_date": "Запросити на побачення",
    #     },
    # )

    # dlg.list.clear()
