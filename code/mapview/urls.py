from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.polygon, name='map'),
    url(r'^t/$', views.map, name='polygon_test'),

]
