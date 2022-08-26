from collections import Counter
from operator import itemgetter
import operator
from tech_news.database import find_news


# Requisito 10
def top_5_news():
    all_news = find_news()
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
    all_news = find_news()

    all_news_list = []

    for news in all_news:
        all_news_list.append(news['category'])

    categories_list = Counter(all_news_list).most_common()

    top_categories_by_name = sorted(categories_list, key=itemgetter(0))

    categories_dict = dict((x, y) for x, y in top_categories_by_name)

    top_categories_by_show = sorted(
        categories_dict.items(), key=operator.itemgetter(1), reverse=True)

    top_five_categories = []
    for category in top_categories_by_show:
        top_five_categories.append(category[0])

    return top_five_categories
