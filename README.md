# Trends in Indian Fake news
A study of all [AltNews](https://www.altnews.in/) articles. 

## Data collection
Utilises scrapy.

The spider [articl.py](ogscraper/articlescrape/spiders/articl.py) retrieves the URLs of all the articles from altnews.in and stores them in a file ([urls.txt](ogscraper/articlescrape/spiders/urls.txt))

Next, the spider [artcraper.py](altscrape/altscrape/spiders/artscraper.py ) retrieves the data from all the given articles.

#### Scraping
```
cd ogscraper/articlescrape/spiders
scrapy crawl articl
cp urls.txt  ../../../altscrape/altscrape/spiders/
cd ../../../altscrape/altscrape/spiders
scrapy crawl artscraper -o articles.csv
```

## Data wrangling and processing
Utilises NLTK.

This is done in [Process.ipynb](Process.ipynb).
