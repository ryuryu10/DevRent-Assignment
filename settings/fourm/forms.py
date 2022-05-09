from pyexpat import model
from django import forms
from .models import fourms

class WRITE_Form(forms.ModelForm):
    class Meta:
        model = fourms
        fields = ['title','content']
        title = forms.CharField(max_length=50)
        content = forms.CharField()