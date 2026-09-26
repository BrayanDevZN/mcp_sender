"""
Inicia todo server kafka e o consumer
"""

from src.app.server.broker import kafkaClient
from src.app.server.topic import Topic
from src.app.server.consumer import Consumer
from src.service import sender_task

class KafkaServer:
    def __init__(self)-> None:

        #inicia o broker
        self.client = kafkaClient().run()

    #Cria o topic
    def _topic(self) -> None:

        instance = Topic(client=self.client)
        instance.run()

    #Cria o consumer
    def _create_consumer(self) -> None:

        instance = Consumer()
        self.consumer = instance.run()
        
    #Roda o consumer
    async def _consumer(self) -> None:

        while True:
            poll = self.consumer.poll(timeout_ms=3000)
            

            for _, consumer in poll.items():

                for message in consumer:

                    try:

                        args = message.value
                        await sender_task(**args)
                      
                        self.consumer.commit()

                    except Exception:

                        self.consumer.commit()


    #Executa todos os metodos
    async def run(self) -> None:

        self._topic()
        self._create_consumer()
        await self._consumer()





    


