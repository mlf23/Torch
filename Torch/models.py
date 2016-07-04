from django.db import models

# Create your models here.
#class Index(models.Model):
 #   filename = models.CharField()

class Project(models.Model):
    language = models.CharField(max_length=250)
    projects = models.CharField(max_length=250)


    def __str__(self):
        return self.language + ' | ' + self.projects

class ReportCard(models.Model):
    language = models.ForeignKey(Project, on_delete=models.CASCADE)

class LoadFile(models.Model):
    docfile = models.FileField(upload_to='file_load/%Y/%m/%d')

class Upload(models.Model):
    Lddfile = models.FileField(upload_to='Files/%Y/%m/%d')

    def __string__(self):
        return self.Lddfile
