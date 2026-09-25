"""
junta os modulos
"""

from src.cache.connect import RedisConnect
from src.cache.control import RedisControl
from redis import Redis


client = RedisConnect().run()
redis_control = RedisControl(client=client)