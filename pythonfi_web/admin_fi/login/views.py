from django.shortcuts import render
from django.contrib.auth.decorators import login_required


def admin_login(request, template_name='admin/login/login.html'):
    return render(request,template_name)


@login_required
def home(request):
    return render(request,'admin/login/home.html')