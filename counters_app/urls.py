from django.conf.urls import url


from . import views
app_name = 'counters_app'
urlpatterns = [
	url(r'^dashboard/(?P<counter_name>\w+)/(?P<db>\w+)$', views.dashboard, name="dashboard"),        
        url(r'^start-apps/(?P<url_hash>\d+)/$', views.get_apps, name='get_apps'),
	url(r'^start-counter/(?P<app_name>\w+)/(?P<url_hash>\d+)/',views.get_counter, name='get_counter'),
        url(r'^$', views.get_url, name = "get_url"),
]
