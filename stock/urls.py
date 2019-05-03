from . import views
from django.urls import re_path


app_name = 'stock'

urlpatterns = [
   re_path(r'^$', views.index, name='index'),
   re_path(r'^sales/(?P<id>\d+)/', views.predict_sales, name='predict_sales'),
   re_path(r'^profit/(?P<id>\d+)/', views.predict_profit, name='predict_profit'),
   re_path(r'^demand/(?P<id>\d+)/', views.predict_demand, name='predict_demand'),
   re_path(r'^profit/graph/(?P<id>\d+)/', views.graphics_profit, name='graph'),
   re_path(r'^sales/graph/(?P<id>\d+)/', views.graphics_sales, name='graph_s'),
   re_path(r'^demand/graph/(?P<id>\d+)/', views.graphics_demand, name='graph_d'),
   re_path(r'^detail/(?P<id>\d+)/(?P<slug>[-\w]+)/$', views.detail, name='detail')
]
