from django.db import models
from django.db.models.fields.related import ForeignKey

# Create your models here.
'''
django model field:
    - html widget 
    - validation
    - db size 
'''
JOB_TYPE = (
    ("FULL TIME","FULL TIME"),
    ("PART TIME","PART TIME"),
)

def image_upload(instance, filename):
    imagename, extenstion = filename.split(".")
    return "jobs/%s.%s"%(instance.id, extenstion)

class Job(models.Model): # table
    title = models.CharField(max_length=100) # column 
    # location 
    job_type = models.CharField(max_length=15, choices=JOB_TYPE) 
    description = models.TextField(max_length=1000)
    published_at = models.DateTimeField(auto_now=True)
    Vacancy = models.IntegerField(default=1)
    salary = models.IntegerField(default=0)
    category = ForeignKey('Category', models.CASCADE)
    experience = models.IntegerField(default=1)
    image = models.ImageField(upload_to=image_upload)

    def __str__(self):
        return self.title

class Category(models.Model):
    name = models.CharField(max_length=25)

    def __str__(self):
        return self.name