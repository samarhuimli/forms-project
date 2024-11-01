from django import forms
from django.forms import ModelForm

from .models import Contact  


class contactform2(forms.Form):
    firstname=forms.CharField(max_length=10)
    lastname=forms.CharField(max_length=10)
    email = forms.EmailField()                    
    message = forms.CharField(widget=forms.Textarea)  
   
class contactForm3(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ('firstname', 'lastname', 'email', 'message') 