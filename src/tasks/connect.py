from src.logs.log import logger

"""
Cria a conexão com celery
"""

from celery import Celery

def celery_connect() -> Celery:

    countdown = 0

    while True:

        try:

            logger.info("Criando conexão com celery...")

            celery = Celery(
                broker="redis://redis-worker:6379/0",
                backend="redis://redis-worker:6379/1"
            )

            logger.info("Conexão Criada com sucesso")

            return celery

        except Exception as error:

            if countdown!=3:
                logger.warning("Houve um erro ao conectar, tentando conectar novamente...")
                countdown+=1
                continue

            msg = f"Houve um erro ao se conectar: {error}"
            logger.error(msg)
            raise Exception(msg)

            