from src.logs.log import logger

"""
Cria conexão com redis
"""

from redis import Redis 

class RedisConnect:

    def __init__(self)-> None:

        self.host = "redis"
        self.port = 6379

    #Cria conexão
    def _con(self) -> None:

        logger.info("Criando conexão com redis...")

        self.con = Redis(
            host=self.host,
            port=self.port,
            decode_responses=True
        )

        logger.info("Conexão criada com sucesso!!")

    #Testa conexão
    def _test(self) -> None:
        countdown = 0
        while True:

            try:

                logger.info("Testando conexão com redis...")

                self.con.ping()

                logger.info("Conexão ok!!!")
                break

            except Exception as e:

                if countdown !=3:
                    logger.warning("Houve um erro ao tentar conectar com redis, tentando conectar de novo...")
                    countdown +=1
                    continue

                msg = f"Houve um erro ao conectar com redis: {e}"
                logger.error(msg)
                raise Exception(msg)

    #Executa os metodos e retorna o objeto redis
    def run(self) -> Redis:
        self._con()
        self._test()
        return self.con

            


        