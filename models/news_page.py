import requests
from bs4 import BeautifulSoup
from collections import Counter
import re

class NewsPage:
    """
    A class for retrieving and parsing a web page.

    This class loads a web page from a given link, parses it using BeautifulSoup.
    Counts the number of words and prints the top 10 words.
    Counts the number of tags and prints the top 5.
    And counts the number of links and images.

    Attributes:
        url (string): URL of the web page.
        html (string / None): HTML of the web page.
        soup (BeautifulSoup / None): Parsed HTML object.
        text (string): Text of the web page.
    """
    def __init__(self, url):
        self.url = url
        self.html = None
        self.soup = None
        self.text = ""

    def get_html(self):
        """
        Sends an HTTP GET request to retrieve the HTML content of the page.
        """
        response = requests.get(self.url)

        if response.status_code == 200:
            self.html = response.text
            print("The page was successfully retrieved.")
        else:
            print("Error. The page was not retrieved.")
            exit(1)

    def parsing(self):
        """
        Parses the downloaded HTML content using BeautifulSoup.
        """
        self.soup = BeautifulSoup(self.html, "html.parser")
        self.text = self.soup.get_text()

    def count_words(self):
        """
        Cleans the extracted text and calculates word frequency.
        """
        clean_text = re.sub(r"[^a-zA-Za-яА-ЯіїєґІЇЄҐ0-9\s]", "", self.text)
        clean_text = clean_text.lower()

        words = clean_text.split()

        word_counts = Counter(words)
        print(f'The most common words: {word_counts.most_common(10)}')

    def count_tags(self):
        """
        Counts the frequency of all HTML tags on the page.
        """
        tags = [tag.name for tag in self.soup.findAll()]
        tag_counts = Counter(tags)

        print(f'The most common HTML tags: {tag_counts.most_common(5)}')

    def count_links_images(self):
        """
        Counts the number of links and images on the page.
        """
        all_links = self.soup.find_all('a')
        all_images = self.soup.find_all('img')

        print(f'Number of links: {len(all_links)}')
        print(f'Number of images: {len(all_images)}')

