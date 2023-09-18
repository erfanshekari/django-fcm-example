import logging
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework.status import (
    HTTP_400_BAD_REQUEST
)
from firebase_admin.messaging import (
    MulticastMessage, 
    send_multicast,
    BatchResponse,
    Notification
)
from .serializers import PushNotificationSerializer

class PushNotificationView(GenericAPIView):
    serializer_class = PushNotificationSerializer

    def post(self, request) -> Response:
        serializer = self.serializer_class(
            data=request.data, 
            context=self.get_serializer_context()
        )
        if serializer.is_valid():
            try:
                notification = serializer.validated_data.get('notification', None)
                reseponse: BatchResponse = send_multicast(
                    MulticastMessage(
                        tokens=serializer.validated_data['tokens'],
                        data=serializer.validated_data.get('data', None),
                        notification=Notification(
                            title=notification.get('title', None),
                            body=notification.get('body', None),
                            image=notification.get('image', None),
                        ) if notification else None
                    )
                )
                return Response(
                    data={
                        'success_count': reseponse.success_count,
                        'failure_count': reseponse.failure_count,
                    }
                )
            except Exception as exc:
                logging.debug(exc)
                return Response(
                    status=HTTP_400_BAD_REQUEST,
                    data={
                        'error': str(exc)
                    }
                )
        else:
            return Response(
                status=HTTP_400_BAD_REQUEST,
                data=serializer.errors
            )