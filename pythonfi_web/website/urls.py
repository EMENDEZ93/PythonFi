from django.conf.urls import url
from pythonfi_web.website.views import hola, manager_example

urlpatterns = [
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
]