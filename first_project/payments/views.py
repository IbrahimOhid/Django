from django.shortcuts import render
from django.http.response import HttpResponse

# Create your views here.
def name(request):
    return render(request, 'payment.html')

