from django.shortcuts import render
from django.http import HttpResponse
from app.models import *

# Create your views here.


def insert_topic(request):
    if request.method=='POST':
        tn=request.POST['tn']

        TO=Topic.objects.get_or_create(topic_name=tn)
        return HttpResponse(f'{tn} Topic is created')

    return render(request,'insert_topic.html')


def insert_webpage(request):
    LTO=Topic.objects.all()
    d={'LTO':LTO}

    if request.method=='POST':
        tn=request.POST['tn']
        na=request.POST['na']
        ur=request.POST['ur']
        em=request.POST['em']

        TO=Topic.objects.get(topic_name=tn)

        WO=Webpage.objects.get_or_create(topic_name=TO,name=na,url=ur,email=em)

        return HttpResponse('WEBPAGE IS CREATED SUCCESFULLY')


    return render(request,'insert_webpage.html',d)


def insert_access(request):
    LWO=Webpage.objects.all()
    d={'LWO':LWO}

    if request.method=='POST':
        na=request.POST['na']
        au=request.POST['au']
        da=request.POST['da']

        WO=Webpage.objects.get(id=na)

        AO=AccessRecord.objects.get_or_create(name=WO,author=au,date=da)

        return HttpResponse('accessRecord IS inserted SUCCESFULLY')


    return render(request,'insert_access.html',d)


def select_multiple(request):
    LTO=Topic.objects.all()
    d={'LTO':LTO}

    if request.method=='POST':
        MTN=request.POST.getlist('tn')
        EQST=Webpage.objects.none()

        for topic in MTN:
            EQST=EQST|Webpage.objects.filter(topic_name=topic)

        d1={'EQST':EQST}
        return render(request,'display_webpage.html',d1)

    return render(request,'select_multiple.html',d)