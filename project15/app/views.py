from django.shortcuts import render
from app.models import *
from django.http import HttpResponse
# Create your views here.



def insert_topic(request):
    tn=input('enter topic name ')
    TO=Topic.objects.get_or_create(topic_name=tn)
    if TO[1]:
        return HttpResponse('Topic object is created')
    else:
        return HttpResponse('The Topic Object already exists')
    

    '''

def insert_webpage(request):
    tn=input('enter topic name ')
    n=input('enter name')
    u=input('enter url ')
    e=input('enter mail-id ')
    TO=Topic.objects.get_or_create(topic_name=tn)[0]
    WO=Webpage.objects.get_or_create(topic_name=TO,name=n,url=u,email=e)
    if WO[1]:
        return HttpResponse('Webpage object is created')
    else:
        return HttpResponse('The Webpage Object already exists')
    
def insert_accessRecord(request):
    tn=input('enter topic name ')
    n=input('enter name')
    u=input('enter url ')
    e=input('enter mail-id ')
    a=input('enter author ')
    d=input('enter date ')
    TO=Topic.objects.get_or_create(topic_name=tn)[0]
    WO=Webpage.objects.get_or_create(topic_name=TO,name=n,url=u,email=e)[0]
    AO=AccessRecord.objects.get_or_create(name=WO,author=a,date=d)
    if AO[1]:
        return HttpResponse('AccessRecord object is created')
    else:
        return HttpResponse('The AccessRecord Object already exists')
    

def insert_webpage(request):
    tn=input('enter topic name ')
    n=input('enter name')
    u=input('enter url ')
    e=input('enter mail-id ')
    TO=Topic.objects.get(topic_name=tn)
    WO=Webpage.objects.get_or_create(topic_name=TO,name=n,url=u,email=e)[0]
    return HttpResponse('Webpage is created')

    
def insert_webpage(request):
    tn=input('enter topic name ')
    n=input('enter name')
    u=input('enter url ')
    e=input('enter mail-id ')
    QLTO=Topic.objects.filter(topic_name=tn)
    if QLTO:
        TO=QLTO[0]
        WO=Webpage.objects.get_or_create(topic_name=TO,name=n,url=u,email=e)
        return HttpResponse('Webpage object is created')
    else:
        return HttpResponse('webpage object already exists')

        '''


def display_topics(request):
    topics=Topic.objects.all()
    d={'topics':topics}
    return render(request,'display_topics.html',context=d)

def display_webpages(request):
    LWO=Webpage.objects.all()
    d={'LWO':LWO}
    return render(request,'display_webpages.html',d)