from django.conf.urls import url


from . import views
app_name = 'counters_app'
urlpatterns = [
	url(r'^simple_chart/$', views.simple_chart, name="simple_chart"),
    	url(r'^$', views.index, name='index'),
]
