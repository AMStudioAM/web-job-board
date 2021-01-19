from django.db import models
from django.db.models.fields import CharField, SlugField
from django.db.models.fields.related import ForeignKey
from django.utils.text import slugify

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
    # location we will use external libs for this variable 
    job_type = models.CharField(max_length=15, choices=JOB_TYPE) 
    description = models.TextField(max_length=1000)
    published_at = models.DateTimeField(auto_now=True)
    Vacancy = models.IntegerField(default=1)
    salary = models.IntegerField(default=0)
    category = ForeignKey('Category', models.CASCADE)
    experience = models.IntegerField(default=1)
    image = models.ImageField(upload_to=image_upload)

    slug = SlugField(blank=True, null=True, allow_unicode=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)


    def __str__(self):
        return self.title

class Category(models.Model):
    name = models.CharField(max_length=25)

    def __str__(self):
        return self.name


class Application(models.Model):
    job = ForeignKey(Job, related_name='apply_job', on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=100)
    website = models.URLField()
    cv = models.FileField(upload_to='Application CV/')
    cover_letter = models.TextField(max_length=500)
    created_at = models.DateTimeField(auto_now=True)

    def __str__(self): # this is function as we call this function, it will return the name of the user who apply in this job
        return f"{self.name} - {self.email} - {self.job}"