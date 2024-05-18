from django.db import models


# Create your models here.
class State(models.Model):
    device = models.CharField(max_length=250)
    os = models.CharField(max_length=250)
    memory = models.PositiveBigIntegerField()
    storage = models.PositiveBigIntegerField()


class Bug(models.Model):

    class StatusChoices(models.TextChoices):
        new = "n", "New"
        inprogress = "i", "In-progress"
        closed = "c", "Closed"

    class PriorityChoices(models.IntegerChoices):
        minor = 1, "Minor"
        major = 2, "Major"
        critical = 3, "Critical"

    application_token = models.CharField(max_length=250)
    number = models.PositiveBigIntegerField()
    status = models.CharField(max_length=1, choices=StatusChoices.choices)
    priority = models.CharField(max_length=1, choices=PriorityChoices.choices)
    comment = models.TextField()
    state = models.OneToOneField(State, on_delete=models.PROTECT)

    class Meta:
        unique_together = ("application_token", "number")
        indexes = [
            models.Index(fields=["application_token", "number"]),
        ]
