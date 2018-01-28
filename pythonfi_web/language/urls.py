from django.conf.urls import url
from pythonfi_web.language.eg.views import ajax_crud, ajax_crud_create, ajax_crud_update, ajax_crud_delete


urlpatterns = [

    url(
        regex=r'^ajax_crud$',
        view=ajax_crud,
        name='ajax_crud'
    ),
    url(
        regex=r'^ajax_crud/create$',
        view=ajax_crud_create,
        name='ajax_crud_create'
    ),
    url(
        regex=r'^ajax_crud/(?P<pk>\d+)/update$',
        view=ajax_crud_update,
        name='ajax_crud_update'
    ),
    url(
        regex=r'^ajax_crud/(?P<pk>\d+)/delete$',
        view=ajax_crud_delete,
        name='ajax_crud_delete'
    ),

]