from django.contrib import admin
from django.urls import path
from .import views

urlpatterns = [
    path('', views.login, name="login"),
    path('signup/', views.signup, name="signup"),
    path('check/', views.check, name="check"),
    path('posts/', views.posts, name="posts"),
    path('add_post/', views.add_post, name="add_post"),
    path('check_post/', views.check_post1, name="check_post"),
]