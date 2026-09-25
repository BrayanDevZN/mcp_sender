"""
rota de sender
"""

from fastapi import APIRouter, HTTPException
from src.app.api.schema import ValidSender
from fastapi.responses import JSONResponse
from src.app.server.producer import Producer
router = APIRouter(prefix="/sender", tags=["sender"])

"rota de enviar emais"
@router.post("/")
async def sender(sender_user:ValidSender) -> JSONResponse:

    try:

        instance = Producer(
            email=sender_user.email,
            subject=sender_user.subject,
            body=sender_user.body
        )


        result = await instance.send()

        return JSONResponse(status_code=201,
                            content={"status": True, "id":result})

    except Exception as e:

        raise HTTPException(
            detail=e,
            status_code=501
        )