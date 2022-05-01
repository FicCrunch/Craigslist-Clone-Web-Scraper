from django.shortcuts import render
import requests
from bs4 import BeautifulSoup
from requests.compat import quote_plus
from . import models

BASE_URL = 'https://stockx.com/search?s={}'
Another_URL = 'https://www.icebox.com/search-products?keyword={}'

# Create your views here.
def home(request):
    return render(request, "base.html")


def new_search(request):
    search = request.POST.get('search')
    models.Search.objects.create(search=search)
    print(quote_plus(search))
    final_url = BASE_URL.format(quote_plus(search))
    print(final_url)
    response = requests.get('https://stockx.com/nike-air-force-1-low-supreme-box-logo-black')
    data = response.text
    # print(data)
    stuff_for_frontend = {
        'search': search
    }
    return render(request, "my_app/new_search.html", stuff_for_frontend)
