from django.shortcuts import render
from pythonfi_web.website.models import ModelTest
from django.views.generic import ListView

def hola(request, template_name='e.g.html'):
    data = {}
    data['test']=ModelTest.objects.all()
    return render(request,template_name, data)


def manager_example(request, template_name='manager_example.html'):
    data = {}
    data['test']=ModelTest.objects.lastname_filter('Edwin')
    return render(request,template_name, data)


def model_method(request, template_name='model_metho.html'):
    data = {}
    data['test']=ModelTest.objects.all()
    return render(request,template_name, data)


class listview_example(ListView):
    model = ModelTest