"""
cria a instancia da api
"""
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from src.app.api.midlleware import Midlleware
from app.api.router.sender import sender_router
from src.service.module import ENVIRONMENTS
class InstanceApi:

    def __init__(self):
        self.app = FastAPI()
        self.routes = [sender_router]


    #Cria o midlleware
    def _midlleware(self) -> None:

        self.app.add_middleware(Midlleware)

    #Cria as configurações de cors
    def _cors(self) -> None:

        self.app.add_middleware(
            CORSMiddleware,
            allow_origins=[ENVIRONMENTS["origin"]],
            allow_headers=["*"],
            allow_methods=["*"],
            allow_credentials=False
        )

    #Adiciona rota
    def _router(self) -> None:

        for router in self.routes:
            self.app.include_router(router=router)


    #Executa os metodos e retorna instancia
    def run(self) -> FastAPI:
        self._midlleware()
        self._cors()
        self._router()
        return self.app 

    