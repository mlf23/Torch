from django.conf.urls import patterns, url
from dashboard import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<project_id>\d+)/$', views.detail, name='detail'),
    url(r'^(?P<project_id>\d+)/code_detail/(?P<code_id>\d+)/$', views.code_detail, name='code_detail'),
    url(r'^(?P<project_id>\d+)/code_analyze/$', views.code_analyze, name='code_analyze'),
    url(r'^landering/$', views.landering, name='landering'),
    url(r'^test/$', views.test, name='test'),
]
