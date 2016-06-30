from django.http import Http404
from django.shortcuts import render
from django.template import loader

from django.http import HttpResponse
from .models import Project



# Create your views here.
def projects(request):
    all_projects = Project.objects.all()
    template = loader.get_template('torch/projects.html')
    context = {
        'all_projects': all_projects,

    }
    return render(request, 'torch/projects.html', context)

def detail(request, user_id):
    return HttpResponse("<h2>Details for projects user: " +str(user_id) +"</h2>")

def index(request):
    return render(request, 'torch/index.html')

def report(request):
    return render(request, 'torch/report_card.html')