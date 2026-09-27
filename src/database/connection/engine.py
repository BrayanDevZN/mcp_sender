from src.logs.log import logger

"""
Cria engine do banco de dados
"""
from sqlalchemy.ext.asyncio import create_async_engine, AsyncEngine
from sqlalchemy import text
class Engine:

    def __init__(self, url:str)-> None:

        self.url = url 


    #Cria a engine
    def _engine(self) -> None:

        try:

            logger.info("Criando engine do banco de dados...")

            self.engine = create_async_engine(url=self.url)

            logger.info("Criada com sucesso!!")

        except Exception as e:

            logger.error(e)
            raise Exception(e)

    #Executa o teste
    async def _test(self) -> None:

        countdown = 0

        while True:

            try:

                logger.info("Testando engine...")


                async with self.engine.begin() as session:

                    session.execute(text("select 1"))

                logger.info("Engine ok!!")
                break

            except Exception as error:

                if countdown !=3:

                    logger.warning("Houve um erro na engine, executando teste novamente...")
                    countdown+=1
                    continue

                msg = f"Houve um erro com a engine: {error}"
                logger.error(msg)
                raise Exception(msg)

    #Executa os metodos e retorna engine
    async def run(self) -> AsyncEngine:

        self._engine()
        await self._test()
        return self.engine

                

                


        