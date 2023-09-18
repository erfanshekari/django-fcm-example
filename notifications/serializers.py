from rest_framework.serializers import (
    ListField,
    CharField,
    Serializer,
    JSONField,
    URLField
)

class NotificationSerializer(Serializer):
    title = CharField()
    body = CharField()
    image = URLField()

class PushNotificationSerializer(Serializer):
    tokens = ListField(child=CharField(), required=True)
    data = JSONField(required=False, allow_null=True)
    notification = NotificationSerializer(allow_null=True, required=False)