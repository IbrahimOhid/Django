from django.urls import path
from . import views


urlpatterns = [
    path('', views.name),
    path('learn/', views.learn)
]
