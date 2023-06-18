import requests
from bs4 import BeautifulSoup
from datetime import datetime
import time
import json

def get_first_news():
    headers = {
        "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36"
}
    url = 'https://honoraryreporters.korea.net/board/main.do?articlecate=1&tpln=5'
    r = requests.get(url = url, headers = headers)
    soup = BeautifulSoup(r.text, 'lxml')
    articles_cards = soup.find_all('div', class_= 'gl_b')

    news_dict = {}
    for article in articles_cards:
        article_title = article.find('a', class_= 'ff_nsf gl_title').text.strip()
        article_url = f'https://honoraryreporters.korea.net{article.a.get("href")}'
        article_time = article.find('span', class_ = 's_text_14 tc_666666 mg_t8').text.strip()
        """date_from_iso = datetime.fromisoformat(article_time)
        date_time = datetime.strftime(date_from_iso, "%Y-%m-%d %H:%M:%S")
        article_date_timestamp = time.mktime(datetime.strptime(date_time, "%Y-%m-%d %H:%M:%S").timeuple())"""

        article_id = article_url.split('/')[-1]
        article_id = article_id[33:-7]

        #print(f"{article_title}/ {article_url} / {article_time}")

        news_dict[article_id] = {
            'article_time':article_time,
            'article_title':article_title,
            'article_url': article_url,
        }

        with open('/Users/alenaagafonova/PycharmProjects/?Korean/parser/news_dict.json', 'w') as file:
            json.dump(news_dict, file, indent =4, ensure_ascii=False)

def check_news_updates():
    with open('/Users/alenaagafonova/PycharmProjects/?Korean/parser/news_dict.json') as file:
        news_dict = json.load(file)
    headers = {
        "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36"
    }
    url = 'https://honoraryreporters.korea.net/board/main.do?articlecate=1&tpln=5'
    r = requests.get(url=url, headers=headers)
    soup = BeautifulSoup(r.text, 'lxml')
    articles_cards = soup.find_all('div', class_='gl_b')

    fresh_news={}
    for article in articles_cards:
        article_url = f'https://honoraryreporters.korea.net{article.a.get("href")}'
        article_id = article_url.split('/')[-1]
        article_id = article_id[33:-7]

        if article_id in news_dict:
            continue
        else:
            article_title = article.find('a', class_='ff_nsf gl_title').text.strip()
            article_url = f'https://honoraryreporters.korea.net{article.a.get("href")}'
            article_time = article.find('span', class_='s_text_14 tc_666666 mg_t8').text.strip()

        news_dict[article_id] = {
            'article_time': article_time,
            'article_title': article_title,
            'article_url': article_url
        }

        fresh_news[article_id] = {
            'article_time': article_time,
            'article_title': article_title,
            'article_url': article_url
        }

    with open('/Users/alenaagafonova/PycharmProjects/?Korean/parser/news_dict.json', 'w') as file:
        json.dump(news_dict, file, indent=4, ensure_ascii=False)

    return fresh_news

def main():
    get_first_news()

if __name__ == '__main__':
    main()