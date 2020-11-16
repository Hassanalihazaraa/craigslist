from django.shortcuts import render
from bs4 import BeautifulSoup
import requests


def home(request):
    return render(request, 'base.html')


def search(request):
    search_content = request.POST.get('search')
    context = {
        'search': search_content,
    }
    return render(request, 'my_app/search.html', context)
