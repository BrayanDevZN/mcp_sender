"""
Inicia a api
"""
from src.app.api.manage import InstanceApi
instance = InstanceApi()
app = instance.run()





"""
Inicia o consumer
"""
if __name__ == "__main__":
    import sys 

    if len(sys.argv) == 2:
        arg = sys.argv[1]

        if arg == "init_consumer":

            from src.app.server.manage import KafkaServer
            instance = KafkaServer()

            import asyncio

            asyncio.run(instance.run())

        else:

            raise ValueError(f"Not expeted arg {arg}")

        



