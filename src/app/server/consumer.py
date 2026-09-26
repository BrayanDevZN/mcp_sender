from src.logs.log import logger

"""
Cria o consumer
"""

from kafka import KafkaConsumer
import json

class Consumer:

    #Cria o consumer
    def _consumer(self) -> None:

        try:

            logger.info("Criando consumer...")
            self.consumer = KafkaConsumer(
                "emails",
                bootstrap_servers="kafka:19092",
                enable_auto_commit=False,
                group_id="sender",
                auto_offset_reset="earliest",
                key_deserializer=lambda key: key.decode("utf-8"),
                value_deserializer=lambda body:json.loads(body.decode("utf-8"))
            )

            logger.info("Criando com sucesso!!!")

        except Exception as e:

            logger.error(e)
            raise Exception(e)

    #Executa o metodo e retorna o pool
    def run(self) -> KafkaConsumer:

        self._consumer()
        return self.consumer
    


        

