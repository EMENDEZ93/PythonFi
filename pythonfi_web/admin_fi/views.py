from django.shortcuts import render


def admin_(request, template_name='admin/index_.html'):
    return render(request,template_name)
