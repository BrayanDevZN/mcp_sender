from src.logs.log import logger

"""
Cria o orquestrador de engines
"""

from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, AsyncEngine

def session(engine:AsyncEngine) -> AsyncSession:

    try:

        logger.info("Criando orquestrador de engine...")

        session = async_sessionmaker(
            engine,
            expire_on_commit=False
        )
        logger.info("Criada com sucesso!!")

        
        return session

    except Exception as error:

        msg = f"Houve um erro ao criar: {error}"
        logger.error(msg)
        raise Exception(msg)



    