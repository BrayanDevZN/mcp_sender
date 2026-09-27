from src.logs.log import logger

"""
Cria as tabelas
"""

from sqlalchemy.ext.asyncio import AsyncEngine
from src.database.base import Base
from src.database.models.dlq import Dlq

async def make_migrate(engine:AsyncEngine) -> None:

    try:

        logger.info("Criando tabelas se não existirem...")

        async with engine.begin() as session:

            await session.run_sync(Base.metadata.create_all)

        logger.info("Criadas com sucesso!!")

    except Exception as error:

        msg = f"Houve um erro ao criar: {error}"
        logger.error(msg)
        raise Exception(msg)