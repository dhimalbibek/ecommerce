from django import forms
from shop.models import product

class createform(forms.ModelForm):
    class Meta:
        model = product
        fields = '__all__'
        # exclude = ['title']
    
