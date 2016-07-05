from __future__ import unicode_literals

from django.db import models
from users.models import *

# Create your models here.

class Project(models.Model):
    title = models.CharField(max_length=100)
    owner = models.CharField(max_length=50) # not necessary
    pub_date = models.DateField()
    language = models.CharField(max_length=50)
    user = models.ForeignKey(User)

    def __str__(self):
        return self.title

class Code(models.Model):
    # for One to Many relationship
    project = models.ForeignKey(Project)
    
    def __str__(self):
        return self.project

