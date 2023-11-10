from django.urls import path
from .views import my_view,showFirebaseJS

urlpatterns = [
    # path('save_fcm_token/', save_fcm_token, name='save_fcm_token'),
    # path('send_notification/<int:target_user_id>/', send_notification, name='send_notification'),
    # Add other URLs as needed

    path('my/', my_view, name='my_view'),
     path('firebase-messaging-sw.js',showFirebaseJS,name="show_firebase_js"),
]