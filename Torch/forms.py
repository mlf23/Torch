from django import forms

from .models import GitFile


class FileForm(forms.Form):
    docfile = forms.FileField(
        label=''
    )


class GitFileForm(forms.Form):
    gitFile = forms.URLField(
        label='git url'
    )

from Torch.models import *

class UploadFileForm(forms.Form):
     Lddfile = forms.FileField(
         label='Select a file'
     )

