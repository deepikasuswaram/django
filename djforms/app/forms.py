from django import forms


g=[('MALE','male'),('FEMALE','female')]
c=[('python','python'),['django','django'],('sql','sql')]

def validate_for_char(data):
    if not data[0].isalpha():
        raise forms.ValidationError('error')
    
def validate_for_len(value):
    if len(value)<5:
        raise forms.ValidationError('error')



class StudentForm(forms.Form):
    sname=forms.CharField(validators=[validate_for_char,validate_for_len])
    sid=forms.IntegerField()
    semail=forms.EmailField(validators=[validate_for_char])
    remail=forms.EmailField()
    def clean(self):
        s=self.cleaned_data['semail']
        r=self.cleaned_data['remail']
        if s!=r:
            raise forms.ValidationError('error')




    #surl=forms.URLField()
    #spassword=forms.CharField(widget=forms.PasswordInput)
    #saddress=forms.CharField(widget=forms.Textarea)
    #gender=forms.ChoiceField(choices=g)
    #gender=forms.ChoiceField(choices=g,widget=forms.RadioSelect)

