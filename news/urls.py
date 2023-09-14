from django.urls import path
from . import views
from .views import *

urlpatterns = [
    path('', index, name='home'),
    path('posts/', posts, name='posts'),
    path('<int:pk>', views.NewsDetailView.as_view(), name='news-detail'),
]