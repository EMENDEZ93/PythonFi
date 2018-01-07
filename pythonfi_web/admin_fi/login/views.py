from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AdminPasswordChangeForm, PasswordChangeForm, UserCreationForm
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth import login as auth_login
from django.contrib import messages
from django.shortcuts import render, redirect
from social_django.models import UserSocialAuth
from .forms import SignUpForm


def signup(request, template_name='admin/login/signup.html'):
    data = {}

    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect('home')
    else:
        form = SignUpForm()

    data['form'] = form
    return render(request, template_name, data)


def admin_login(request, template_name='admin/login/login.html'):
    return render(request,template_name)


@login_required
def home(request):
    return render(request,'admin/login/home.html')


@login_required
def setting(request):
    user = request.user

    try:
        github_login = user.social_auth.get(provider='github')
    except UserSocialAuth.DoesNotExist:
        github_login = None


    try:
        twitter_login = user.social_auth.get(provider='twitter')
    except UserSocialAuth.DoesNotExist:
        twitter_login = None

    can_disconnect = (user.social_auth.count() > 1 or user.has_usable_password())

    return render(request, 'admin/login/setting.html', {
        'github_login':github_login,
        'twitter_login': twitter_login,
        'can_disconnect ': can_disconnect
    })


@login_required
def password(request):
    if request.user.has_usable_password():
        PasswordForm = PasswordChangeForm
    else:
        PasswordForm = AdminPasswordChangeForm

    if request.method == 'POST':
        form = PasswordForm(request.user, request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            messages.success(request, 'Your password was successfully update')
            return redirect('password')
        else:
            messages.error(request, 'Please correct the error below')
    else:
        form = PasswordForm(request.user)
    return render(request,'admin/login/password.html', {'form':form})