from aiogram import Dispatcher
from handlers.start import router as start_router
from handlers.gpt import router as gpt_router
from handlers.date import router as date_router
from handlers.message import router as message_router
from handlers.profile import router as profile_router
from handlers.opener import router as opener_router



def register_routes(dp: Dispatcher):
    dp.include_router(start_router)
    dp.include_router(gpt_router)
    dp.include_router(date_router)
    dp.include_router(message_router)
    dp.include_router(profile_router)
    dp.include_router(opener_router)




