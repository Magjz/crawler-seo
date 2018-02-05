# from django.db import models
# from django import forms
# from django.contrib.auth.models import User
# from django.contrib.auth.forms import UserCreationForm
# from django.contrib.auth import get_user_model

# User = get_user_model()

# class RegisterForm(UserCreationForm):
#     email = forms.EmailField(label='Email', required=True)
#     firstname = forms.CharField(label='Firstname')
#     lastname = forms.CharField(label='Lastname')

#     class Meta:
#         model = User
#         fields = ("username", "firstname", "lastname", "email")
#         field_classes = {
#             'form-control' : forms.EmailField, 
#             'form-control' : forms.CharField, 
            
#         }

# class ProfileForm(forms.ModelForm): 
#     class Meta: 
#         model = User
#         fields = ("username", "firstname", "lastname", "email")
       
