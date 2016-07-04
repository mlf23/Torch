from django.shortcuts import get_object_or_404, render
from dashboard.models import Project, Code, NameForm
from django.http import HttpResponseRedirect
# Create your views here.

def index(request):
    if request.method == 'POST':
        form = NameForm(request.POST)
        if form.is_valid():
            return HttpResponseRedirect('dashboard/test')
    else:
        form = NameForm()

    project_list = Project.objects.all().order_by('-pub_date')
    context = {'project_list': project_list, 'form': form} # mapping for using in template
    return render(request, 'dashboard/index.html', context)

def detail(request, project_id):
    project = get_object_or_404(Project, pk=project_id)
    return render(request, 'dashboard/detail.html', {'project': project})

def code_detail(request, code_id, project_id):
    project = get_object_or_404(Project, pk=project_id)
    code = get_object_or_404(Code, pk=code_id)
    return render(request, 'dashboard/code_detail.html', {'code': code, 'project': project})

def code_analyze(request, project_id):
    project = get_object_or_404(Project, pk=project_id)
    return render(request, 'dashboard/code_analyze.html', {'project': project})

def landering(request):
    return render(request, 'dashboard/landering.html')

def test(request):
    return render(request, 'dashboard/test.html')
