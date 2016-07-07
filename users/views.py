from django.shortcuts import render

# Create your views here.
from users.forms import *
# from users.files import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.views.decorators.csrf import csrf_protect
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.template import RequestContext


def register_success(request):
    return render_to_response(
        'users/success.html',
    )


def logout_page(request):
    logout(request)
    return HttpResponseRedirect('/')


@login_required
def home(request):
    return render_to_response(
        'home.html',
        {'user': request.user}
    )