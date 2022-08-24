import parsel
import time
import requests


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
    # if next_page is None:
    #     return None
    # else:
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
    """Seu código deve vir aqui"""
