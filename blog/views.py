# blog/views.py

from rest_framework import generics
from django.shortcuts import get_object_or_404
from .models import Post, Comment

from .serializers import PostSerializer, CommentSerializer

class PostListCreateView(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class PostDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class CommentListCreateView(generics.ListCreateAPIView):
    serializer_class = CommentSerializer
    
    # permission_classes = [IsAuthenticated]

    queryset = Comment.objects.all()
    # def get_queryset(self):
    #     post_id = self.kwargs['pk']
    #     return Comment.objects.filter(post_id=post_id)
    # def perform_create(self, serializer):
    #     post_id = self.kwargs.get('post_id')
    #     post = get_object_or_404(Post, pk=post_id)
    #     serializer.save(author=self.request.user, post=post)
class CommentDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
