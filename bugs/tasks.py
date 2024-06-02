from celery import shared_task
from django.db import transaction

from .serializers import BugSerializer


@shared_task
def save_bug(data):
    with transaction.atomic:
        BugSerializer(data=data).save(number=data["number"])
