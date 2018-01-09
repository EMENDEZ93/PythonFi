from django.contrib.auth import views as auth_views
from django.conf.urls import url
from pythonfi_web.admin_fi.login.views import admin_login, home, setting, password, signup
from .login import views as core_views

urlpatterns = [

    url(
        regex=r'^signup/$',
        view=signup,
        name='signup'
    ),

    url(
        regex=r'^account_activation_sent/$',
        view=core_views.account_activation_sent,
        name='account_activation_sent'
    ),

    url(
        regex=r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        view=core_views.activate,
        name='activate'
    ),

    url(
        regex=r'^facultad$',
        view=admin_login,
        name='adminfi'
    ),

    url(
        regex=r'^home$',
        view=home,
        name='home'
    ),

    url(
        regex=r'^settings$',
        view=setting,
        name='settings'
    ),

    url(
        regex=r'^settings/password/$',
        view=password,
        name='password'
    ),

]