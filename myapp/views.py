from django.shortcuts import render
from bs4 import BeautifulSoup
import requests
from requests.compat import quote_plus

BASE_CRAIGSLIST_URL = 'https://losangeles.craigslist.org/search/?query={}'


def home(request):
    return render(request, 'base.html')


def search(request):
    search_content = request.POST.get('search')
    final_url = BASE_CRAIGSLIST_URL.format(quote_plus(search_content))
    response = requests.get(final_url)
    data = response.text
    context = {
        'search': search_content,
    }
    return render(request, 'my_app/search.html', context)
