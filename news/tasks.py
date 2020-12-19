# from ..blog.celery import app
from bs4 import BeautifulSoup
import requests
import lxml
from .models import News
from blog.celery import app


@app.task
def parsing():
    url = 'https://ru.sputnik.kg/news/'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'lxml')
    titles = soup.find_all('h2', class_='b-plainlist__title')[0:1]
    texts = soup.find_all('div', class_='b-plainlist__announce')[0:1]




    for i in range(0, len(titles)):
        x = {'title': titles[i].text, 'text': texts[i].text}
        News.objects.create(**x)

    print('Добавлена статья')


#celery -A blog worker -l info просто запуск задачи
