from aiogram import Router
from aiogram.types import Message
from aiogram.filters import CommandStart
from aiogram.enums.parse_mode import ParseMode  # Import ParseMode

from keyboards.menu import menu_keyboard
from utils.resource_loader import load_message, load_image  # Import load_image
from utils.message_sender import send_html, send_text  # Import send_text

router = Router()


@router.message(CommandStart())
async def start(message: Message):
    main_image = load_image("main")  # Load the main image
    await message.answer_photo(main_image)  # Send the image

    start_message = load_message("main")  # Load the start message
    await send_text(
        message,
        start_message.format(first_name=message.from_user.first_name)
        )
    # await message.answer(
    #     start_message,
    #     reply_markup=menu_keyboard(),
    #     parse_mode=ParseMode.MARKDOWN,  # Set Markdown as the parse mode
    # )
