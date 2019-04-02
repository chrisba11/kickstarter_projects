from django.shortcuts import render, get_list_or_404, get_object_or_404
from django.http import HttpResponse
from django.shortcuts import render
from .models import Project

# Create your views here.

def project_list_view(request):
    projects = get_list_or_404(Project)
    context ={
        'projects': projects[:10],
    }
    return render(request, 'projects/project_list.html', context)
