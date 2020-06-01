from django.urls import path
from .views import *

urlpatterns = [
    path('login/', login, name='login'),
    path('images/<str:username>/', images, name='images'),
    path('videos/<str:username>/', videos, name='videos'),
]