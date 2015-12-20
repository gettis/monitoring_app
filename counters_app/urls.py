from django.conf.urls import url


from . import views
app_name = 'counters_app'
urlpatterns = [
	url(r'^dashboard/(?P<counter_name>\w+)/(?P<db>\w+)$', views.dashboard, name="dashboard"),        
        url(r'^start/(?P<url_hash>\d+)/', views.index, name='index'),
        url(r'^$', views.get_url, name = "get_url"),
]
