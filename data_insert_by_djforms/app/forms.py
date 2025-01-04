from django import forms
from app.models import *
class TopicForm(forms.Form):
    tn=forms.CharField()

class WebpageForm(forms.Form):
    tn=forms.ModelChoiceField(queryset=Topic.objects.all())
    name=forms.CharField()
    url=forms.URLField()
    email=forms.EmailField()
    
class AccessForm(forms.Form):
    name=forms.ModelChoiceField(queryset=Webpage.objects.all())
    author=forms.CharField()
    date=forms.DateField()