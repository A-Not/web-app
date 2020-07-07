from django.urls import path
from . import views
from django.conf.urls import include
from rest_framework import routers


urlpatterns = [
    path('video/', views.PostView.as_view(), name='posts_list'),
    path('live/', views.LiveView.as_view(), name='posts_list'),
    path('terminate/', views.TerminateView.as_view(), name='posts_list'),
    path('image/', views.ImageDetectionView.as_view(), name='posts_list')


]
