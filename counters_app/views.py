
from django.shortcuts import render
from django.template import RequestContext, loader
from django.http import HttpResponse
from .models import Counter

from collections import OrderedDict
from bokeh.plotting import figure
from bokeh.resources import CDN
from bokeh.embed import components
from bokeh.charts import TimeSeries
import datetime

def simple_chart(request,counter_name):
	counter_len = len(Counter.objects.values())
	Date = [Counter.objects.values()[i]["pub_date"] for i in range(counter_len)]
	name = counter_name
	y_values = Counter.objects.values_list("counter_value",flat=True).filter(counter_name=counter_name)
	
	ddict = OrderedDict({'Date':Date})
	ddict[name] = y_values

	plot = TimeSeries(ddict,index='Date',title=name,ylabel='Counter Values' )
	
	script, div = components(plot, CDN)
	context = RequestContext(request,{"the_script":script, "the_div":div})
	return render(request, "counters_app/simple_bokeh.html",context)

def index(request):	
	counter_len = len(Counter.objects.values())
	counter_names = [str(Counter.objects.values().order_by("pub_date")[i]["counter_name"]) for i in range(counter_len)]
	latest_counter = list(set(counter_names))
	context = RequestContext(request,{'latest_counter':latest_counter,} )
	return render(request,'counters_app/Counter.html',context)

