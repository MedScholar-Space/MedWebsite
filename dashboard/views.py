from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib import messages
import random

from .forms import *
from django.core.paginator import Paginator ,EmptyPage,PageNotAnInteger
from Quiz.models import *
from Results.models import *
from MedApp.models import *
def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(
                request, username=cd['Username'], password=cd['Password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect("logged")
                else:
                    return redirect("deactivated")
            else:
                return HttpResponse('Invalid login')
    else:
        form = LoginForm()
    context = {'form': form}
    return render(request, 'account/login.html', context)


def logged_in(request):
    return render(request, "account/logged_insuccess.html")


def deactivated(request):
    return render(request, "account/account_deactivated.html")


@login_required
def dashboard(request):
    profile = request.user
    results = Result.objects.filter(user=profile)
    user_semesters = request.user.profile.semestre.all()
    if request.method == 'POST':
        user_form = UserEditForm(instance=request.user,data=request.POST)
        profile_form = ProfileEditForm(instance=request.user.profile,data=request.POST,files=request.FILES)
        picture_form = ImageEditForm(instance=request.user.profile,data=request.POST,files=request.FILES)

        if user_form.is_valid():
            user_form.save()
        if profile_form.is_valid():
            profile_form.save()
    
        if picture_form.is_valid():
            picture_form.save()

            messages.success(request, 'Profile updated '\
            'successfully')
            return redirect("dashboard")

        else:
            messages.error(request, 'Error updating your profile')
            print('Something is wrong')
    else:
            user_form = UserEditForm(instance=request.user)
            profile_form = ProfileEditForm(instance=request.user.profile)
            picture_form = ImageEditForm(instance=request.user.profile)

    categories = Category.objects.filter(semestre__in=user_semesters  )
    context = {'profile':profile,'results':results,'d':categories,'user_form': user_form,'profile_form': profile_form,'picture_form':picture_form}
    return render(request,'account/dashboard.html',context)

@login_required
def dashboard_Test(request):
    profile = request.user
    results = Result.objects.filter(user=profile)
    
    user_semesters = request.user.profile.semestre.all()
    if request.method == 'POST':
        user_form = UserEditForm(instance=request.user,data=request.POST)
        profile_form = ProfileEditForm(instance=request.user.profile,data=request.POST,files=request.FILES)
        picture_form = ImageEditForm(instance=request.user.profile,data=request.POST,files=request.FILES)

        if user_form.is_valid():
            user_form.save()
        if profile_form.is_valid():
            profile_form.save()
    
        if picture_form.is_valid():
            picture_form.save()

            messages.success(request, 'Profile updated '\
            'successfully')
            return redirect("dashboard")

        else:
            messages.error(request, 'Error updating your profile')
            print('Something is wrong')
    else:
            user_form = UserEditForm(instance=request.user)
            profile_form = ProfileEditForm(instance=request.user.profile)
            picture_form = ImageEditForm(instance=request.user.profile)
        

    courses  = cour.objects.all()
    quizs  = Result.objects.filter(user=request.user)
    categories = Category.objects.filter(semestre__in=user_semesters  ) 
    context = {'profile':profile,'results':results,'quizs':quizs,'d':categories,'user_form': user_form,'profile_form': profile_form,'courses':courses,'picture_form':picture_form}
    return render(request,'Admin/Admin/index.html',context)

def register(request):
    semestres = Semestre.objects.all()
    semester1 = Semestre.objects.get(semestre="Free Trial")
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        profile_form = ProfileRegistration(request.POST)
        if user_form.is_valid() and profile_form.is_valid():
    # Create a new user object but avoid saving it yet
            new_user = user_form.save(commit=False)
            new_profile = profile_form.save(commit=False)
# Set the chosen password
            new_user.set_password(
            user_form.cleaned_data['password'])
            new_profile.user = new_user

# Save the User object
            new_user.save()
            

            new_profile.save()
            new_profile.semestre.add(semester1)
            print(type(new_profile.semestre))

            return render(request,
              'account/register_done.html',
              {'new_user': new_user })

    else:
        user_form = UserRegistrationForm()
        profile_form = ProfileRegistration()
        print(f'{user_form.errors}\n {profile_form.errors}')
    return render(request,
              'account/register.html',
              {'user_form': user_form,'profile_form':profile_form,'semestres':semestres})

@login_required
def edit(request):  
    profile= Profile.objects.all()
    if request.method == 'POST':
        user_form = UserEditForm(instance=request.user,data=request.POST)
        profile_form = ProfileEditForm(instance=request.user.profile,data=request.POST,files=request.FILES)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, 'Profile updated '\
            'successfully')
            return redirect("dashboard")
        else:
            messages.error(request, 'Error updating your profile')
    else:
            user_form = UserEditForm(instance=request.user)
            profile_form = ProfileEditForm(instance=request.user.profile)
    return render(request,'account/edit.html',{'user_form': user_form,'profile_form': profile_form})
