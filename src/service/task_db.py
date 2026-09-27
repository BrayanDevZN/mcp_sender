"""
tasks das operações do banco de dados
"""

from src.service.db.control import control_db
from src.tasks.manage import celery_app
import asyncio
@celery_app.task
def insert_dlq(session_id:str, status:bool, content:str) -> None:

    asyncio.run(control_db.dlq.insert(session_id=session_id, status=status, content=content))


@celery_app.task
def delete_dlq(session_id:str) -> None:

    asyncio.run(control_db.dlq.delete(session_id=session_id))
