from django.conf.urls import url

from pythonfi_web.language.datagrid.basic.views import basic, basic_update

from pythonfi_web.language.eg.export_excel.views import export_users_csv, export_users_xls
from pythonfi_web.language.eg.views import ajax_crud, ajax_crud_create, ajax_crud_update, ajax_crud_delete
from pythonfi_web.language.eg.ajax_request.views import SignUpView, validate_username
from pythonfi_web.language.eg.multiple_file_upload_ajax import views
from pythonfi_web.language.eg.filter_querysets_dynamically.views import search


from django_filters.views import FilterView
from pythonfi_web.language.eg.filter_querysets_dynamically.filters import UserFilter2



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

    url(
        regex=r'^ajax_request',
        view=SignUpView.as_view(),
        name='SignUpView'
    ),
    url(
        regex=r'^validate_username/',
        view=validate_username,
        name='validate_username'
    ),

    url(r'^clear/$', views.clear_database, name='clear_database'),
    url(r'^basic-upload/$', views.BasicUploadView.as_view(), name='basic_upload'),
    url(r'^progress-bar-upload/$', views.ProgressBarUploadView.as_view(), name='progress_bar_upload'),
    url(r'^drag-and-drop-upload/$', views.DragAndDropUploadView.as_view(), name='drag_and_drop_upload'),

    url(r'^export/csv/$', export_users_csv, name='expost_user_csv'),
    url(r'^export/xls/$', export_users_xls, name='export_users_xls'),

    url(r'^filtro$', search, name='search'),

    url(r'^filtro_class$', FilterView.as_view(filterset_class=UserFilter2,
        template_name='admin/admin_fi/eg/filter_querysets_dynamically/user_list2.html'), name='search_2'),

    url(
        regex=r'^basic$',
        view=basic,
        name='basic'
    ),

    url(
        regex=r'^basic_update$',
        view=basic_update,
        name='basic_create'
    ),

]