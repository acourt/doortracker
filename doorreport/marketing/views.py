from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse

def index(request):
	return HttpResponse("Welcome to the marketing site!")