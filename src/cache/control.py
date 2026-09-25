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


        