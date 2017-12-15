from django.contrib.auth import views as auth_views
from django.conf.urls import url
from pythonfi_web.website.views import hola, manager_example, model_method, listview_example, authentication, hello, index_, admin_



urlpatterns = [

    url(
        regex=r'^index_$',
        view=index_,
        name='index_'
    ),

    url(
        regex=r'^admin_$',
        view=admin_,
        name='admin_'
    ),

    url(
        regex=r'^e.g$',
        view=hola,
        name='e.g'
    ),

    url(
        regex=r'^manager$',
        view=manager_example,
        name='manager'
    ),

    url(
        regex=r'^model$',
        view=model_method,
        name='modelmethod'
    ),

    url(
        regex=r'^listview$',
        view=listview_example.as_view(),
        name='listview'
    ),

    url(
        regex=r'^login$',
        view=authentication,
        name='login'
    ),

    url(
        regex=r'^respond$',
        view=hello,
        name='hello'
    ),

    url(r'^logout$',auth_views.logout, {'next_page' : '/respond'} , name='logout'),



]