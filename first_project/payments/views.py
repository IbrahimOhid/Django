from django.shortcuts import render
from django.http.response import HttpResponse

# Create your views here.
def bkash(request):
    return render(request, 'payment/payment1.html')

def rocket(request):
    return render(request, 'payment/payment2.html')

