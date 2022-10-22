from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import Group,User
from django.contrib.auth import authenticate, login,logout
from django.views import View
from .form import RegisterForm,LoginForm
from .models import Profile

class UserProfile(View):
    def get(self,request,*args,**kwargs):
        user = request.user
        profile = Profile.objects.get(user = user)
        return render(request,'user/profile.html',{'profile':profile})

class UserLogin(View):
    def get(self,request,*args,**kwargs):
        frm = LoginForm()
        return render(request,'user/login.html',{'form':frm})
    def post(self,request,*args,**kwargs):
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password =form.cleaned_data['pasword']
            username = email.split('@')[0]+email.split('@')[1].split('.')[0]
            user = authenticate(request, username=username, password=password)
            print(username,password,user)
            if user is not None:
                login(request, user)
                return redirect('user_profile')
        return render(request,'user/login.html',{'form':form})

class UserRegister(View):
    def get(self,request,*args,**kwargs):
        frm = RegisterForm()
        return render(request,'user/register.html',{'form':frm})
    def post(self,request,*args,**kwargs):
        form = RegisterForm(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            username =email.split('@')[0]+email.split('@')[1].split('.')[0]
            user = User.objects.create_user(username=username,email=email,password=password)
            user.first_name = first_name
            user.last_name = last_name
            group = Group.objects.get(name='regular')
            user.groups.add(group)
            user.save()
            return redirect('user_login')
        return render(request,'user/register.html',{'form':form})

class UserLogout(View):
    def get(self,request,*args,**kwargs):
        logout(request)
        return redirect('user_login')
class UserEdit(View):
    def get(self,request,*args,**kwargs):
        pass
