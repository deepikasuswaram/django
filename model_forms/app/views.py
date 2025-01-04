from django.shortcuts import render
from app.models import *
from app.forms import *

from django.http import HttpResponse
def insert_topic(request):
    ETFO=TopicForm()
    d={'ETFO':ETFO}
    if request.method=="POST":
        DTFO=TopicForm(request.POST)
        if DTFO.is_valid():
            DTFO.save()
            return HttpResponse('one record inserted')
        else:
            return HttpResponse('invalid data')
    return render(request,'insert_topic.html',d)

def insert_webpage(request):
    EWFO=WebpageForm()
    d={'EWFO':EWFO}
    if request.method=="POST":
        DWFO=WebpageForm(request.POST)
        if DWFO.is_valid():
            DWFO.save()
            return HttpResponse('one record inserted')
        else:
            return HttpResponse('invalid data')
    return render(request,'insert_webpage.html',d)

def insert_access(request):
    EAFO=AccessForm()
    d={'EAFO':EAFO}
    if request.method=="POST":
        DAFO=AccessForm(request.POST)
        if DAFO.is_valid():
            DAFO.save()
            return HttpResponse('one record inserted')
        else:
            return HttpResponse('invalid data')
    return render(request,'insert_access.html',d)