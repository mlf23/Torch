from django.conf.urls import patterns, url

from . import views


urlpatterns = [
    url(r'^$', views.start, name='start'),
    url(r'^index/$', views.gitLoader, name='gitloader'),
    url(r'^report_card/$', views.report, name='report'),
    url(r'^start/$', views.start),
    url(r'^start/index/$', views.index),
    url(r'^sign_up/$', views.sign_up),
    url(r'^settings/$', views.settings),


    # url(r'^$', views.projects, name='projects'),
    #/projects/123/
    # url(r'^(?P<user_id>[0-9]+)/$', views.detail, name = 'detail'),
]
