from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import Group,User
from django.contrib.auth import authenticate, login,logout
from django.views import View
from .form import RegisterForm,LoginForm
from .models import Profile

class UserProfile(View):
    '''
    User profile page will be handled by the views,
    it will return the loged in user profile with basic
    information of that user,
    and will be shown if and only if a user is logged in and only profile 
    owner will can see the that.
    '''
    def get(self,request,*args,**kwargs):
        # only get request will be handled to the authenticate user.
        user = request.user
        profile = Profile.objects.get(user = user)
        return render(request,'user/profile.html',{'profile':profile})

class UserLogin(View):
    '''
    Any anonymous and user can visit that paze, If any one try to navigate paze
    that is only for the authencate user only will be redirect here.
    '''
    def get(self,request,*args,**kwargs):
        #get request to logged in
        frm = LoginForm()
        return render(request,'user/login.html',{'form':frm})
    def post(self,request,*args,**kwargs):
        #post request for receivin user data for authenticate
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
    '''
    if anyone want to create a new profile will be here,
    for register himself for bazaw profile
    '''
    def get(self,request,*args,**kwargs):
        #for passing the form
        frm = RegisterForm()
        return render(request,'user/register.html',{'form':frm})
    def post(self,request,*args,**kwargs):
        #For validate the informations and create a profile
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
    '''
    Logged in user logot will be handled
    '''
    def get(self,request,*args,**kwargs):
        logout(request)
        return redirect('user_login')
class UserEdit(View):
    '''
    Authenticate user can edit their personal informations
    '''
    def get(self,request,*args,**kwargs):
        pass
