from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def virat(request):
    return HttpResponse('<h1>Virat is the KING OF CRICKET</h1>')

def abd(request):
    return render(request,'abd.html')