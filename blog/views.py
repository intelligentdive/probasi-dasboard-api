from rest_framework import permissions
from rest_framework import generics
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from .models import Post, Comment
from user.models import User
import jwt, datetime
from rest_framework.authentication import TokenAuthentication
from .serializers import PostSerializer, CommentSerializer
from rest_framework.exceptions import AuthenticationFailed
from rest_framework import views, response, exceptions, permissions

from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView

from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import AuthenticationFailed
from .models import User



class PostListCreateView(generics.ListCreateAPIView):
    # serializer_class = PostSerializer
    def get(self, request):
        authorization_header = request.headers.get('Authorization')
        if not authorization_header or not authorization_header.startswith('Bearer '):
            raise AuthenticationFailed('Invalid or missing Bearer token!')

        token = authorization_header.split('Bearer ')[1].strip()  # Strip whitespaces

        try:
            # Make sure to use the same secret key that was used to encode the JWT
            payload = jwt.decode(token, 'secret', algorithms=['HS256'])
        except jwt.ExpiredSignatureError:
            raise AuthenticationFailed('JWT has expired!')
        except jwt.DecodeError:
            raise AuthenticationFailed('JWT is invalid!')

        user1 = User.objects.filter(id=payload['id']).first()

        if not user1:
            raise AuthenticationFailed('User not found!')

        # profile = Post.objects.filter(user=user).first()

        
        # You should import and use your profile serializer here
        serializer =  PostSerializer(data=request.data)
        if serializer.is_valid():
            # Create a new profile for the authenticated user
            serializer.save(user=user1)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) 
    

        return Response(serializer.data)      



class PostDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    def get(self, request):
        authorization_header = request.headers.get('Authorization')
        if not authorization_header or not authorization_header.startswith('Bearer '):
            raise AuthenticationFailed('Invalid or missing Bearer token!')

        token = authorization_header.split('Bearer ')[1].strip()  # Strip whitespaces

        try:
            # Make sure to use the same secret key that was used to encode the JWT
            payload = jwt.decode(token, 'secret', algorithms=['HS256'])
        except jwt.ExpiredSignatureError:
            raise AuthenticationFailed('JWT has expired!')
        except jwt.DecodeError:
            raise AuthenticationFailed('JWT is invalid!')

        user = Post.objects.filter(id=payload['id']).first()

        if not user:
            raise AuthenticationFailed('User not found!')

        profile = Post.objects.filter(user=user).first()

        if not profile:
            raise AuthenticationFailed('Profile not found!')

        # You should import and use your profile serializer here
        serializer =  PostSerializer(profile)

        return Response(serializer.data)      



class CommentListCreateView(generics.ListCreateAPIView):
    serializer_class = CommentSerializer
    def get(self, request):
        authorization_header = request.headers.get('Authorization')
        if not authorization_header or not authorization_header.startswith('Bearer '):
            raise AuthenticationFailed('Invalid or missing Bearer token!')

        token = authorization_header.split('Bearer ')[1].strip()  # Strip whitespaces

        try:
            # Make sure to use the same secret key that was used to encode the JWT
            payload = jwt.decode(token, 'secret', algorithms=['HS256'])
        except jwt.ExpiredSignatureError:
            raise AuthenticationFailed('JWT has expired!')
        except jwt.DecodeError:
            raise AuthenticationFailed('JWT is invalid!')

        user = Comment.objects.filter(id=payload['id']).first()

        if not user:
            raise AuthenticationFailed('User not found!')

        profile = Comment.objects.filter(user=user).first()

        if not profile:
            raise AuthenticationFailed('Profile not found!')

        # You should import and use your profile serializer here
        serializer =  CommentSerializer(profile)

        return Response(serializer.data)      



class CommentDetailView(generics.RetrieveUpdateDestroyAPIView):
    # queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    def get(self, request):
        authorization_header = request.headers.get('Authorization')
        if not authorization_header or not authorization_header.startswith('Bearer '):
            raise AuthenticationFailed('Invalid or missing Bearer token!')

        token = authorization_header.split('Bearer ')[1].strip()  # Strip whitespaces

        try:
            # Make sure to use the same secret key that was used to encode the JWT
            payload = jwt.decode(token, 'secret', algorithms=['HS256'])
        except jwt.ExpiredSignatureError:
            raise AuthenticationFailed('JWT has expired!')
        except jwt.DecodeError:
            raise AuthenticationFailed('JWT is invalid!')

        user = Comment.objects.filter(id=payload['id']).first()

        if not user:
            raise AuthenticationFailed('User not found!')

        profile = Comment.objects.filter(user=user).first()

        if not profile:
            raise AuthenticationFailed('Profile not found!')

        # You should import and use your profile serializer here
        serializer =  CommentSerializer(profile)

        return Response(serializer.data)      
