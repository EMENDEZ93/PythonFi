from django.shortcuts import render

def admin_login(request, template_name='admin/login/login.html'):
    return render(request,template_name)
