"""
Midlleware que confere rate limit
"""


from starlette.middleware.base import BaseHTTPMiddleware
from src.cache.manage import redis_control
from src.service import ENVIRONMENTS
from fastapi import HTTPException, Request
class Midlleware(BaseHTTPMiddleware):

    async def dispatch(self, request:Request, call_next):

        global_limit = int(ENVIRONMENTS["global_rate_limit"])

        global_rate_limit = await redis_control.get("global_rate_limit") 
       

        if global_rate_limit is not None and int(global_rate_limit) > global_limit:

            raise HTTPException(
                status_code=429,
                detail=f"Exceded global rate limit"
            )

        await redis_control.incr("global_rate_limit")


        limit = int(ENVIRONMENTS["rate_limit"])
        name = f"rate_limit:{request.client.host}"
        rate_limit = await redis_control.get(name=name)
    
        if rate_limit is not None and int(rate_limit)>limit:

            raise HTTPException(
                status_code=429,
                detail=f"Exceded rate limit for {request.client.host}"
            )

        await redis_control.incr(name=name)


        return await call_next(request)
        
        


       