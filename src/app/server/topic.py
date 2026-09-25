from src.logs.log import logger

"""
Cria o topic de envio
"""

from kafka.admin import NewTopic, KafkaAdminClient

class Topic:

    def __init__(self, client:KafkaAdminClient)-> None:

        self.client = client 


    #objeto do topic
    def _topic(self) -> None:

        self.name = "emails"

        self.topic = NewTopic(
            name=self.name,
            num_partitions=5,
            replication_factor=1
        )


    #Confere se o topic ja existe
    def _exists(self) -> None:

        logger.info("Conferindo se o topic ja existe...")


        self.exists = self.name in self.client.list_topics()

    #Cria o topic
    def _create(self) -> None:

        if not self.exists:

            try:
                logger.info(f"Criando topic {self.name}...")

        
                self.client.create_topics([self.topic])

                logger.info("Criado com sucesso!!!")

            except Exception as e:
                logger.error(e)
                raise Exception(e)


    #Executa todos os metodos
    def run(self) -> None:

        self._topic()
        self._exists()
        self._create()