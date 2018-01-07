from django.contrib.auth import views as auth_views
from django.conf.urls import url
from pythonfi_web.admin_fi.login.views import admin_login, home, setting, password, signup


urlpatterns = [

    url(
        regex=r'^signup/$',
        view=signup,
        name='signup'
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