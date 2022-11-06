import requests
from bs4 import BeautifulSoup
import string
import os

number_of_pages = int(input('Number of pages: '))
type_of_article = input('Type of the article: ')

for page_number in range(1, number_of_pages+1):
    path = os.path.join(os.getcwd(), 'Page_{}'.format(page_number))
    os.mkdir(path)
    url = 'https://www.nature.com/nature/articles?sort=PubDate&year=2020&page={}'.format(page_number)
    articles_url = 'https://www.nature.com'
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    articles_type = soup.find_all('span', {'class': 'c-meta__type'})
    for article_type in articles_type:
        if article_type.text == type_of_article:
            article = article_type.find_parent('article').find('a', {'class': 'c-card__link u-link-inherit'})
            article_title = article.text
            article_url = article.get('href')
            article_res = requests.get(articles_url + article_url)
            article_soup = BeautifulSoup(article_res.content, 'html.parser')
            article_text = bytes(article_soup.find('div', {'class': 'c-article-body main-content'}).text.strip(), 'utf-8')
            file_title = article_title.strip()
            for c in string.punctuation:
                file_title = file_title.replace(c, '')
            file_title = file_title.replace(' ', '_') + '.txt'
            file = open(os.path.join(path, file_title), 'wb')
            file.write(article_text)
            file.close()
