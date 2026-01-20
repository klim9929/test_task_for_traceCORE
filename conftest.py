import logging
from logging.handlers import RotatingFileHandler
import os
from datetime import datetime

"""Здесь происходит настройка логгера и можно хранить глобальные фикстуры"""

log_dir = "logs"
if not os.path.exists(log_dir):
    os.makedirs(log_dir)

log_file_path = os.path.join(log_dir, f"test_run_{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.log")

formatter = logging.Formatter(
    fmt="%(asctime)s | %(levelname)-8s | %(name)s | %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S"
)

root_logger = logging.getLogger()
root_logger.setLevel(logging.INFO)
root_logger.handlers.clear()

file_handler = RotatingFileHandler(log_file_path, maxBytes=10*1024*1024, backupCount=3, encoding="utf-8")
file_handler.setFormatter(formatter)
root_logger.addHandler(file_handler)

console_handler = logging.StreamHandler()
console_handler.setFormatter(formatter)
root_logger.addHandler(console_handler)

