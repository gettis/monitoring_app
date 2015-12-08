
from django.shortcuts import render
from django.template import RequestContext, loader
from django.http import HttpResponse
from .models import Counter

from bokeh.plotting import figure
from bokeh.resources import CDN
from bokeh.embed import components

def simple_chart(request):
    plot = figure()
    plot.circle([1,2], [3,4])
    script, div = components(plot, CDN)
    context = RequestContext(request,{"the_script":script, "the_div":div})
    return render(request, "counters_app/simple_bokeh.html",context)

def index(request):	
	latest_counter = Counter.objects.order_by("pub_date")[:5]
	context = RequestContext(request,{'latest_counter':latest_counter,} )
	return render(request,'counters_app/Counter.html',context)

