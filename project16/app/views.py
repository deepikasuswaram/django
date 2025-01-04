from django.shortcuts import render

from django.http import HttpResponse

from app.models import *


def insert_dept(request):
    dpn=input('enter deptno:')
    dna=input('enter dname:')
    loc=input('enter loc:')
    DO=Dept.objects.get_or_create(deptno=dpn,dname=dna,loc=loc)

    if DO[1]:
        return HttpResponse('one record is inserted into dept')
    else:
        return HttpResponse(' this record alredy exist')



def insert_emp(request):
    dn = input('deptno: ')
    eno = input('empno: ')
    en = input('ename: ')
    j = input('job: ')
    hd = input('hiredate: ')
    sal = input('sal: ')
    comm = input('comm: ')
    mg = input('enter mgrno (or leave blank for NULL): ')
    
    if comm=='':
        comm=None
    if mg=='':
        MGOL=None

    else:
        MGO=Emp.objects.filter(empno=mg) 
        if MGO:
            MGOL=MGO[0]
        else:
            return HttpResponse('MGR no is not available')

    DO=Dept.objects.filter(deptno=dn)
    if DO:
        DOL=DO[0]
        EO=Emp.objects.get_or_create(empno=eno,ename=en,job=j,hiredate=hd,sal=sal,comm=comm,mgr=MGOL,deptno=DOL)
        if EO:
            return HttpResponse('One record inserted succeffuly')
        else:
            return HttpResponse('already exists')
    else: 
        return HttpResponse('dept no is not avalible')




def display_data(request):
   depts_list=Dept.objects.all()
   emps=Emp.objects.all()
   #emps=Emp.objects.filter(ename__range=('a','k'))
   #emps=Emp.objects.filter(ename__startswith='a')
   #emps=Emp.objects.filter(ename__endswith='e')
   #emps=Emp.objects.filter(ename__startswith='a')
   emps=Emp.objects.all()
   return render(request,'test1.html',context={'depts_list':depts_list,'emps':emps})

def empdept(request):
   
    LEDO=Emp.objects.select_related('deptno').all()
    #LEDO=Emp.objects.select_related('deptno').filter(job='SALESMAN')
    #LEDO=Emp.objects.select_related('deptno').filter(comm__isnull=False)
    #LEDO=Emp.objects.select_related('deptno').filter(mgr__isnull=True)
    #LEDO=Emp.objects.select_related('deptno').filter(mgr__isnull=False,ename__startswith='j')
    #LEDO=Emp.objects.select_related('deptno').filter(deptno__dname='RESEARCH')
    #LEDO=Emp.objects.select_related('deptno').filter(deptno__loc='CHICAGO',sal__gt='1500')
    #LEDO=Emp.objects.select_related('deptno').filter(deptno__dname='SALES',job='MANAGER')
    from django.db.models import Avg,Max,F,Count
    #print(Emp.objects.all().aggregate(Avg('sal')))
    #print(Emp.objects.all().aggregate(avg__salary=Avg('sal')))
    #print(Emp.objects.values('deptno').annotate((Avg('sal'))))
    #print(Emp.objects.filter(deptno=30).aggregate(Avg('sal')))
    #D=Emp.objects.all().aggregate(Avg('sal'))
    #LEDO=Emp.objects.select_related('deptno').filter(sal__gt=D['sal__avg'])
    #LEDO=Emp.objects.select_related('deptno').filter(sal__lt=D['sal__avg'])
    #LEDO=Emp.objects.select_related('deptno').filter(sal__lte=D['sal__avg'])
    #print(Emp.objects.all().aggregate(Max('sal')))
    #DOMS=Emp.objects.all().aggregate(Max('sal'))
    #print(DOMS)
    #LEDO=Emp.objects.select_related('deptno').filter(sal__gte=DOMS['sal__max'])
    #LEDO=Emp.objects.select_related('deptno').filter(sal__lt=DOMS['sal__max'])
    #LEDO=Emp.objects.select_related('deptno').filter(sal__gt=DOMS['sal__max'])
    #LEDO=Emp.objects.select_related('deptno').annotate(annual_sal=F('sal')*12).values('ename','annual_sal')
    #print(Emp.objects.select_related('deptno').annotate(count=Count('empno')))
    LEDO=Emp.objects.select_related('deptno').order_by('-sal')[1:3]
    print(LEDO)
    d={'LEDO':LEDO}
    return render(request,'empdept.html',d)

def empmgr(request):
    LEMO=Emp.objects.select_related('mgr').all()
    LEMO=Emp.objects.select_related('mgr').filter(job='SALESMAN')
    LEMO=Emp.objects.select_related('mgr').filter(comm__isnull=True)
    LEMO=Emp.objects.select_related('mgr').filter(mgr__isnull=True)
    LEMO=Emp.objects.select_related('mgr').filter(mgr__isnull=False,ename__startswith='j')
    LEMO=Emp.objects.select_related('mgr').filter(mgr__sal__gt='2900')
    LEMO=Emp.objects.select_related('mgr').filter(mgr__job='ANALYST')

    d={'LEMO':LEMO}
    return render(request,'empmgr.html',d)

def empdeptmgr(request):
    LEDMO=Emp.objects.select_related('deptno','mgr').all()
    LEDMO=Emp.objects.select_related('deptno','mgr').filter(job='SALESMAN')
    LEDMO=Emp.objects.select_related('deptno','mgr').filter(comm__isnull=True)
    LEDMO=Emp.objects.select_related('deptno','mgr').filter(mgr__isnull=True)
    LEDMO=Emp.objects.select_related('deptno','mgr').filter(mgr__isnull=False,ename__startswith='j')
    LEDMO=Emp.objects.select_related('deptno','mgr').filter(mgr__sal__gt='2900')
    LEDMO=Emp.objects.select_related('deptno','mgr').filter(mgr__job='ANALYST')
    LEDMO=Emp.objects.select_related('deptno','mgr').filter(deptno__dname='RESEARCH')
    LEDMO=Emp.objects.select_related('deptno','mgr').filter(deptno__loc='CHICAGO',sal__gt='1500')
    LEDMO=Emp.objects.select_related('deptno','mgr').filter(deptno__dname='SALES',job='MANAGER')



    d={'LEDMO':LEDMO}
    return render(request,'empdeptmgr.html',d)

def deptemp(request):
    LDEO=Dept.objects.prefetch_related('emp_set').all()
    d={'LDEO':LDEO}
    return render(request,'deptemp.html',d)


def mgremp(request):
    LMEO=Emp.objects.prefetch_related('emp_set').all()
    d={'LMEO':LMEO}
    return render(request,'mgremp.html',d)
