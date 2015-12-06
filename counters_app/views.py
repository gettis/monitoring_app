from django.shortcuts import render
from django.template import RequestContext, loader
from django.http import HttpResponse
from .models import Counter

def index(request):
	
	latest_counter = Counter.objects.order_by("pub_date")[:5]
	template = loader.get_template('counters_app/Counter.html')
	context = RequestContext(request,{'latest_counter':latest_counter,} )
	return HttpResponse(template.render(context))

