"""
junta db com cache
"""
from src.cache.manage import redis_control
from src.service.db.conenct import session
from src.database.module import DlqRepository

class ControlDlq:

    def __init__(self)-> None:

        self.db = DlqRepository(session=session)

    #Cria o evento e salva cache
    async def insert(self, session_id:str, status:bool, content:str) -> dict:

        result = await self.db.insert(session_id=session_id, status=status, content=content)

        await redis_control.hash(name=session_id, data=result)

        return result

    
    async def select_all(self) -> dict|None:

        name = "all-events"

        cache = await redis_control.hget(name=name)

        if cache is not None:

            return cache 

        result = await self.db.select_all()

        if result is not None:

            await redis_control.hash(name=name, data=result)

        return result


    async def select(self, session_id:str) -> dict|None:

        cache = await redis_control.hget(name=session_id)

        if cache is not None:
            return cache 

        result = await self.db.select(session_id=session_id)

        if result is not None:
            await redis_control.hash(name=session_id, data=result)

        return result


    async def delete(self, session_id:str) -> None:

        await self.db.delete(session_id=session_id)
        await redis_control.delete(name=session_id)


    
        

        