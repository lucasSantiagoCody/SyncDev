from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login,logout as auth_logout, get_user_model
from .models import CustomUser, Profile
from django.contrib import messages
from django.contrib.messages import constants
from django.urls import reverse, reverse_lazy
from django.contrib.auth.decorators import login_required
from .utils import verify_years_old
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.views import LoginView, PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView
from .forms import CustomUserCreationForm, LoginForm
from django.conf import settings
from PIL import Image
import os
from django.views.decorators.csrf import csrf_exempt
import json

def signup(request):
    if request.method == 'GET':
        form = CustomUserCreationForm
        return render(request, 'signup.html', {'form':form})
    elif request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        context =  {
            'username': username,
            'email':  email,
            'password1': password1,
            'password2': password2
        }
        context_serializer = context.json()
        if password1 == password2:
            try:
                user = CustomUser.objects.create_user(username=username, email=email, password=password1)
                user.save()
                messages.add_message(request, constants.SUCCESS, 'Successfully Created Account  ')
                return redirect(reverse('login'))
            except:
                verify_user = CustomUser.objects.filter(email__exact=email)
                
                if verify_user:
                    messages.add_message(request, constants.WARNING, '')
                    return JsonResponse({'status':"Use another E-mail!", 'context': context_serializer})
                elif not verify_user:
                    return JsonResponse({'status':"Could Not Create  Acccount!", 'context': context_serializer})
        else:
            return JsonResponse({'status':"The two Password fields didn't match!",
                                 'context':context_serializer})


def login(request):
    if request.method == 'GET':
        form = LoginForm
        return render(request,'login.html', {'form': form})
    elif request.method == 'POST':        
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(email=email, password=password)
    
        if user:
            auth_login(request, user)
            return redirect(reverse('index'))
        elif not user:
            verify_user = CustomUser.objects.filter(email=email)
            if verify_user:
                messages.add_message(request, constants.ERROR, 'Password Invalid!')
            elif not verify_user:
                messages.add_message(request, constants.ERROR, 'User Not Found!')
            return redirect(reverse('login'))

@login_required
def profile(request):
    profile = Profile.objects.get(user=request.user)

    if request.method == 'GET':
        if profile.phone and profile.nif and profile.date_of_birth:
            profile_informations  = 'found'
        else:
            profile_informations  = 'not found'
        return render(request, 'profile.html', {'profile': profile, 'profile_informations': profile_informations})


@login_required 
def add_info_profile(request):
    profile = Profile.objects.get(user=request.user)

    if request.method == 'POST':
        phone = request.POST.get('phone')
        nif = request.POST.get('nif')
        date_of_birth = request.POST.get('date_of_birth')
        
        # verifications about nif and date born
        verify_nif_exist = Profile.objects.filter(nif__exact=nif)
        verify_date_born = verify_years_old(date_of_birth)

        if verify_date_born == 'invalid':
            messages.add_message(request, constants.ERROR, 'Deves ter uma idade superior ou igual à 13 anos')
            return redirect(reverse('profile'))
        if verify_nif_exist:
            messages.add_message(request, constants.ERROR, 'Use another Nif')
            return redirect(reverse('profile'))

        try:
            profile.phone = phone
            profile.nif = nif
            profile.date_of_birth = date_of_birth
            profile.save()
            messages.add_message(request, constants.SUCCESS, 'Successfully Saved Informations')
        except:
            messages.add_message(request, constants.ERROR, 'Unable To Save Profile Informations')
            
    return redirect(reverse('profile'))


@login_required
def edit_profile(request):

    if request.method == 'POST':
        user = CustomUser.objects.get(email=request.user.email)
        profile = Profile.objects.get(user=user)
        form = request.POST.get('form')

        if form == 'yourself':
            try:
                name = request.POST.get('name')
                profile_informations = request.POST.get('profile_informations')
                if profile_informations == 'found':
                    phone = request.POST.get('phone')
                    nif = request.POST.get('nif')
                    date_of_birth = request.POST.get('date_of_birth')
                    profile.phone = phone
                    profile.nif = nif
                    # remove this code in future
                    if date_of_birth:
                        profile.date_of_birth = date_of_birth 
                user.username = name
                user.save()
                profile.save()
                messages.add_message(request, constants.SUCCESS, 'Successfully To Edit your informations')
            except:
                messages.add_message(request, constants.ERROR, 'Unable To Edit Your Informations')
        elif form == 'login_options':
            email = request.POST.get('email')
            try: 
                user.email = email
                user.save()
                messages.add_message(request, constants.SUCCESS, 'Successfully To Edit your informations')
            except:
                messages.add_message(request, constants.SUCCESS, 'Unable To Edit your informations')

    return redirect(reverse('profile'))


@login_required
def save_profile_picture(request):
    profile = Profile.objects.get(user=request.user)
    if profile.profile_picture:
        try:
            image = profile.profile_picture 
            path = os.path.join(settings.MEDIA_ROOT, str(image))
            os.remove(path)
        except:
            messages.add_message(request, constants.ERROR, 'Could not to remove the old image')
    if request.method == 'POST':
        profile_picture = request.FILES.get('file')
        try:
            profile.profile_picture = profile_picture
            profile.save()
            messages.add_message(request, constants.SUCCESS, 'Successfully Saved Profile Picture')
        except:
            messages.add_message(request, constants.ERROR, 'Unable To Save Profile Picture!')
    
    return redirect(reverse('profile'))


@login_required
def password_change(request):
    if request.method ==  'GET':
        return render(request, 'password_change.html')
    elif request.method == 'POST':
        old_password  = request.POST.get('old_password')
        new_password1 = request.POST.get('new_password1')
        new_password2 = request.POST.get('new_password2')
        user = CustomUser.objects.get(email=request.user.email)

        if new_password1 == new_password2:
            user_authenticate = authenticate(email=request.user.email, password=old_password)
            if user_authenticate:
                try:
                    user.set_password(new_password1)
                    user.save()
                    auth_login(request, user)
                    messages.add_message(request, constants.SUCCESS, 'Successfully changed password')
                except:
                    messages.add_message(request, constants.ERROR, 'Could Not Changed password')
            else:
                messages.add_message(request, constants.ERROR, 'Old Password Is Invalid')
        else:
            messages.add_message(request, constants.ERROR, 'Passwords (P1, P2) Not Match')
        return redirect(reverse('password_change'))



class ResetPasswordView(PasswordResetView):
    template_name='password_reset.html'
    html_email_template_name='password_reset_email.html'

class ResetPasswordDoneView(PasswordResetDoneView):
    template_name='password_reset_done.html'

class ResetPasswordConfirmView(PasswordResetConfirmView):
    template_name='password_reset_confirm.html'
    
class ResetPasswordCompleteView(PasswordResetCompleteView):
    template_name='password_reset_complete.html'

        
def logout(request):
    auth_logout(request)
    messages.add_message(request, constants.SUCCESS, 'Logout Success')
    return redirect(reverse('index'))

