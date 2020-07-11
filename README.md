# webscraper
A beginner scrapy project.

The spider [articl.py](ogscraper/articlescrape/spiders/articl.py) retrieves the URLs of all the articles from altnews.in and stores them in a file ([urls.txt](ogscraper/articlescrape/spiders/urls.txt))
Then the spider [artcraper.py](altscrape/altscrape/spiders/artscraper.py ) retrieves the data from all the given articles.

## Running
'''
cd ogscraper/articlescrape/spiders
scrapy crawl articl
cp urls.txt  ../../../altscrape/altscrape/spiders/
cd ../../../altscrape/altscrape/spiders
scrapy crawl artscraper -o articles.csv
'''
