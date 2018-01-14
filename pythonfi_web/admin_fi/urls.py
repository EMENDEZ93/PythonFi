from django.contrib.auth import views as auth_views
from django.conf.urls import url
from pythonfi_web.admin_fi.login.views import admin_login, home, setting, password, signup, home_test
from .login import views as core_views

urlpatterns = [

    url(
        regex=r'^signup/$',
        view=signup,
        name='signup'
    ),
    url(
        regex=r'^login/$',
        view=auth_views.LoginView.as_view(template_name='admin/login/_login.html'),
        name='login'
    ),
    url(
        regex=r'^logout/$',
        view=auth_views.LogoutView.as_view(),
        name='logout'
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
        regex=r'^reset/$',
        view=auth_views.PasswordResetView.as_view(
            template_name='admin/login/password_reset.html',
            email_template_name='admin/login/password_reset_email.html',
            subject_template_name='admin/login/password_reset_subject.txt'),
        name='password_reset'
    ),
    url(
        regex=r'^reset/done$',
        view=auth_views.PasswordResetDoneView.as_view(template_name='admin/login/password_reset_done.html'),
        name='password_reset_done'
    ),
    url(
        regex=r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        view=auth_views.PasswordResetConfirmView.as_view(template_name='admin/login/password_reset_confirm.html'),
        name='password_reset_confirm'
    ),
    url(
        regex=r'^reset/complete/$',
        view=auth_views.PasswordResetCompleteView.as_view(template_name='admin/login/password_reset_complete.html'),
        name='password_reset_complete'
    ),
    url(
        regex=r'^settings/password/$',
        view=auth_views.PasswordChangeView.as_view(template_name='admin/login/password_change.html'),
        name='password_change'
    ),
    url(
        regex=r'^settings/password/done/$',
        view=auth_views.PasswordChangeDoneView.as_view(template_name='admin/login/password_change_done.html'),
        name='password_change_done'
    ),



    url(
        regex=r'^facultad$',
        view=admin_login,
        name='adminfi'
    ),

    url(
        regex=r'^$',
        view=home,
        name='home'
    ),

    url(
        regex=r'^test$',
        view=home_test,
        name='home_test'
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