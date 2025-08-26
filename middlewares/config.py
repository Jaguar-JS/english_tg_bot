import os
from typing import Dict, Any


class LoggingConfig:
    """Конфигурация для системы логирования"""
    
    # Уровни логирования
    DEFAULT_LEVEL = "INFO"
    BOT_LEVEL = "INFO"
    AIOGRAM_LEVEL = "WARNING"
    AIOHTTP_LEVEL = "WARNING"
    
    # Файлы логов
    LOG_FILE = "bot.log"
    ERROR_LOG_FILE = "bot_errors.log"
    
    # Форматы
    CONSOLE_FORMAT = "json"  # json или text
    FILE_FORMAT = "json"
    
    # Ротация логов
    MAX_FILE_SIZE = 10 * 1024 * 1024  # 10MB
    BACKUP_COUNT = 5
    
    # Фильтрация
    EXCLUDE_PATTERNS = [
        "password",
        "token",
        "secret"
    ]
    
    @classmethod
    def from_env(cls) -> 'LoggingConfig':
        """Создание конфигурации из переменных окружения"""
        config = cls()
        
        config.DEFAULT_LEVEL = os.getenv("LOG_LEVEL", config.DEFAULT_LEVEL)
        config.BOT_LEVEL = os.getenv("BOT_LOG_LEVEL", config.BOT_LEVEL)
        config.AIOGRAM_LEVEL = os.getenv("AIOGRAM_LOG_LEVEL", config.AIOGRAM_LEVEL)
        config.AIOHTTP_LEVEL = os.getenv("AIOHTTP_LOG_LEVEL", config.AIOHTTP_LEVEL)
        
        config.LOG_FILE = os.getenv("LOG_FILE", config.LOG_FILE)
        config.ERROR_LOG_FILE = os.getenv("ERROR_LOG_FILE", config.ERROR_LOG_FILE)
        
        return config
    
    def to_dict(self) -> Dict[str, Any]:
        """Преобразование в словарь для логирования"""
        return {
            "default_level": self.DEFAULT_LEVEL,
            "bot_level": self.BOT_LEVEL,
            "aiogram_level": self.AIOGRAM_LEVEL,
            "aiohttp_level": self.AIOHTTP_LEVEL,
            "log_file": self.LOG_FILE,
            "error_log_file": self.ERROR_LOG_FILE,
            "console_format": self.CONSOLE_FORMAT,
            "file_format": self.FILE_FORMAT
        }
