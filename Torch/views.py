from django.http import Http404
from django.shortcuts import render
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.template import RequestContext
from django.core.urlresolvers import reverse
from django.template import loader
from django.http import HttpResponse
from .models import Project

from .models import Upload
from .forms import UploadFileForm



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

def fileup(request):
    # Handle file upload
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            newdoc = Upload(Lddfile=request.FILES['Lddfile'])
            newdoc.save()

            # Redirect to the document list after POST
            return HttpResponseRedirect(reverse("Torch.views.fileup"))
    else:
        form = UploadFileForm()  # A empty, unbound form

    # Load documents for the list page
    files = Upload.objects.all()

    # Render list page with the documents and the form
    return render_to_response(
        'torch/index.html',
        {'files': files, 'form': form},
        context_instance=RequestContext(request)
    )

