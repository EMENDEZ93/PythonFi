from django.shortcuts import render

def index_(request, template_name='website/index_.html'):
    return render(request,template_name)
