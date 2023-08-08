# web_scraper/views.py
from django.shortcuts import render
from .scraper import scrape_articles

def scrape_view(request):
    url = 'https://visualstudio.microsoft.com/visual-cpp-build-tools/'  # Replace this with the URL of the news website you want to scrape
    articles = scrape_articles(url)
    return render(request, 'index.html', {'articles': articles})
