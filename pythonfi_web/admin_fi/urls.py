from django.contrib.auth import views as auth_views
from django.conf.urls import url
from pythonfi_web.admin_fi.login.views import admin_login, home


urlpatterns = [

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

]