# authentication/urls.py
from django.urls import path
from .views import email_signup_view, phone_signup_view

urlpatterns = [
    path('email-signup/', email_signup_view, name='email-signup'),
    path('phone-signup/', phone_signup_view, name='phone-signup'),
]
