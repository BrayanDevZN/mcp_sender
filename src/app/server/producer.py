from src.logs.log import logger

"""
producer de sender
"""
import uuid
from kafka import KafkaProducer
import json
class Producer:
    def __init__(self, email:str, subject:str, body:str) -> None:

        self.prod = KafkaProducer(
            bootstrap_servers="kafka:19092",
            key_serializer=lambda key: str(key).encode("utf-8"),
            value_serializer=lambda value: str(json.dumps(value)).encode("utf-8"),
            enable_idempotence=True,
            acks="all"
        )

        self.key = str(uuid.uuid4())
        self.body = {
            "email": email, 
            "subject": subject,
            "body": body
        }

    #Envia
    async def send(self) -> str:

        try:

            logger.info("Enviando dados para consumer...")

            self.prod.send(
                key=self.key,
                value=self.body,
                topic="emails"    
            )

            logger.info("Enviado com sucesso!!")

            return self.key 

        except Exception as e:
            logger.error(f"Houve um erro ao enviar: {e}")
            raise Exception(e)

        



    


        

