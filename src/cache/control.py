from src.logs.log import logger

"""
le e salva no redis
"""

from redis import Redis, WatchError

class RedisControl:
    def __init__(self, client:Redis)-> None:

        self.client = client


    #incrementa
    async def incr(self, name:str) -> None:

        while True:

            logger.info(f"Incrementando {name}...")

            try:

                with self.client.pipeline(transaction=True) as session:

                    session.watch(name)
                    session.multi()
                    session.incr(name)
                    session.expire(name=name, time=60)
                    session.execute()
                    logger.info(f"{name} incrementado com sucesso!!")
                    break 

            except WatchError:

                logger.warning(f"Alguem estava alterando {name}")

                continue

    #Le 
    async def get(self, name:str) -> int|None:

        try:

            logger.info(f"tentando ler {name}...")

            result = self.client.get(name)

            logger.info(f"{name} {"" if result is not None else "não"} existe!!")

            return result

        except Exception as e:

            logger.error(e)
            raise Exception(e)

    #Salva dicionario
    async def hash(self, name:str, data:dict) -> None:

        while True:

            try:

                logger.info(f"Salvando {name}...")

                with self.client.pipeline(transaction=True) as session:
                    session.watch(name)
                    session.multi()
                    session.hset(name=name, mapping=data)
                    session.expire(name=name, time=120)
                    session.execute()
                    logger.info(f"{name} salvado com sucesso!!")
                    break 

            except WatchError:

                logger.warning(f"Alguem ja estava alterando {name}, tentando de novo...")
                continue

    #Le hash
    async def hget(self, name:str) -> dict|None:

        while True:

            try:

                logger.info(f"lendo {name}...")
                with self.client.pipeline(transaction=True) as session:

                    session.watch(name)
                    session.multi() 
                    session.hgetall(name=name) 
                    result = session.execute()[0]
                    logger.info(f"{name} lida com sucesso!!")

                return result 

            except WatchError:

                logger.warning(f"Alguem ja estava alterando {name}, tentando de novo...")
                continue

    #Deleta
    async def delete(self, name:str) -> None:

        try:

            logger.info(f"Deletando {name}...")
            with self.client.pipeline() as session:

                session.delete(name=name)
                session.execute() 

                logger.info(f"{name} deletado com sucesso!!")
                return
        except Exception as error:
            msg = f"Houve um erro ao deletar: {error}"
            logger.error(msg)
            raise Exception(msg)

        









        