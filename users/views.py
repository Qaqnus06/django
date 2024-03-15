from typing import Any
from django.db.models.base import Model as Model
from django.db.models.query import QuerySet
from django.shortcuts import render
from django.contrib.auth import authenticate,login,logout
from .forms import LoginForm,RegisterForm,ProfileForm
from django .http import HttpResponse,HttpResponseRedirect
from.models import User
from django.views.generic import UpdateView
from django .urls import reverse_lazy,reverse
from django.shortcuts import render, HttpResponseRedirect, reverse
from django.contrib.auth import authenticate, login
from .forms import LoginForm
# Create your views here.
# def index(request):
#     return  render (request, 'users/index.html')


# def login_page(request):
#     form =None
#     if request.method == 'POST':
#         form = LoginForm(request.POST)
#         if form.is_valid():
#             username=form.cleaned_data['username']
#             password=form.cleaned_data['password']
#             # user=authenticate(request,username=username,password=password)
       
#             pass
 
#     return render(request, 'users/login_page.html', {'form': form})



def login_page(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')  # Use get() method for accessing cleaned_data
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return HttpResponseRedirect(reverse('product:index'))  # Fix reverse call

    else:  # Use else for GET requests to avoid unnecessary form instantiation
        form = LoginForm()

    data = {
        'form': form
    }        
    return render(request, 'users/login_page.html', context=data)

def logout_page(request):
    logout(request)

    return HttpResponseRedirect(reverse('login_page')) 

def register_page(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            try:
                user = User.objects.create_user(
                    username=form.cleaned_data['username'],
                    first_name=form.cleaned_data['first_name'],
                    last_name=form.cleaned_data['last_name'],
                    password=form.cleaned_data['password']
                )
                # You don't need to call user.save() when using create_user method
                return HttpResponseRedirect(reverse('login_page'))
            except :  # Catch specific exception to handle errors properly
                  # This will help you debug errors
                return HttpResponseRedirect(reverse('product:index'))  # Redirect to an appropriate page if user creation fails

    else:  # Use else for GET requests to avoid unnecessary form instantiation
        form = RegisterForm()

    data = {
        'form': form
    }

    return render(request, 'users/register_page.html', context=data)


# class ProfileView(UpdateView):
#     form_class=ProfileForm
#     model=User

#     template_name='users/profile.html'
    

#     def get_object(self, queryset=None):
#         return self.request.user
        
#     def get_success_url(self):
#         return reverse_lazy('product:index')    
def profile_page(request):


    form=ProfileForm()


    data={

        'form':form
    }        
    return render(request,'users/profile_page.html',context=data)        
