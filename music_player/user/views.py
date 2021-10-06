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
        print(profile)
        return render(request,'profile.html',{'profile':profile})

class UserLogin(View):
    def get(self,request,*args,**kwargs):
        frm = LoginForm()
        return render(request,'login.html',{'form':frm})
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
                return redirect(to='/')
        return render(request,'login.html',{'form':form})

class UserRegister(View):
    def get(self,request,*args,**kwargs):
        frm = RegisterForm()
        return render(request,'register.html',{'form':frm})
    def post(self,request,*args,**kwargs):
        form = RegisterForm(request.POST)
        if form.is_valid():
            # first_name = form.cleaned_data['first_name']
            # last_name = form.cleaned_data['last_name']
            email = form.cleaned_data['email']
            # password = form.cleaned_data['pasword']
            username =email.split('@')[0]+email.split('@')[1].split('.')[0]
            obj = form.save(commit=False)
            obj.username = username
            obj.save()
            user = User.objects.get(username=username)
            group = Group.objects.get(name='regular')
            user.groups.add(group)
            return redirect(to='/')
        return render(request,'register.html',{'form':form})

class UserLogout(View):
    def get(self,request,*args,**kwargs):
        logout(request)
        return redirect('user_login')
class UserEdit(View):
    def get(self,request,*args,**kwargs):
        pass
