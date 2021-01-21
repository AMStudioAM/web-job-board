from django import forms
from django.forms import models
from .models import Application
from .models import Job

# here is the classes for forms 

class ApplicationForm(forms.ModelForm): # form for apply for jobs
    class Meta:
        model = Application
        fields = ['name', 'email', 'website', 'cv', 'cover_letter']

class AddJob(forms.ModelForm): # form for add new jobs
    class Meta:
        model = Job 
        fields = ["title", "job_type", "description", "Vacancy", "salary", "category", "experience", "image"]