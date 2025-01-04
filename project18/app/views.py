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

    '''
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
    
def insert_access(request):
    id=input('enter id')
    a=input('enter author ')
    d=input('enter date ')
    WO=Webpage.objects.filter(id=id)
    if WO:
        WOL=WO[0]
        AO=AccessRecord.objects.get_or_create(name=WOL,author=a,date=d)
        return HttpResponse('AccessRecord object is created')
    else:
        return HttpResponse('not available')
    
def display_topics(request):
    QST=Topic.objects.all()
    d={'topics':QST}
    return render(request,'display_topics.html',d)

def display_webpages(request):
    QSW=Webpage.objects.all()

    QSW=Webpage.objects.filter(name__startswith='v')
    d={'webpages':QSW}
    return render(request,'display_webpages.html',d)

def update_webpages(request):
    #where name abcd changing email to abcd@gmail.com
    Webpage.objects.filter(name='abcd').update(email='abcd@gmail.com')

    #where tn boxing changing url to https://boxing.in
    Webpage.objects.filter(topic_name='Boxing').update(url='https://boxing.in')

    #zero rows satisfying
    Webpage.objects.filter(name='deepika').update(email='deepika@gmail.com')

    Webpage.objects.filter(pk=5).update(topic_name='FootBall')

    Webpage.objects.update_or_create(name='Rohit',defaults={'name':'Virat'})

    Webpage.objects.update_or_create(name='Rohit',defaults={'name':'Virat'})




    webpages=Webpage.objects.all()
    d={'webpages':webpages}
    return render(request,'update_webpages.html',d)

def display_access(request):
    QSA=AccessRecord.objects.all()
    QSA=AccessRecord.objects.filter(date__year='2025')


    d={'access':QSA}

    return render(request,'display_access.html',d)



