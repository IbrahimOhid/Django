from django.urls import path
from . import views


urlpatterns = [
    path('bkash/', views.bkash, name='bkash'),
    path('rocket/', views.rocket, name='rocket')
]
