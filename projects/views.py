from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from projects.models import User, Project, Code
# Create your views here.

class ProjectsModelView(TemplateView):
    template_name = 'projects/main.html'

    def get_context_data(self, **kwargs):
        context = super(ProjectsModelView, self).get_context_data(**kwargs)
        context['object_list'] = ['User']
        return context

class UserList(ListView):
    model = User

class ProjectList(ListView):
    model = Project

class CodeList(ListView):
    model = Code

class UserDetail(DetailView):
    model = User

    def get_context_data(self, **kwargs):
        self.object = self.get_object() # Caution!!!!!!!!!!!!
        project_list = Project.objects.filter(user_id = self.kwargs['pk']).order_by('-pub_date')
        context = {'project_list': project_list, 'object': self.object}
        return context
