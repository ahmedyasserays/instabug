import logging
from celery import shared_task
from django.db import transaction
from .redis import LastNumberStore
from .serializers import BugSerializer

logger = logging.getLogger()


@shared_task
def save_bug(data):
    try:
        with transaction.atomic():
            ser = BugSerializer(data=data)
            ser.is_valid(raise_exception=True)
            ser.save(number=data["number"])
    except Exception as e:
        logger.error(f"got error {e}")
        logger.error(f"couldn't save bug from data: {data}")
        store = LastNumberStore(data["application_token"])
        with store:
            store.update_last_number(0)
        raise e
