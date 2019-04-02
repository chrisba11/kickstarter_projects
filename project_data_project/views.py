from django.shortcuts import render


def home_page(request):
    return render(request, 'generic/home.html', context={'message': 'Hello world'})
