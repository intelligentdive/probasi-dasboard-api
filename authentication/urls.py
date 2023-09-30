# authentication/urls.py
from django.urls import path
from .views import email_signup_view, phone_signup_view, LoginView
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
urlpatterns = [
    path('email-signup/', email_signup_view, name='email-signup'),
    path('phone-signup/', phone_signup_view, name='phone-signup'),
    path('login/', LoginView.as_view(), name='login'),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
