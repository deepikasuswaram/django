from django import forms
from app.models import *

class TopicForm(forms.ModelForm):
    class Meta:
        model=Topic
        fields='__all__'

class WebpageForm(forms.ModelForm):
    class Meta:
        model=Webpage
        fields='__all__'
        #fields=['topic_name','name']
        #exclude=['email']
        #labels={'topic_name':'TN'}
        #widgets={'url':forms.PasswordInput}
        #help_texts={'topic_name':'this is parent column'}



class AccessForm(forms.ModelForm):
    class Meta:
        model=AccessRecord
        fields='__all__'

        