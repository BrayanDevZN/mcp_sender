"""
facilita importação
"""
from src.database.connection.manage import MakeConnect
from src.database.repository.dlq import DlqRepository
from src.database.migrate import make_migrate
import asyncio

