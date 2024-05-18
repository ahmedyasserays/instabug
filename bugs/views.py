from django.db import transaction
from django.db.models import Max
from rest_framework.exceptions import ValidationError
from rest_framework.generics import (
    CreateAPIView,
    RetrieveAPIView,
    get_object_or_404,
)

from .models import Bug
from .serializers import BugSerializer


class BugsCreateView(CreateAPIView):
    serializer_class = BugSerializer

    @transaction.atomic
    def perform_create(self, serializer):
        last_number = Bug.objects.filter(
            application_token=serializer.validated_data["application_token"]
        ).aggregate(last_number=Max("number", default=0))["last_number"]
        serializer.save(number=last_number + 1)


class BugsRetrieveView(RetrieveAPIView):
    serializer_class = BugSerializer

    def get_object(self):
        if not self.request.GET.get("application_token"):
            raise ValidationError(
                "Missing required query parameter: application_token"
            )
        return get_object_or_404(
            Bug.objects.all(),
            number=self.kwargs["number"],
            application_token=self.request.GET["application_token"],
        )
