from src.logs.log import logger

"""
Envia email pro usuario
"""

import yagmail

class Sender:

    def __init__(self, email:str, password:str)->None:

        self.isntance = yagmail.SMTP(
            user=email,
            password=password
        )


    def send(self,email:str, subject:str, body:str) -> None:

        logger.info(f"Enviando email para {email}...")

        self.isntance.send(
            to=email,
            subject=subject,
            contents=body
        )

        logger.info("Email enviado com sucesso!!!")


        




        