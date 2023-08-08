# web_scraper/scraper.py
import requests
from bs4 import BeautifulSoup

def scrape_articles(url):
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        articles = []
        article_blocks = soup.find_all('div', class_='article-content')  # Assuming article content is wrapped in <div> tags with class 'article-content'
        
        for block in article_blocks:
            title = block.find('h2', class_='article-title').text.strip()  # Assuming article titles are wrapped in <h2> tags with class 'article-title'
            content = block.find('p', class_='article-content-body').text.strip()  # Assuming article content is wrapped in <p> tags with class 'article-content-body'
            articles.append({'title': title, 'content': content})
        
        return articles
    return []
