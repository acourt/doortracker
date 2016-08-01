from django.conf.urls import url
from django.views.generic import TemplateView
from . import views

app_name = 'doorlogger'
urlpatterns = [
    
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^logevent$', views.logevent, name='logevent'),
	url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
	url(r'^.*$', views.IndexView.as_view(), name='index'),
    
    ]

