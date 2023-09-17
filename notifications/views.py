from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework.status import (
    HTTP_400_BAD_REQUEST
)
from firebase_admin.messaging import (
    MulticastMessage, 
    send_multicast
)
from django.utils.translation import gettext_lazy as _

from .serializers import PushNotificationSerializer

class PushNotificationView(GenericAPIView):
    serializer_class = PushNotificationSerializer

    def post(self, request) -> Response:
        serializer = self.serializer_class(
            data=request.data, 
            context=self.get_serializer_context()
        )
        if serializer.is_valid():
            print(serializer.validated_data)
            try:
                send_multicast(MulticastMessage(
                tokens=serializer.validated_data['tokens'],
                data=serializer.validated_data['payload']
            ))
            except Exception as exc:
                print(exc)
                return Response(
                    status=HTTP_400_BAD_REQUEST,
                    data={
                        'error': _('Unable to push notification!')
                    }
                )
            return Response()
        else:
            return Response(
                status=HTTP_400_BAD_REQUEST,
                data=serializer.errors
            )