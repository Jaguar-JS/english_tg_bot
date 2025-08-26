import logging
import json
from datetime import datetime
from typing import Any, Dict
from aiogram import BaseMiddleware
from aiogram.types import TelegramObject, Message, CallbackQuery
from aiogram.enums import ChatType


class StructuredFormatter(logging.Formatter):
    """Форматтер для structured logging с JSON"""
    
    def format(self, record: logging.LogRecord) -> str:
        log_entry = {
            "timestamp": datetime.fromtimestamp(record.created).isoformat(),
            "level": record.levelname,
            "logger": record.name,
            "message": record.getMessage(),
            "module": record.module,
            "function": record.funcName,
            "line": record.lineno
        }
        
        # Добавляем extra поля если есть
        if hasattr(record, 'extra_data'):
            log_entry.update(record.extra_data)
            
        return json.dumps(log_entry, ensure_ascii=False, default=str)


class LoggingMiddleware(BaseMiddleware):
    """Middleware для логирования всех событий бота"""
    
    def __init__(self, logger_name: str = "bot_middleware"):
        super().__init__()
        self.logger = logging.getLogger(logger_name)
        
    async def __call__(
        self,
        handler: callable,
        event: TelegramObject,
        data: Dict[str, Any]
    ) -> Any:
        # Логируем входящее событие
        await self._log_incoming_event(event, data)
        
        try:
            # Выполняем обработчик
            result = await handler(event, data)
            
            # Логируем успешное выполнение
            await self._log_success_event(event, data)
            
            return result
            
        except Exception as e:
            # Логируем ошибку
            await self._log_error_event(event, data, e)
            raise
    
    async def _log_incoming_event(self, event: TelegramObject, data: Dict[str, Any]) -> None:
        """Логирование входящего события"""
        extra_data = {
            "event_type": event.__class__.__name__,
            "user_id": self._get_user_id(event),
            "chat_id": self._get_chat_id(event),
            "chat_type": self._get_chat_type(event),
            "action": "incoming"
        }
        
        if isinstance(event, Message):
            extra_data.update({
                "text": event.text[:100] if event.text else None,
                "message_id": event.message_id
            })
        elif isinstance(event, CallbackQuery):
            extra_data.update({
                "callback_data": event.data,
                "message_id": event.message.message_id if event.message else None
            })
        
        self.logger.info("Incoming event", extra={"extra_data": extra_data})
    
    async def _log_success_event(self, event: TelegramObject, data: Dict[str, Any]) -> None:
        """Логирование успешного выполнения"""
        extra_data = {
            "event_type": event.__class__.__name__,
            "user_id": self._get_user_id(event),
            "action": "success"
        }
        
        self.logger.info("Event processed successfully", extra={"extra_data": extra_data})
    
    async def _log_error_event(self, event: TelegramObject, data: Dict[str, Any], error: Exception) -> None:
        """Логирование ошибки"""
        extra_data = {
            "event_type": event.__class__.__name__,
            "user_id": self._get_user_id(event),
            "error_type": error.__class__.__name__,
            "error_message": str(error),
            "action": "error"
        }
        
        self.logger.error("Event processing failed", extra={"extra_data": extra_data}, exc_info=True)
    
    def _get_user_id(self, event: TelegramObject) -> int | None:
        """Получение ID пользователя из события"""
        if hasattr(event, 'from_user') and event.from_user:
            return event.from_user.id
        elif hasattr(event, 'user') and event.user:
            return event.user.id
        return None
    
    def _get_chat_id(self, event: TelegramObject) -> int | None:
        """Получение ID чата из события"""
        if hasattr(event, 'chat') and event.chat:
            return event.chat.id
        elif hasattr(event, 'message') and event.message and event.message.chat:
            return event.message.chat.id
        return None
    
    def _get_chat_type(self, event: TelegramObject) -> str | None:
        """Получение типа чата из события"""
        if hasattr(event, 'chat') and event.chat:
            chat_type = event.chat.type
            if hasattr(chat_type, 'value'):
                return chat_type.value
            return str(chat_type)
        elif hasattr(event, 'message') and event.message and event.message.chat:
            chat_type = event.message.chat.type
            if hasattr(chat_type, 'value'):
                return chat_type.value
            return str(chat_type)
        return None


def setup_logging(level: str = "INFO") -> None:
    """Настройка системы логирования"""
    # Создаем форматтер
    formatter = StructuredFormatter()
    
    # Настраиваем корневой логгер
    root_logger = logging.getLogger()
    root_logger.setLevel(getattr(logging, level.upper()))
    
    # Очищаем существующие хендлеры
    for handler in root_logger.handlers[:]:
        root_logger.removeHandler(handler)
    
    # Создаем консольный хендлер
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)
    root_logger.addHandler(console_handler)
    
    # Создаем файловый хендлер для логов
    try:
        file_handler = logging.FileHandler("bot.log", encoding="utf-8")
        file_handler.setFormatter(formatter)
        root_logger.addHandler(file_handler)
    except Exception as e:
        root_logger.warning(f"Failed to create file handler: {e}")
    
    # Устанавливаем уровень для сторонних библиотек
    logging.getLogger("aiogram").setLevel(logging.WARNING)
    logging.getLogger("aiohttp").setLevel(logging.WARNING)
