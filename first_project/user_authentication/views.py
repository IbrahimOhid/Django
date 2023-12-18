from django.shortcuts import render
from django.http.response import HttpResponse

# Create your views here.
def code(request):
    return render(request, 'user_authentication/user.html')
