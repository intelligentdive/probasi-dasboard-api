from rest_framework import permissions
from rest_framework import generics
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from .models import Post, Comment
from user.models import User
import jwt, datetime
from rest_framework.authentication import TokenAuthentication
from .serializers import PostSerializer, CommentSerializer,PostSerializer1
from rest_framework.exceptions import AuthenticationFailed
from rest_framework import views, response, exceptions, permissions
from rest_framework.exceptions import AuthenticationFailed, NotFound 
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from django.http import JsonResponse
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import AuthenticationFailed
from .models import User
from rest_framework import viewsets
from rest_framework.generics import CreateAPIView

from rest_framework.decorators import action

class PostListCreateView(views.APIView):
    
    def post(self, request):
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

        # You should import and use your profile serializer here
        serializer =  PostSerializer1(data=request.data)
        if serializer.is_valid():
            # Create a new profile for the authenticated user
            serializer.save(user=user1)
           
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) 
    

        # return Response(serializer.data)      



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
    








class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    @action(detail=True, methods=['post'])
    def like_post(self, request, pk):
        post = self.get_object()
        authorization_header = request.headers.get('Authorization')

        if not authorization_header or not authorization_header.startswith('Bearer '):
            raise AuthenticationFailed('Invalid or missing Bearer token!')

        token = authorization_header.split('Bearer ')[1]

        if not token:
            raise AuthenticationFailed('Invalid or missing token!')

        try:
            # Make sure to use the same secret key that was used to encode the JWT
            payload = jwt.decode(token, 'secret', algorithms=['HS256'])
        except jwt.ExpiredSignatureError:
            raise AuthenticationFailed('JWT has expired!')
        except jwt.DecodeError:
            raise AuthenticationFailed('JWT is invalid!')

        user = User.objects.filter(id=payload['id']).first()
        if user not in post.likes.all():
            post.likes.add(user)
            post.dislikes.remove(user)  # Remove user from dislikes if they have disliked before
            post.update_like_dislike_counts()
            return Response({'message': 'Post liked'}, status=status.HTTP_200_OK)
        return Response({'message': 'Post already liked'}, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=True, methods=['post'])
    def dislike_post(self, request, pk):
        post = self.get_object()
        authorization_header = request.headers.get('Authorization')

        if not authorization_header or not authorization_header.startswith('Bearer '):
            raise AuthenticationFailed('Invalid or missing Bearer token!')

        token = authorization_header.split('Bearer ')[1]

        if not token:
            raise AuthenticationFailed('Invalid or missing token!')

        try:
            # Make sure to use the same secret key that was used to encode the JWT
            payload = jwt.decode(token, 'secret', algorithms=['HS256'])
        except jwt.ExpiredSignatureError:
            raise AuthenticationFailed('JWT has expired!')
        except jwt.DecodeError:
            raise AuthenticationFailed('JWT is invalid!')

        user = User.objects.filter(id=payload['id']).first()
        if user not in post.dislikes.all():
            post.dislikes.add(user)
            post.likes.remove(user)  # Remove user from likes if they have liked before
            post.update_like_dislike_counts()
            return Response({'message': 'Post disliked'}, status=status.HTTP_200_OK)
        return Response({'message': 'Post already disliked'}, status=status.HTTP_400_BAD_REQUEST)   
    


class AllPostsView(generics.ListAPIView):
    serializer_class = PostSerializer

    def get(self, request):
        # Retrieve the JWT token from the Authorization header
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

        user = User.objects.filter(id=payload['id']).first()

        if not user:
            raise AuthenticationFailed('User not found!')

        # You might want to retrieve all posts for the user instead of just one profile
        posts = Post.objects.filter()

        # You should import and use your profile serializer here
        serializer = PostSerializer(
            posts,
            many=True,
            context={'request_user': user}  # Pass the user to the serializer context
        )

        return Response(serializer.data)
 

 



class CommentCreateAPIView(APIView):
    def post(self, request, post_id):
        authorization_header = request.headers.get('Authorization')

        if not authorization_header or not authorization_header.startswith('Bearer '):
            raise AuthenticationFailed('Invalid or missing Bearer token!')

        token = authorization_header.split('Bearer ')[1]

        try:
            # Make sure to use the same secret key that was used to encode the JWT
            payload = jwt.decode(token, 'secret', algorithms=['HS256'])
        except jwt.DecodeError:
            raise AuthenticationFailed('Invalid token!')

        # Assuming you're using JWT for authentication
        user = User.objects.filter(id=payload['id']).first()

        # Ensure that the post with the specified ID exists, or handle accordingly
        try:
            post = Post.objects.get(id=post_id)
            post.comment_count = post.comment_count + 1
            post.save()
        except Post.DoesNotExist:
            raise NotFound("Post not found")

        # Create the comment
        comment_text = request.data.get('text')
        comment = Comment(post=post, text=comment_text, user=user)
        comment.save()

        return JsonResponse({"message": "Comment created successfully."})
    


class CommentView(APIView):
    def get(self, request, post_id):
        try:
            post = Post.objects.get(id=post_id)
        except Post.DoesNotExist:
            raise NotFound("Post not found")

        comments = Comment.objects.filter(post=post)
        serializer = CommentSerializer(comments, many=True)

        return Response(serializer.data)
