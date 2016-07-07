from django.conf.urls import patterns, url

from projects import views

urlpatterns = [
    # default
    # url(r'^$', views.main, name='main'),
    url(r'^$', views.ProjectsModelView.as_view(), name='projects'),

    url(r'^project/$', views.ProjectList.as_view(), name='project_list'),

    url(r'^user/$', views.UserList.as_view(), name='user_list'),

    url(r'^user/(?P<pk>\d+)/$', views.UserDetail.as_view(), name='user_detail'),

    url(r'^project/(?P<pk>\d+)/$', views.ProjectDetail.as_view(), name='project_detail'),

    url(r'^printAddProject/$', views.printAddProject, name='printAddProject'),
]
