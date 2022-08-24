import parsel
import time
import requests
from tech_news.database import create_news


# Requisito 1
def fetch(url):
    try:
        response = requests.get(
            url, headers={"user-agent": "Fake user-agent"}, timeout=3
        )
        response.raise_for_status()
        time.sleep(1)
    except (requests.HTTPError, requests.ReadTimeout):
        return None
    else:
        return requests.get(url).text


# Requisito 2
def scrape_novidades(html_content):
    selector = parsel.Selector(html_content)
    links = selector.css("a.cs-overlay-link::attr(href)").getall()
    return links


# Requisito 3
def scrape_next_page_link(html_content):
    selector = parsel.Selector(html_content)
    next_page = selector.css("a.next.page-numbers::attr(href)").get()
    return next_page


# Requisito 4
def scrape_noticia(html_content):
    selector = parsel.Selector(html_content)

    url = selector.css("link[rel=canonical]::attr(href)").get()

    title = selector.css(
        ".entry-title::text"
    ).get().strip()

    timestamp = selector.css("li.meta-date::text").get()

    writer = selector.css("a.url.fn.n::text").get()

    comments_preview = selector.css("#comments > h5::text").get()
    if comments_preview is None:
        comments_count = 0
    else:
        comments = comments_preview.split(" ")
        comments_count = int(comments[0])

    summary = selector.xpath(
        "string(//div[@class='entry-content']/p)"
    ).get().strip()

    tags = selector.css(
        "a[rel='tag']::text"
    ).getall()

    category = selector.css(
        "#page > div > div > div > section "
        "> div.entry-header-inner.cs-bg-dark "
        "> div > div > a > span.label::text"
    ).get()

    return ({
        "url": url,
        "title": title,
        "timestamp": timestamp,
        "writer": writer,
        "comments_count": comments_count,
        "summary": summary,
        "tags": tags,
        "category": category,
    })


# Requisito 5
def get_tech_news(amount):

    pages = amount / 12

    base_url = 'https://blog.betrybe.com/'

    main_page = fetch(base_url)

    links_news = scrape_novidades(main_page)

    link_next_page = scrape_next_page_link(main_page)

    all_news_links = links_news

    while pages > 1:
        new_page = fetch(link_next_page)
        all_news_links.extend(scrape_novidades(new_page))
        new_page_link = scrape_next_page_link(new_page)
        link_next_page = new_page_link

        pages -= 1

    news_links_in_use = all_news_links[:amount]

    news_catalog = []

    for links in news_links_in_use:
        new_news = scrape_noticia(fetch(links))
        news_catalog.append(new_news)

    create_news(news_catalog)

    return news_catalog

    # len(all_news_links) < amount
