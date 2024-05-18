from rest_framework import serializers
from .models import Bug, State


class StateSerializer(serializers.ModelSerializer):
    class Meta:
        model = State
        fields = "__all__"


class BugSerializer(serializers.ModelSerializer):
    state = StateSerializer()
    number = serializers.IntegerField(read_only=True)
    extra_kwargs = {
        "number": {"read_only": True}
    }

    class Meta:
        model = Bug
        fields = "__all__"

    def create(self, validated_data):
        state_data = validated_data.pop("state")
        state = State.objects.create(**state_data)
        validated_data["state_id"] = state.id
        return super().create(validated_data)
