"""
junta os modulos de service
"""
from src.service.db.control import ControlDb
from src.service.sender import sender_task, ENVIRONMENTS
from src.service.task_db import insert_dlq, delete_dlq
