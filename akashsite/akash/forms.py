from django import forms
from .models import akash
 
 
class akashForm(forms.ModelForm):
    class Meta:
        model = akash
        fields = "__all__"
