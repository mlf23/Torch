from django.conf.urls import patterns, url

from . import views


urlpatterns = [
    #/projects/
    #url(r'^$', views.index, name='index'),
    url(r'^$', views.projects, name='projects'),

    #/projects/123/
    url(r'^(?P<user_id>[0-9]+)/$', views.detail, name = 'detail'),

]
