from django.shortcuts import render

# Create your views here.
def example(request):
    return render(request,'example.html')

def home(request):
    return render(request,'home.html')


def forms(request):
    return render(request,'forms.html')