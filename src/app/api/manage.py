"""
cria a instancia da api
"""
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from src.app.api.midlleware import Midlleware
from src.app.api.router import router
from src.service import ENVIRONMENTS
class InstanceApi:

    def __init__(self):
        self.app = FastAPI()


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

        self.app.include_router(router)


    #Executa os metodos e retorna instancia
    def run(self) -> FastAPI:
        self._midlleware()
        self._cors()
        self._router()
        return self.app 

    