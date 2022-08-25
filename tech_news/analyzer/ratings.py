from tech_news.database import find_news


# Requisito 10
def top_5_news():
    all_news = find_news()
    print(all_news)
    sorted_by_comments_count = sorted(
        all_news, key=lambda k: (-k['comments_count'], k['title']))
    list_news = sorted_by_comments_count[:5]

    top_five = []

    for news in list_news:
        top_five.append((news['title'], news['url']))
    return top_five
    # 'comments_count'


# Requisito 11
def top_5_categories():
    """Seu código deve vir aqui"""
