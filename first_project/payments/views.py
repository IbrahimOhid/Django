from django.shortcuts import render
from django.http.response import HttpResponse

# Create your views here.
def bkash(request):
    payment_method = 'Bkash'
    discount = '80%'
    condition = 'Only First Payment'
    payment_info = {'pm': payment_method, 'dis': discount, 'con': condition}
    return render(request, 'payment/payment1.html', payment_info)

def rocket(request):
    return render(request, 'payment/payment2.html')

