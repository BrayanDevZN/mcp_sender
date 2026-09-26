"""
Configuração global de logs
"""


import logging
import sys
from pathlib import Path
BASE_DIR = Path(__file__).resolve().parent / "app.log"

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(name)s | %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
    handlers=[
        # Terminal
        logging.StreamHandler(sys.stdout),

        # Arquivo
        logging.FileHandler(
            BASE_DIR,
            encoding="utf-8"
        )
    ]
)

logger = logging.getLogger(__name__)