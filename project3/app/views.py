from django.shortcuts import render

# Create your views here.
d={'name':'deepika','age':20}
def jinja_print(request):
    return render(request,'jinja_print.html',context=d)