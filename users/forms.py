from typing import Any
from django import forms
from.models import User

class LoginForm(forms.Form):
    username=forms.CharField(required=True,widget=forms.TextInput(attrs={"class":"form-control"}))
    password=forms.CharField(required=True,widget=forms.PasswordInput(attrs={"class":"form-control"}))

class RegisterForm(forms.Form):
    first_name=forms.CharField(required=True, widget=forms.TextInput(attrs={"class":"form-control"}))
    last_name=forms.CharField(required=True, widget=forms.TextInput(attrs={"class":"form-control"}))
    username=forms.CharField(required=True, widget=forms.TextInput(attrs={"class":"form-control"}))
    email=forms.CharField(required=True, widget=forms.EmailInput(attrs={"class":"form-control"}))
    # photo=forms.ImageField(required=True, widget=forms.Filein(attrs={"class":"form-control"}))
    password=forms.CharField(required=True, widget=forms.PasswordInput(attrs={"class":"form-control"}))
    confirm_password=forms.CharField(required=True, widget=forms.PasswordInput(attrs={"class":"form-control"}))

    def clean_login(self) :
        password=self.cleaned_data.get('password',None)
        confirm_password=self.cleaned_data.get('confirm_password',None)

        if password:
            if confirm_password!=password:
                raise forms.ValidationError("passwordlar ikkixil")
            
            return self.cleaned_data

    # def clean_first_name(self) : 
    #     first_name=self.cleaned_data.get('first_name',None)
    #     if len(first_name)<5:

    #          raise forms.ValidationError("Ismingiz juda uzun ekan")




    #     return self.cleaned_data
    







 

class ProfileForm(forms.ModelForm):
    # password=forms.CharField(required=False,disabled=True, widget=forms.PasswordInput(attrs={"class":"form-control"}))
    
    first_name=forms.CharField(required=True, widget=forms.TextInput(attrs={"class":"form-control"}))
    username=forms.CharField(required=True, widget=forms.TextInput(attrs={"class":"form-control"}))
    # last_name=forms.CharField(required=True, widget=forms.TextInput(attrs={"class":"form-control"}))
    
    # bio=forms.CharField(required=True, widget=forms.TextInput(attrs={"class":"form-control"}))
    # phone_number=forms.CharField(required=True, widget=forms.NumberInput(attrs={"class":"form-control"}))
    photo=forms.ImageField(required=True, widget=forms.FileInput(attrs={"class":"form-control"}))


    class Meta:
        model=User
        fields=('username','first_name','photo')