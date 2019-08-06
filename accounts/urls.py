from django.contrib import admin
from django.urls import path,include
from . import views
from django.conf.urls import url

app_name = 'accounts'
urlpatterns = [
    url(r'^signup/$',views.signup_view, name = 'signup'),
    url(r'^login/$',views.login_view, name = 'login'),
    url(r'^logout/$',views.logout_view,name='logout'),
]