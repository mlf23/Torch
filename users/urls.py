from django.conf.urls import url
from users.views import *

urlpatterns = [
    # url(r'^$', 'django.contrib.auth.views.login'),
    # url(r'^logout/$', logout_page),
    # url(r'^accounts/login/$', 'django.contrib.auth.views.login'),  # If user is not login it will redirect to login page
    url(r'^sign_up/$', sign_up),
    url(r'^success/$', register_success),
    # url(r'^home/$', home),
]
