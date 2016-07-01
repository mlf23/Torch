from django import forms
from Torch.models import *

class UploadFileForm(forms.Form):
     Lddfile = forms.FileField(
         label='Select a file'
     )