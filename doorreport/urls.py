from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^doorlogger/', include('doorlogger.urls')),
    url(r'^admin/', admin.site.urls),
]