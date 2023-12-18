from django.shortcuts import render
from django.http.response import HttpResponse

# Create your views here.
def list(request):
    return render(request, 'listing_details/listing.html')