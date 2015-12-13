
from django.shortcuts import render
from django.template import RequestContext, loader
from django.http import HttpResponse, HttpResponseRedirect
from .models import Counter

from bokeh.models import HoverTool
from collections import OrderedDict
from bokeh.plotting import figure,ColumnDataSource,vplot
from bokeh.resources import CDN
from bokeh.embed import components
from bokeh.charts import Histogram
import datetime
import requests
from forms import URLForm
'''
url = "http://localhost:8000/metrix/"

r = requests.get(url)
content = r.content

list_counters = content.split("<br \>")

for counter in list_counters:
    if counter != "":
        c = counter.split("=")
        d = Counter(counter_name= c[0], counter_value= c[1])
        d.save()
'''
def get_url(request):
        if request.method == 'POST':
            form = URLForm(request.POST)
            if form.is_valid():
                url = form.cleaned_data["URL"]
                try:
                    r = requests.get(url)
                except requests.exceptions.RequestException as e:
                    print e
                    return HttpResponse("Connection failed")
                else:
                    content = r.content
                    list_counters = content.split("<br \>")
                    
                    for counter in list_counters:
                        if counter != "":
                            c = counter.split("=")
                            d = Counter(counter_name= c[0], counter_value= c[1])
                            d.save()

                    return HttpResponseRedirect('/counters_app/start')
    # if a GET (or any other method) we'll create a blank form
        else:
            form = URLForm()

        return render(request, 'counters_app/URL.html', {'form': form})
def slope(x1,y1,x2,y2):
	return str(float(y2 - y1)/(x2 - x1))


def simple_chart(request,counter_name):
	counter_len = len(Counter.objects.values())
	
	Date = [Counter.objects.values()[i]["pub_date"] for i in range(counter_len)]
	name = counter_name
	y_values = Counter.objects.values_list("counter_value",flat=True).filter(counter_name=counter_name)
	
	points = zip(Date,y_values)
	 
	ddict = OrderedDict({'Date':Date})
	#ddict[name] = y_values
	

	#plot specifications	
	TOOLS="pan,wheel_zoom,box_zoom,reset,hover,save"	
	p = figure(width=1200, height=400, x_axis_type="datetime",tools=TOOLS,title=name+"'s Metrics" )	
	p.min_border_left = 100
	p.min_border_top = 50
	p.border_fill = 'whitesmoke'
	p.ygrid.band_fill_color = "#E6E6FA"	
	p.title_text_color = "olive"
	p.title_text_font = "times"
	p.title_text_font_style = "italic"	
	

	p.outline_line_width = 7
	p.outline_line_alpha = 0.3
	p.outline_line_color = "black"	
	
	#HoverTool specifications
	source = ColumnDataSource(
       		 data=dict(
		
		rates = [slope(points[i][0].microsecond,points[i][1],points[i+1][0].microsecond,points[i+1][1]) for i in range(len(points)-1)]
		)       		 
   	 )	


	hover = p.select(dict(type=HoverTool))
	hover.point_policy = "follow_mouse"
	hover.tooltips = OrderedDict([
	("Counter Name",name),
   	("Rate of count","@rates c/us"),
	])
	
	p.line(Date,y_values,line_width=1,source=source)
	p.square(Date, y_values, fill_color=None, line_color="green",size=4)
	script1, div1 = components(p, CDN)

	hist = Histogram(list(y_values),bins=50,title='Histogram')
	hist.border_fill = 'whitesmoke'
	hist.background_fill = "beige"
	
	script2, div2 = components(hist, CDN)
	
	#area = Area(list(y_values),title="CDF")
	#area.border_fill ="whitesmoke"
	#area.background_fill = "#191970"
		
	#script3, div3 = components(area,CDN)

	


	context = RequestContext(request,{"the_script1":script1, "the_div1":div1,"the_script2":script2,"the_div2":div2})#,"the_script3":script3,"the_div3":div3})	

	return render(request, "counters_app/simple_bokeh.html",context)

def index(request):	
	counter_len = len(Counter.objects.values())
	counter_names = [str(Counter.objects.values().order_by("pub_date")[i]["counter_name"]) for i in range(counter_len)]
	latest_counter = list(set(counter_names))
	context = RequestContext(request,{'latest_counter':latest_counter,} )
	return render(request,'counters_app/Counter.html',context)

