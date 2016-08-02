from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.views import generic
from .models import Door, Event
import requests
import json
import time

class IndexView(generic.ListView):
	template_name = 'doorlogger/index.html'
	context_object_name = 'latest_door_list'

	def get_queryset(self):
		return Door.objects.order_by('-door_name')[:5]

def logevent(request):
	return HttpResponse("Get here to log an event\n");	

class DetailView(generic.DetailView):
	model = Door
	template_name = 'doorlogger/detail.html'
