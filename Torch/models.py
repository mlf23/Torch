from django.db import models

# Create your models here.

class Project(models.Model):
    language = models.CharField(max_length=250)
    projects = models.CharField(max_length=250)


    def __str__(self):
        return self.language + ' | ' + self.projects

class ReportCard(models.Model):
    language = models.ForeignKey(Project, on_delete=models.CASCADE)

class LoadFile(models.Model):
    docfile = models.FileField(upload_to='file_load/%Y/%m/%d')

class GitFile(models.Model):
    giturl = models.URLField(max_length=1000)
    gitFile = models.FileField(upload_to='Git/%Y/%m/%d')
    newFile = models.FilePathField(path='Git/%Y/%m/%d', recursive=True)