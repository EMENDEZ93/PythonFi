from django.conf.urls import url
from pythonfi_web.website.views import hola, manager_example, model_method, listview_example

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
]