from django.conf.urls import url
from pythonfi_web.website.views import hola

urlpatterns = [
    url(
        regex=r'^e.g$',
        view=hola,
        name='e.g'
    ),
]