from django.conf.urls import url


from . import views
app_name = 'counters_app'
urlpatterns = [
	url(r'^simple_chart/(?P<counter_name>\w+)$', views.simple_chart, name="simple_chart"),        
        url(r'^start$', views.index, name='index'),
        url(r'^', views.get_url, name = "get_url"),
]
