from .models import commnetsModel
from django import forms
class commentsForm(forms.ModelForm):
    car=None
    class Meta:
        model=commnetsModel
        exclude=['car',]
        widget={
            'body':forms.Textarea()
        }
    
