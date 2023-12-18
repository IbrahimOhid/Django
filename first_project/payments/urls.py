from django.urls import path
from . import views


urlpatterns = [
    path('bkash/', views.bkash),
    path('rocket/', views.rocket)
]
