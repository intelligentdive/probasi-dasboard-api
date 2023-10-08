# blog/urls.py

from django.urls import path
from . import views
from .views import PostViewSet
urlpatterns = [
    path('posts/', views.PostListCreateView.as_view(), name='post-list-create'),
    # path('posts/<int:pk>/', views.PostDetailView.as_view(), name='post-detail'),
    # path('posts/<int:pk>/comments/', views.CommentListCreateView.as_view(), name='comment-list-create'),
    # path('comments/<int:pk>/', views.CommentDetailView.as_view(), name='comment-detail'),
    path('posts/<int:pk>/like/', PostViewSet.as_view({'post': 'like_post'}), name='like-post'),
    path('posts/<int:pk>/dislike/', PostViewSet.as_view({'post': 'dislike_post'}), name='dislike-post'),
    path('all_posts/', views.AllPostsView.as_view(), name='all_posts_api'),


    path('posts/<int:post_id>/comment/', views.CommentCreateAPIView.as_view(), name='comment-create'),



    path('postscommentlist/<int:post_id>/', views.CommentView.as_view(), name='comment-create'),
]
