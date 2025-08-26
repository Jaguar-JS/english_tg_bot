from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message

from utils.resource_loader import load_message, load_image
# from utils.message_sender import send_text_buttons

router = Router()


@router.message(Command("date"))
async def cmd_date(message: Message):
    msg = load_message("date")
    date_img = load_image("date_img")
    await message.answer_photo(date_img)

    # await send_text_buttons(
    #     message.chat.id,
    #     msg,
    #     {
    #         "date_grande": "Аріана Гранде",
    #         "date_robbie": "Марго Роббі",
    #         "date_zendaya": "Зендея",
    #         "date_gosling": "Райан Гослінг",
    #         "date_hardy": "Том Харді",
    #     },
    # )
