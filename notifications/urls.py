from django.urls import path
from .views import (
    PushNotificationView
)

urlpatterns = [
    path('push', PushNotificationView.as_view(), name='push-notification')
]
