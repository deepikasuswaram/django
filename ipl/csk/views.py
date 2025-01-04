from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def msd(request):
    return HttpResponse('<h1><marquee>MSD IS THE BEST INDIAN WICKET KEEPER AND BATSMAN</marquee></h1>')

def raina(request):
    return render(request,'raina.html')