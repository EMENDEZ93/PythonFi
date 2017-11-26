from django.shortcuts import render


def hola(request):
    return render(request,template_name='e.g.html')
