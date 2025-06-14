from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from . import views

urlpatterns = [
    path('', views.PostsList, name='PostsList'),
    path('create/', views.PostCreate, name='PostCreate'),
    path('<int:post_id>/edit/', views.Post_edit, name='PostEdit'),
    path('<int:post_id>/delete/', views.Post_delete, name='PostDelete'),
]
