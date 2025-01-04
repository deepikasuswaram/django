from django.shortcuts import render

# Create your views here.
def college(request):
    return render(request,'college.html')