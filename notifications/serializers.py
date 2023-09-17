from rest_framework.serializers import (
    ListField,
    CharField,
    Serializer,
    JSONField
)

class PushNotificationSerializer(Serializer):
    tokens = ListField(child=CharField())
    payload = JSONField()