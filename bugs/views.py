from django.db.models import Max
from rest_framework.exceptions import ValidationError
from rest_framework.generics import (
    CreateAPIView,
    RetrieveAPIView,
    get_object_or_404,
)

from .models import Bug
from .serializers import BugSerializer
from .tasks import save_bug
from .redis import RedisBugStore


class BugsCreateView(CreateAPIView):
    serializer_class = BugSerializer

    def perform_create(self, serializer):
        application_token = serializer.validated_data["application_token"]
        bug_store = RedisBugStore(application_token)
        with bug_store:
            last_number = bug_store.get_last_number()
            if last_number == 0:
                last_number = Bug.objects.filter(
                    application_token=application_token
                ).aggregate(last_number=Max("number", default=0))[
                    "last_number"
                ]
            data = serializer.validated_data
            data["number"] = last_number + 1
            bug_store.update_last_number(data["number"])
            save_bug.delay(data)


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
