from django.shortcuts import render


def admin_(request, template_name='admin/base.html'):
    return render(request,template_name)
