from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from app.forms import *
from app.models import *

def insert_topic(request):
    ESTO=TopicForm()
    d={'ESTO':ESTO}
    if request.method=='POST':
        DSTO=TopicForm(request.POST)
        if DSTO.is_valid():
            tn=request.POST['tn']
            TO=Topic.objects.get_or_create(topic_name=tn)

            return HttpResponse('Topic is inserted')
        else:
            return HttpResponse('Invalid Data')

    return render(request,'insert_topic.html',d)

def insert_webpage(request):
    ESWO=WebpageForm()
    d={'ESWO':ESWO}
    if request.method=='POST':
        DSWO=WebpageForm(request.POST)
        if DSWO.is_valid():
            tn=request.POST['tn']
            na=request.POST['name']
            ur=request.POST['url']
            em=request.POST['email']

            TO=Topic.objects.get(topic_name=tn)

            WO=Webpage.objects.get_or_create(topic_name=TO,name=na,url=ur,email=em)

            return HttpResponse('WEBPAGE IS CREATED SUCCESFULLY')
        else:
            return HttpResponse('Invalid Data')


    return render(request,'insert_webpage.html',d)


def insert_access(request):
    ESAO=AccessForm()
    d={'ESAO':ESAO}
    if request.method=='POST':
        DSAO=AccessForm(request.POST)
        if DSAO.is_valid():
            na=request.POST['name']
            au=request.POST['author']
            da=request.POST['date']

            WO=Webpage.objects.get(id=na)

            AO=AccessRecord.objects.get_or_create(name=WO,author=au,date=da)
            return HttpResponse('ACCESS RECORD IS INSERTED SUCCESFULLY')
        else:
            return HttpResponse('Invalid Data')

    return render(request,'insert_access.html',d)

def wish(request,name):
    return HttpResponse(f'<h1>Hello {name}, How Are You</h1>')