from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings
import views


urlpatterns = [
 
    url(r'^$', views.index, name='index'),
    url(r'^skcmdb/', include('skcmdb.urls')),
    url(r'^admin/', admin.site.urls),
    url(r'^skconfig/', include('skconfig.urls')),
    url(r'^skaccounts/', include('skaccounts.urls')),
    url(r'^sktask/', include('sktask.urls')),
    url(r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT}),

]
