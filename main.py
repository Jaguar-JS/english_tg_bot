import asyncio
from aiogram import Bot, Dispatcher

from config import TG_BOT_TOKEN
from handlers import register_routes
from middlewares import LoggingMiddleware, PerformanceMiddleware, setup_logging, LoggingConfig

# ---------- Настройка логирования ----------
logging_config = LoggingConfig.from_env()
setup_logging(level=logging_config.DEFAULT_LEVEL)

# ---------- Создание бота/диспетчера ----------
bot = Bot(token=TG_BOT_TOKEN)
dp = Dispatcher()

# ---------- Регистрация middleware ----------
dp.message.middleware(LoggingMiddleware())
dp.message.middleware(PerformanceMiddleware())
dp.callback_query.middleware(LoggingMiddleware())
dp.callback_query.middleware(PerformanceMiddleware())

# ---------- Запуск ----------
async def main():
    register_routes(dp)
    await dp.start_polling(bot)


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("Bot stopped by user.")
