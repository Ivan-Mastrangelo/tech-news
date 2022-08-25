from tech_news.database import search_news
from datetime import datetime


# Requisito 6
def search_by_title(title):

    search_result = search_news({"title": {"$regex": title, "$options": "i"}})

    news_list = []

    for result in search_result:
        news_list.append((result['title'], result['url']))

    return news_list


# Requisito 7
def search_by_date(date):

    try:

        original_date = datetime.strptime(date, '%Y-%m-%d')

        date_formated = datetime.strftime(original_date, '%d/%m/%Y')

        search_result = search_news({"timestamp": date_formated})

        news_list = []

        for result in search_result:
            news_list.append((result['title'], result['url']))

    except ValueError:
        raise ValueError("Data inválida")

    return news_list


# Requisito 8
def search_by_tag(tag):

    search_result = search_news({"tags": {"$regex": tag, "$options": "i"}})

    news_list = []

    for result in search_result:
        news_list.append((result['title'], result['url']))

    return news_list


# Requisito 9
def search_by_category(category):

    search_result = search_news(
        {"category": {"$regex": category, "$options": "i"}}
    )

    news_list = []

    for result in search_result:
        news_list.append((result['title'], result['url']))

    return news_list
