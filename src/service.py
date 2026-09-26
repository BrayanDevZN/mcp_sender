from src.logs.log import logger

"""
junta os modulos e facilita importação
"""

from src.config import ENVIRONMENTS
from src.sender import Sender
from src.tasks.manage import celery_app

@celery_app.task
def sender(email:str, subject:str, body:str) -> None:

    countdown = 0

    while True:

        try:

            instance = Sender(email=ENVIRONMENTS["email"], password=ENVIRONMENTS["password"])

            instance.send(
                email=email,
                subject=subject,
                body=body
            )

            break 

        except Exception as e:

            if countdown!=3:
                logger.warning("Houve um erro ao tentar enviar email, tentando enviar novamente...")
                countdown+=1
                continue

            msg = f"Houve um erro ao tentar enviar email: {e}"
            logger.error(e)
            raise Exception(msg)


async def sender_task(email:str, subject:str, body:str) -> None:

    try:
        logger.info("Criando task...")

        args = locals()
        sender.delay(**args)

        logger.info("Criada com sucesso!!!")

    except Exception as e:

        logger.error(e)
        raise Exception(e)

        