import scrapy
from ..items import ArticlescrapeItem

class ArticlSpider(scrapy.Spider):
    name = 'articl'

    start_urls = ['https://www.altnews.in/']
    
    for page in range(2,248):
        start_urls.append('https://www.altnews.in/page/' + str(page) + '/')

    def parse(self, response):
        urls = response.css("a.herald-read-more::attr(href)").getall()

        with open('urls.txt', 'a', encoding='utf8') as file:
            for url in urls:
                file.write(url + '\n')