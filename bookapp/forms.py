from django import forms
from django.forms import ModelForm
from .models import Book
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
# class BookCreateForm(forms.Form):
#     book_name=forms.CharField()
#     author=forms.CharField()
#     pages=forms.IntegerField()
#     price=forms.IntegerField()
class BookCreateForm(ModelForm):
    class Meta:
        model=Book
        fields="__all__"
    def clean(self):
        print("validation here")

class UserRegistrationForm(UserCreationForm):
    class meta:
        model=User
        fields=["username","password1","password2","email"]

class LoginForm(forms.Form):
    username=forms.CharField()
    password=forms.CharField()