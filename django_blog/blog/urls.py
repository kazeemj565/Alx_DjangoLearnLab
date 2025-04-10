# In blog/urls.py
from django.contrib.auth import views as auth_views
from django.urls import path
from . import views
from .views import (
    PostListView, PostDetailView, PostCreateView,
    PostUpdateView, PostDeleteView, PostByTagListView,
    CommentCreateView, CommentUpdateView, CommentDeleteView
)

urlpatterns = [
    path('register/', views.register, name='register'),
    path('profile/', views.profile, name='profile'),
    path('login/', auth_views.LoginView.as_view(template_name='blog/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='blog/logout.html'), name='logout'),
    path('', PostListView.as_view(), name='post-list'),
    path('posts/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('posts/<int:post_id>/comments/new/', views.add_comment, name='comment-add'),
    path('comment/<int:pk>/update/', views.edit_comment, name='comment-edit'),
    path('comments/<int:pk>/delete/', views.delete_comment, name='comment-delete'),
    path('post/<int:pk>/comments/new/', CommentCreateView.as_view(), name='comment-create'),
    path('comment/<int:pk>/update/', CommentUpdateView.as_view(), name='comment-update'),
    path('comment/<int:pk>/delete/', CommentDeleteView.as_view(), name='comment-delete'),
    path('search/', views.PostSearchView.as_view(), name='post-search'),
    path('tags/<str:tag_name>/', views.PostsByTagView.as_view(), name='posts-by-tag'),
    path('comment/<int:post_id>/add/', views.add_comment, name='comment-add'),
    path('tags/<slug:tag_slug>/', PostByTagListView.as_view(), name='posts-by-tag'),

    ]


