from django.conf.urls import url

from . import views

app_name = "Item"

urlpatterns = [
    url(r'^(?P<region_selected>[-\w]+)/$', views.get_travel_data, name = 'travel_data'),
    url(r'^search/query/$', views.search_result, name='search_travel_data'),
    url(r'^search/keyword/$', views.keyword_result, name='keyword_search'),
    url(r'^search/query/detail/(?P<id>[-\w]+)/$', views.data_detail, name='travel_data_detail')
]
