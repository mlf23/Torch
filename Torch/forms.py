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