from django.shortcuts import render, get_list_or_404, get_object_or_404
from django.core.cache.backends.base import DEFAULT_TIMEOUT
from django.views.decorators.cache import cache_page
from django.core.paginator import Paginator
from django.conf import settings
from .models import Project


CACHE_TTL = getattr(settings, 'CACHE_TTL', DEFAULT_TIMEOUT)


@cache_page(CACHE_TTL)
def project_list_view(request):
    project_list = get_list_or_404(Project, id__lte=100)
    paginator = Paginator(project_list, 20)

    page = request.GET.get('page')
    projects = paginator.get_page(page)

    context = {
        'projects': projects,
    }
    return render(request, 'projects/project_list.html', context)
