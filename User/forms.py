from django import forms
from django.forms import ModelForm, widgets
from .models import user, post

class SignupForm(ModelForm):
    class Meta:
        model = user
        fields = ('username', 'first_name', 'last_name', 'email', 'password')

        labels = {
            'username':'',
            'first_name':'',
            'last_name':'',
            'email':'',
            'password':''
        }


        widgets = {
            'username':forms.TextInput(attrs={'class':'form-control', 'name':'username', 'placeholder': 'Username'}),
            'first_name':forms.TextInput(attrs={'class':'form-control', 'name':'firstname', 'placeholder':'First Name'}),
            'last_name':forms.TextInput(attrs={'class':'form-control', 'name':'lastname', 'placeholder':'Last Name'}),
            'email':forms.widgets.EmailInput(attrs={'class':'form-control', 'name':'email', 'placeholder':'Email'}),
            'password':forms.widgets.PasswordInput(attrs={'class':'form-control', 'name':'password', 'placeholder':'Password'})
        }

class PostsForm(ModelForm):
    class Meta:
        model = post
        fields = ('user','texts', 'created_at', 'updated_at')

        labels = {
            'user':'',
            'texts':'',
            'created_at':'Created at',
            'updated_at':'Updated at',
        }


        widgets = {
            'texts':forms.TextInput(attrs={'class':'form-control', 'name':'text', 'placeholder':'Enter Your Text'}),
            'created_at':forms.DateInput(attrs={'type':"date",'class':'form-control', 'name':'created_at', 'placeholder':'Created at'}),
            'updated_at':forms.DateInput(attrs={'type':'date', 'class':'form-control', 'name':'updated_at', 'placeholder':'Updated at'})
        }