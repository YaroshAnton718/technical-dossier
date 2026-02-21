from models.news_page import NewsPage

def main():
    """
    The main function hat runs the news page analysis.
    """
    url = "https://tsn.ua"
    news_page = NewsPage(url)

    news_page.get_html()

    news_page.parsing()

    news_page.count_words()

    news_page.count_tags()

    news_page.count_links_images()

if __name__ == '__main__':
    main()