from django.shortcuts import render

# Create your views here.
d={'a':10,'b':20,'c':30}
def conditions(request):
    return render(request,'conditions.html',d)

D={'name':'deepika','mobile':'8978455071'}
def loops(request):
    return render(request,'loops.html',D)