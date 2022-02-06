from django import forms

class loginform(forms.ModelForm):
    username =forms.CharField(max_length=30)
    password =forms.PasswordInput()
    