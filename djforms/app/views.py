from django.shortcuts import render
from django.http import HttpResponse
from app.forms import *
# Create your views here.

def studform(request):
    ESFO=StudentForm()
    d={'ESFO':ESFO}
    if request.method=='POST':
        SFDO=StudentForm(request.POST)
        if SFDO.is_valid():
            return HttpResponse(str(SFDO.cleaned_data))
        else:
            return HttpResponse('Invalid data')
    
    
    return render(request,'studform.html',d)
