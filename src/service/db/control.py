"""
Junta todos os modulos
"""
from src.service.db.dlq import ControlDlq

class ControlDb:

    def __init__(self)->None:

        self.dlq = ControlDlq()


control_db = ControlDb()
        