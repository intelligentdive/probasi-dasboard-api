from django.shortcuts import render

# Create your views here.
# authentication/views.py
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import status
from authentication.models import CustomUser
from .serializers import EmailSignUpSerializer, PhoneSignUpSerializer

@api_view(['POST'])
@permission_classes([AllowAny])
def email_signup_view(request):
    if request.method == 'POST':
        serializer = EmailSignUpSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
@permission_classes([AllowAny])
def phone_signup_view(request):
    if request.method == 'POST':
        serializer = PhoneSignUpSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
