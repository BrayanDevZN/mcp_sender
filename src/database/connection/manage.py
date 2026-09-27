"""junta os modulos de conexão"""


from src.database.connection.engine import Engine
from src.database.connection.session import session
from pathlib import Path
import asyncio 

class MakeConnect:

    def __init__(self, url:str|None = None)-> None:

        self.url = url
        asyncio.run(self._run())

    #Define qual url usar se ela for none
    def _url(self) -> None:

        if self.url is None:

            BASE_DIR = Path(__file__).resolve().resolve().parent.parent

            path = BASE_DIR / "storage/sender.db"

            self.url = f"asyncpg+sqlite:///{path}"

    #Cria a engine
    async def _engine(self) -> None:

        instance = Engine(url=self.url)

        self.engine = await instance.run()

    #Cria a session
    def _session(self) -> None:

        self.session = session(engine=self.engine)

    #executa os metodos
    async def _run(self) -> None:

        self._url()
        await self._engine()
        self._session()

        
        