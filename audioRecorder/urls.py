
from django.conf.urls import url,include
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
]

from django.views.generic import RedirectView
urlpatterns += [
	url(r'^$',RedirectView.as_view(url ='/youtubeadl/',permanent = True))
]

urlpatterns += [
	url(r'^youtubeadl/',include('youtubeadl.urls'))
]

#login and logout
from django.contrib.auth import views as auth_views
urlpatterns += [
	url(r'^accounts/',include('django.contrib.auth.urls')),
]

#use static to serve files
from django.conf import settings
from django.conf.urls.static import  static
urlpatterns += static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
