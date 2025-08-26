import time
import logging
from typing import Any, Dict
from aiogram import BaseMiddleware
from aiogram.types import TelegramObject


class PerformanceMiddleware(BaseMiddleware):
    """Middleware для мониторинга производительности"""
    
    def __init__(self, logger_name: str = "performance"):
        super().__init__()
        self.logger = logging.getLogger(logger_name)
    
    async def __call__(
        self,
        handler: callable,
        event: TelegramObject,
        data: Dict[str, Any]
    ) -> Any:
        start_time = time.time()
        
        try:
            result = await handler(event, data)
            execution_time = time.time() - start_time
            
            # Логируем время выполнения
            extra_data = {
                "event_type": event.__class__.__name__,
                "execution_time_ms": round(execution_time * 1000, 2),
                "handler": handler.__name__,
                "action": "performance"
            }
            
            if execution_time > 1.0:  # Предупреждение для медленных обработчиков
                self.logger.warning("Slow handler execution", extra={"extra_data": extra_data})
            else:
                self.logger.info("Handler executed", extra={"extra_data": extra_data})
            
            return result
            
        except Exception as e:
            execution_time = time.time() - start_time
            extra_data = {
                "event_type": event.__class__.__name__,
                "execution_time_ms": round(execution_time * 1000, 2),
                "handler": handler.__name__,
                "error": str(e),
                "action": "performance_error"
            }
            
            self.logger.error("Handler failed", extra={"extra_data": extra_data})
            raise
