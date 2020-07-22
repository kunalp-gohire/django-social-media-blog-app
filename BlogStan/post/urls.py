from django.contrib.auth import views as auth_views
from django.urls import path, include
from . import views

app_name = 'posts'
urlpatterns = [
    path('', views.PostList.as_view(), name='all'),
    path('new/', views.CreatePost.as_view(), name='create'),
    path('by/<username>', views.UserPosts.as_view(), name='for_user'),
    path('by/<username>/<int:pk>/', views.PostDetail.as_view(), name='single'),
    path('delete/<int:pk>', views.DeletePost.as_view(), name='delete'),
    path('comment/add/<int:pk>', views.add_comment_to_post,
         name='add_comment'),
    path('comment/<int:pk>/remove/',
         views.comment_remove,
         name='remove_comment'),
]
