from dataclasses import fields
from django import forms
from django.contrib.auth.models import User
class RegisterForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        kwargs["label_suffix"] = ""
        super().__init__(*args, **kwargs)
    class Meta:
        model = User
        fields = ['first_name','last_name','email','password']
        # fields = '__all__'
        widgets = {
            'first_name': forms.TextInput(attrs={'placeholder': 'Enter your first name'}),
            'last_name': forms.TextInput(attrs={'placeholder': 'Enter your Last name'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Enter your Email'}),
            'password':forms.PasswordInput(attrs={'placeholder': 'Enter your Password'}),
        }
        labels = {
            'first_name':'First Name',
            'last_name': 'Last Name',
            'email': 'Email',
            'password':'password',
        }
    


class LoginForm(forms.Form):
    email = forms.EmailField(label='Email',widget=forms.EmailInput(attrs={'placeholder': 'Enter your Email'}))
    pasword = forms.CharField(max_length=50,label='Password',widget=forms.PasswordInput(attrs={'placeholder': 'Enter your Password'}))
    def __init__(self, *args, **kwargs):
        kwargs["label_suffix"] = ""
        super().__init__(*args, **kwargs)