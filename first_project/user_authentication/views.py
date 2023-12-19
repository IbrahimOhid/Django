from django.shortcuts import render
from django.http.response import HttpResponse
from datetime import datetime

# Create your views here.
def code(request):
    name = 'Mohammad Ibrahim'
    cgpa = 3.05
    institute = 'Chittagong Polytechnic Institute'
    all_info = {'na': name, 'mark': cgpa, 'ins': institute}
    return render(request, 'user_authentication/user.html', all_info)

def date(request):
    da = datetime.now()
    return render(request, 'user_authentication/date.html', {'d': da} )

def  student(request):
    name = {'students': ['ibrahim', 'ohid', 'ebnol', 'osman', 'mohammad']}
    return render(request, 'user_authentication/studentInfo.html', name)
