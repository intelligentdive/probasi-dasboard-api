# blog/models.py

from django.db import models
from user.models import User







class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    is_published = models.BooleanField(default=False)
    anonymous = models.BooleanField(default=False)
    likes = models.ManyToManyField(User, related_name='liked_posts', blank=True)
    dislikes = models.ManyToManyField(User, related_name='disliked_posts', blank=True)
   # comments = models.ManyToManyField(Comment, related_name='disliked_posts', blank=True)
    like_count = models.PositiveIntegerField(default=0,blank= True,null= True )  # Field to store the like count
    dislike_count = models.PositiveIntegerField(default=0,blank= True,null= True) 
    comment_count = models.PositiveIntegerField(default=0) 
    image = models.ImageField(upload_to='post_images/',blank= True,null= True) 
    def __str__(self):
        return self.title
    def update_like_dislike_counts(self):
        self.like_count = self.likes.count()
        self.dislike_count = self.dislikes.count()
        self.save()

    def get_user_has_liked(self, post):
        request = self.context.get('request')
        if request and request.user.is_authenticated:
            return post.likes.filter(pk=request.user.pk).exists()
        return False    


     


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    text = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comment by {self.post} at {self.created_at}"       

