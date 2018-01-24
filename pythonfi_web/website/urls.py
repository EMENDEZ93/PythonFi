from django.contrib.auth import views as auth_views
from django.conf.urls import url
from pythonfi_web.website.views import index_


urlpatterns = [

    url(
        regex=r'^index_$',
        view=index_,
        name='index_'
    ),

]