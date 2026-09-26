"""
inicia o worker
"""

from src.tasks.connect import celery_connect
celery_app = celery_connect()
celery_app.autodiscover_tasks(["src.service"])