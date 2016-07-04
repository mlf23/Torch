"""untitled5 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.contrib import admin
from Torch import views


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^projects/', include('Torch.urls')),
    url(r'^index/', 'Torch.views.fileup'),
    url(r'^index/$', 'Torch.views.fileup', name='fileup'),
    url(r'^report_card/', 'Torch.views.report'),
    url(r'^main/', include('projects.urls')),
    url(r'^', include('projects.urls')),
    url(r'^main/', include('projects.urls', namespace="projects")),
    url(r'^sign_up/', 'Torch.views.sign_up'),
]
