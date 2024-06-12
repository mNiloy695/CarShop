from django.shortcuts import render,redirect
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login,logout,authenticate,update_session_auth_hash
from django.contrib.auth.forms import AuthenticationForm,PasswordChangeForm,SetPasswordForm
from .forms import RegistrationForm,userChangeForm
from django.contrib import messages
from .forms import User
from car.models import Buy
from  django.views.generic import CreateView
from django.contrib.auth.views import LoginView ,LogoutView
from django.utils.decorators import method_decorator

# def registration(request):
#     if not request.user.is_authenticated:
#         if request.method=='POST':
#             form=RegistrationForm(request.POST)
#             if form.is_valid():
#                 messages.success(request,'Your registration Successfully completed')
#                 form.save()
#                 return redirect('login')
#         else:
#             form=RegistrationForm()
#         return render(request,'registration.html',{'form':form})
#     else:
#         return redirect('login')


class registrationView(CreateView):
     model=User
     form_class=RegistrationForm
     template_name='registration.html'
     success_url=reverse_lazy('login')
    
# def login_user(request): 
#     if not request.user.is_authenticated:
#         if request.method=='POST':
#             form=AuthenticationForm(request,request.POST)
#             if form.is_valid():
#                 name=form.cleaned_data['username']
#                 user_pass=form.cleaned_data['password']
#                 user=authenticate(username=name,password=user_pass)
#                 if user is not None:
#                     messages.success(request,'You logged successfully')
#                     login(request,user)
#                     return redirect('profile')
#                 else:
#                     messages.success(request,'Your logged infomation wrong')
#                     return redirect('login')
#         else:
#             form=AuthenticationForm()
#         return render(request,'login.html',{'form':form,'type':'Log In'})
#     else:
 
#        return redirect('profile')

class loginView(LoginView):
     template_name='login.html'
     def get_success_url(self):
          return reverse_lazy('profile')
     def from_valid(self,form):
          messages.success(self.request,'You successfully loged in')
          return super().form_valid(form)
     def form_invalid(self,form):
          messages.success(self.request,'your logged information is wrong')
          return super().form_invalid(form)
     def get_context_data(self,**kwargs):
          context=super().get_context_data(**kwargs)
          context['type']='Login'
          return context          

# @login_required
# def logout_user(request):
#     logout(request)
#     return redirect('home')
class logoutview(LogoutView):
     def get_success_url(self):
          return reverse_lazy('login')
@login_required
def profile(request):
    cars=Buy.objects.filter(user=request.user)
    return render(request,'profile.html',{'cars':cars})
@login_required 
def change_pass(request):
        if request.method=='POST':
            form=PasswordChangeForm(user=request.user,data=request.POST)
            if form.is_valid():
                messages.success(request,'your password succesfully updated')
                form.save()
                update_session_auth_hash(request,form.user)
                return redirect('home')
        else:
            form=PasswordChangeForm(user=request.user)
        return render(request,'login.html',{'form':form,'type':'Change Password'})
@login_required 
def change_pass2(request):
        if request.method=='POST':
            form=SetPasswordForm(user=request.user,data=request.POST)
            if form.is_valid():
                messages.success(request,'your password succesfully updated')
                form.save()
                update_session_auth_hash(request,form.user)
                return redirect('home')
        else:
            form=SetPasswordForm(user=request.user)
        return render(request,'login.html',{'form':form,'type':'Change your password'})
@login_required
def update(request,id):
        user=User.objects.get(pk=id)
        if request.method=='POST':
            form=userChangeForm(request.POST,instance=user)
            if form.is_valid():
                messages.success(request,'Your registration Successfully completed')
                form.save()
                messages.success(request,'Update successfully')
                return redirect('profile')
        else:
            form=userChangeForm(instance=user)
        return render(request,'update.html',{'form':form})