# blog/serializers.py

from rest_framework import serializers
from .models import Post, Comment
from user.serializer import UserSerializer
class CommentSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    class Meta:
        model = Comment
        fields = '__all__'

class PostSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    user_has_liked = serializers.SerializerMethodField()
    user_has_disliked = serializers.SerializerMethodField()

    class Meta:
        model = Post
        exclude = ['likes', 'dislikes']

    def get_user_has_liked(self, post):
        request_user = self.context.get('request_user')
        if request_user:
            # Check if the request_user has liked the post
            return post.likes.filter(pk=request_user.pk).exists()
        return False 

    def get_user_has_disliked(self, post):
        request_user = self.context.get('request_user')
        if request_user:
            # Check if the request_user has disliked the post
            return post.dislikes.filter(pk=request_user.pk).exists()
        return False



class PostSerializer1(serializers.ModelSerializer):
    
    

    class Meta:
        model = Post
        exclude = ['likes', 'dislikes']

    
