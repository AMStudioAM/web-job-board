from django.shortcuts import render
from .models import Application, Job
from django.core.paginator import Paginator
from .form import Application, ApplicationForm
from .form import AddJob, Job

# Create your views here.

def job_list(request):
    job_list = Job.objects.all() # return all jobs in the site 

    paginator = Paginator(job_list, 2) # Show 2 contacts per page.
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {"jobs": page_obj} # template name 
    return render(request, 'job/job_list.html', context)

def job_detail(request , slug):
    job_detail = Job.objects.get(slug=slug)
    if request.method == 'POST':
        form = ApplicationForm(request.POST, request.FILES)
        if form.is_valid():
            myform = form.save(commit=False)
            myform.job = job_detail
            myform.save()
    else:
        form = ApplicationForm()
    context = {"job": job_detail, 'form' :form}
    return render(request, "job/job_detail.html", context)

def add(request):
    if request.method == 'POST':
        form = AddJob(request.POST, request.FILES)
        if form.is_valid():
            myform = form.save(commit=False)
            myform.job= add 
            myform.save()
            form = AddJob()
    else:
        form= AddJob()
    context = {"job": add, 'form': form}
    return render(request, "job/add.html", context)

