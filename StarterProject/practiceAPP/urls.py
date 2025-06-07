from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:img_id>/', views.img_detail, name='img_detail'),
]
