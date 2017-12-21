
from django.conf.urls import url,include
from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^$', views.index,name="home"),
    url(r'^download/$',views.download, name = "download"),
    url(r'^submit/$',views.submit,name="submit"),
    url(r'^myvideos/$',views.userVideosView.as_view(),name = "my-videos"),
    url(r'^myaudios/$',views.userAudiosView.as_view(),name = "my-audios"),
    url(r'^myfiles/$',views.models_form_upload,name="my-files"),
]
