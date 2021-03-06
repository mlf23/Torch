from django.http import Http404
from django.shortcuts import render
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.template import RequestContext
from django.core.urlresolvers import reverse
from django.template import loader
from django.http import HttpResponse
from .models import Project
from users.models import User

from .models import LoadFile

from .forms import GitFileForm
import git
import os
from datetime import datetime
from .models import Upload
from .forms import UploadFileForm
from users.forms import RegistrationForm
from users.models import User

from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.views.decorators.csrf import csrf_protect
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.template import RequestContext

# Create your views here.
# def projects(request):
#     all_projects = Project.objects.all()
#     template = loader.get_template('torch/projects.html')
#     context = {
#         'all_projects': all_projects,
#
#     }
#     return render(request, 'torch/projects.html', context)

def detail(request, user_id):
    return HttpResponse("<h2>Details for projects user: " +str(user_id) +"</h2>")

def index(request):
    return render(request, 'torch/index.html')

def report(request):
    return render(request, 'torch/report_card.html')

#git file loader
def gitLoader(request):
    if request.method == 'GET':
        #form generated
        form_git = GitFileForm(request.GET, request.FILES)
        if form_git.is_valid():
            gitUrl = form_git.cleaned_data['gitFile']
            dirname = datetime.now().strftime('%Y-%m-%d-%H-%M')
            g = git.Repo.clone_from(gitUrl, dirname)

            # Redirect to the document list after POST
            return HttpResponseRedirect(reverse("Torch.views.gitLoader"))

    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            newdoc = Upload(Lddfile=request.FILES['Lddfile'])
            newdoc.save()

            # Redirect to the document list after POST
            return HttpResponseRedirect(reverse("Torch.views.gitLoader"))

    else:
        form_git = GitFileForm()  # A empty, unbound form
        form = UploadFileForm()
        files = Upload.objects.all()
    return render_to_response(
            'torch/index.html',
            {'files': files, 'form': form, 'form_git': form_git},
            context_instance=RequestContext(request)
    )


def sign_up(request):
    return render(request, 'torch/sign_up.html')

def start(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            # user = User.objects.create_user(
            #     username=form.cleaned_data['username'],
            #     password=form.cleaned_data['password1'],
            #     email=form.cleaned_data['email']
            # )
            user = User(username=form.cleaned_data['username'], password=form.cleaned_data['password1'], email=form.cleaned_data['email'])
            user.save()
            return HttpResponseRedirect('/users/success/')
    else:
        form = RegistrationForm()

    # 로그인 세션 확인
    # 아이디와 비밀번호 비교해서 로그인 성공 시 'login_info' 세션 생성해서 아이디 저장
    # request.session['login_info'] = "~~~id" 하고 is_login = TRUE 로 변경
    if request.session.get('login_info', False):
        is_login = True

    else:
        is_login = False

    print(is_login)

    variables = RequestContext(request, {
        'form': form,
        'is_login': is_login,
    })

    return render_to_response(
        'torch/start.html',
        variables,
    )

def settings(request):
    return render(request, 'torch/settings.html')
