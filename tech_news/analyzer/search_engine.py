from tech_news.database import search_news


# Requisito 6
def search_by_title(title):

    search_result = search_news({"title": {"$regex": title, "$options": "i"}})

    news_list = []

    for result in search_result:
        news_list.append((result['title'], result['url']))

    return news_list


# Requisito 7
def search_by_date(date):
    """Seu código deve vir aqui"""


# Requisito 8
def search_by_tag(tag):
    """Seu código deve vir aqui"""


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""
