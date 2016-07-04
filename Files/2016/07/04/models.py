from __future__ import unicode_literals

from django.db import models
from django import forms
# Create your models here.

class Project(models.Model):
    project_name = models.CharField(max_length=200)
    pub_date = models.DateTimeField('data published')

    def __str__(self):
        return self.project_name

class Code(models.Model):
    project = models.ForeignKey(Project)
    code_title = models.CharField(max_length=100)
    code_contents = models.CharField(max_length=3000)
    author = models.CharField(max_length=100)

    def __str__(self):
        return self.code_title

class NameForm(forms.Form):
    your_name = forms.CharField(label='Your name', max_length=100)
