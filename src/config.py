"""
Le as variaveis de ambiente
"""

from pathlib import Path
from dotenv import load_dotenv
import os 


BASE_DIR = Path(__file__).resolve().parent.parent / ".env"
ENVIRONMENTS = {}
NAME_ENV = ["email", "password", "origin", "rate_limit", "global_rate_limit"]

class NotFoundEnv(Exception):
    pass 


load_dotenv() if not os.path.exists(BASE_DIR) else load_dotenv(BASE_DIR)

  
for name in NAME_ENV:

    env = os.getenv(name) 
    if env is None:

        raise NotFoundEnv(f"Expeted env {name}")

    ENVIRONMENTS[name] = env 


