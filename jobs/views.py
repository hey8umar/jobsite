from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

jobs = {
    "first thing": "make me a website",
    "second": "make this",
    "third": "an actual job",
    "fourth": "just a job",
    "fifth": "do you care at this stage?" 
}

def index(request, job):
    try:
        getJob = jobs[job] 
        return HttpResponse("Hello " + getJob)
    except:
        return HttpResponse("job not found")    

