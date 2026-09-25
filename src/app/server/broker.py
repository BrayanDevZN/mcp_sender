from src.logs.log import logger

"""
Cria a conexão com servidor kafka
"""



from kafka.admin import KafkaAdminClient


class kafkaClient:

    def __init__(self)-> None:

        logger.info("Criando conexão com servidor kafka...")

        self.bootstrap = KafkaAdminClient(bootstrap_servers="kafka:19092")

    def _test(self) -> None:

        countdown = 0

        while True:

            try:
                logger.info("Testando conexão...")

                self.bootstrap.describe_cluster()


                logger.info("Conexão ok!!!")
                break

            except Exception as e:

                if countdown !=3:

                    logger.warning("Houve um erro na conexão, o teste sera executado novamente!!!")
                    countdown +=1
                    continue

                logger.error(f"Houve um erro na conexão: {e}")
                raise

    #Executa o teste e retorna conexão
    def run(self) -> KafkaAdminClient:
        self._test()
        return self.bootstrap


                




    

    

    
        