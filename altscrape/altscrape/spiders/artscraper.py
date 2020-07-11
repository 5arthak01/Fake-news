import scrapy
import csv
from ..items import AltscrapeItem

class ArtscraperSpider(scrapy.Spider):
    name = 'artscraper'
    allowed_domains = ['altnews.in']
    start_urls = []

    with open('urls.txt', 'r', encoding='utf8') as file:
        urls = file.readlines()

    start_urls = [url[:-1] for url in urls]

    """
    with open("urls.csv", 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            start_urls.append(row[0])
    """

    def parse(self, response):
        title = response.css("header.entry-header h1.entry-title::text").getall()
        author = response.css("span.vcard.author span.fn a::text").getall()
        date = response.css("span.updated::text").getall() 
        content = response.css("p::text").getall() 

        items = AltscrapeItem()

        items['title'] = title
        items['author'] = author
        items['date'] = date
        items['content'] = content

        yield items
