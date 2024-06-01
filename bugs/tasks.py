from celery import shared_task
from django.db import transaction

from .serializers import BugSerializer


@shared_task
@transaction.atomic
def save_bug(data):
    BugSerializer(data=data).save(number=data["number"])
