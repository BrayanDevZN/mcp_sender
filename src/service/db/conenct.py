"""
junta os modulos de conexão com a url
"""

from src.database.module import MakeConnect
from src.config import ENVIRONMENTS
instance = MakeConnect(url=ENVIRONMENTS["url"])
session = instance.session
engine = instance.engine