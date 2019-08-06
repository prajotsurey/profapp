from django.contrib import admin
from django.urls import path,include
from . import views
from django.conf.urls import url

app_name = "articles"
urlpatterns = [
    url(r'^create/$',views.articleCreate, name = 'create'),
    url(r'^publicarticles/$',views.publicArticles, name ='publiclist'),
    url(r'^yourarticles/$',views.userArticles, name ='yourlist'),
    url(r'^(?!create|publicarticles|yourarticles)(?P<slug>[\w-]+)/$',views.articleDetail , name = 'detail'),
]
