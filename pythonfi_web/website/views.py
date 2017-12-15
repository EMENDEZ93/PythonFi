from django.shortcuts import render, redirect
from pythonfi_web.website.models import ModelTest
from django.views.generic import ListView
from django.conf import settings
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login

from django.views.generic import ListView
from django.views.generic.detail import DetailView



def authentication(request):
    co = {}

    if request.method == 'POST':
        action = request.POST.get('action', None)
        username = request.POST.get('username', None)
        password = request.POST.get('password', None)

        if action == 'singup':
            user = User.objects.create_user(username=username, password=password)
            user.save()
            print('********************************************')
        elif action == 'login':
            print('_____________________________________________')
            user = authenticate(username=username, password=password)
            login(request, user)
        return redirect('hello')

    return render(request, 'website/login.html', co)


def hello(request):
    return render(request, 'hello.html')



def hola(request, template_name='e.g.html'):
    data = {}

    data['test']=ModelTest.objects.all()
    #print ( os.path.join(os.path.abspath(__file__), 'static').replace('\\', '/') )

    print ( settings.STATIC_ROOT )

    return render(request,template_name, data)


def manager_example(request, template_name='manager_example.html'):
    data = {}
    data['test']=ModelTest.objects.lastname_filter('Edwin')
    return render(request,template_name, data)


def model_method(request, template_name='model_metho.html'):
    data = {}
    data['test']=ModelTest.objects.all()
    return render(request,template_name, data)


def index_(request, template_name='website/index_.html'):
    return render(request,template_name)


def admin_(request, template_name='admin/index_.html'):
    return render(request,template_name)


class listview_example(ListView):
    model = ModelTest


