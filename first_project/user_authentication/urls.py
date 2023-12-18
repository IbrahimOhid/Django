from  django.urls import path
from . import views

urlpatterns = [
    path('code/', views.code),
    path('date/', views.date)
]
