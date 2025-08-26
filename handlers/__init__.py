from aiogram import Dispatcher
from handlers.start import router as start_router
from handlers.gpt import router as gpt_router
from handlers.llama import router as llama_router
from handlers.date import router as date_router
from handlers.message import router as message_router
from handlers.profile import router as profile_router
from handlers.opener import router as opener_router
from handlers.info import router as info_router
from handlers.catalog import router as catalog_router


def register_routes(dp: Dispatcher):
    dp.include_router(start_router)
    dp.include_router(gpt_router)
    dp.include_router(llama_router)
    dp.include_router(date_router)
    dp.include_router(message_router)
    dp.include_router(profile_router)
    dp.include_router(opener_router)
    dp.include_router(info_router)
    dp.include_router(catalog_router)


