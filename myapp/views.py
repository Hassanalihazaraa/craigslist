from django.shortcuts import render
from bs4 import BeautifulSoup
import requests
from requests.compat import quote_plus
from . import models

BASE_CRAIGSLIST_URL = 'https://losangeles.craigslist.org/search/?query={}'


def home(request):
    return render(request, 'base.html')


def search(request):
    search_content = request.POST.get('search')
    models.Search.objects.create(search=search_content)
    final_url = BASE_CRAIGSLIST_URL.format(quote_plus(search_content))
    response = requests.get(final_url)
    data = response.text
    soup = BeautifulSoup(data, features='html.parser')

    post_listing = soup.find_all('li', {'class': 'result-row'})

    final_posting = []

    for post in post_listing:
        post_title = post.find(class_='result-title').text
        post_url = post.find('a').get('href')
        post_price = post.find(class_='result-price').text
        final_posting.append((post_title, post_url, post_price))

    print(final_posting)
    context = {
        'search': search_content,
        'final_postings': final_posting,
    }
    return render(request, 'my_app/search.html', context)
