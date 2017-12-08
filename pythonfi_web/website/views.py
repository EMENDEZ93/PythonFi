from django.shortcuts import render
from pythonfi_web.website.models import ModelTest


def hola(request, template_name='e.g.html'):
    data = {}
    data['test']=ModelTest.testQuery.all()
    return render(request,template_name, data)


def manager_example(request, template_name='manager_example.html'):
    data = {}
    data['test']=ModelTest.objects.lastname_filter('Edwin')
    return render(request,template_name, data)
