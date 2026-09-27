from src.logs.log import logger


"""
Contra a tabela dlq
"""

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, delete
from src.database.models.dlq import Dlq

class DlqRepository:

    def __init__(self, session:AsyncSession)-> None:

        self.session = session

    #Cria a linha
    async def insert(self, session_id:str, status:bool, content:str) -> dict:

        try:

            logger.info("Salvando resultado do evento...")

            async with self.session.begin() as session:

                instance = Dlq(
                    session_id=session_id,
                    status=status,
                    content=content
                )

                await session.add(instance)

                session.flush()
            logger.info("Salvo com sucesso!!!")

            result = {
                "id":instance.id,
                "session_id": instance.session_id,
                "status": instance.status,
                "content": instance.content,
                "created_at": str(instance.created_at)
            }
            return result

        except Exception as error:

            msg = f"Houve um error ao salvar: {error}"
            logger.error(msg)
            raise Exception(msg)

    #seleciona todos resultados
    async def select_all(self) -> None|dict:

        try:

            logger.info("buscando eventos...")

            async with self.session.begin() as session:

                result = select(Dlq)
                if result is None:
                    logger.info("Ainda não ha dados!!")
                    return None

                result = await session.execute(result).scalars().all()
                if not result:
                    logger.info("Ainda não ha dados!!")
                    return None

            logger.info("Lido com sucesso!!")

            result = {
                "id": [Id for Id in result.id],
                "session_id": [session_id for session_id in result.session_id],
                "status": [status for status in result.status],
                "content": [content for content in result.content],
                "created_at": [str(created_at) for created_at in result.created_at]
            }
            return result
        except Exception as error:
            msg = f"Houve um erro ao ler: {error}"
            logger.error(msg)
            raise Exception(msg)

    #Busca um usuario por session id
    async def select(self, session_id:str) -> None|dict:

        try:

            logger.info("Buscando eventos...")

            async with self.session.begin() as session:

                query = select(Dlq).where(Dlq.session_id == session_id)
                instance = await session.execute(query).one()

                if instance is None:

                    logger.info("Evento não encontrado!!")
                    return None 

            logger.info("Evento encontrado!!")


            result = {
                "id":instance.id,
                "session_id": instance.session_id,
                "status": instance.status,
                "content": instance.content,
                "created_at": str(instance.created_at)
            }

            return result

        except Exception as error:
            msg = f"Houve um erro ao ler: {error}"
            logger.error(msg)
            raise Exception(msg)

    #Deleta evento
    async def delete(self, session_id:str) -> None:

        try:

            logger.info("Deletando evento...")

            async with self.session.begin() as session:

                query = delete(Dlq).where(Dlq.session_id == session_id)

                await session.execute(query)

            logger.info("Deletado!!")

        except Exception as error:

            msg = f"Erro ao deletar: {error}"
            logger.error(msg)
            raise Exception(msg)





    
        