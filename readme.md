# A Test Scrapy Project

simple Scrapy web crawler to scrape data off of https://codeintheschools.org using BeautifulSoup html parser.

to install the project run
```commandline
git clone https://github.com/kamora101/scrape_proj.git
```

create a virtual environment and activate it
```commandline
python3 -m venv venv
source venv/bin/activate
```
install the required modules
```commandline
pip install -r requirements.txt
```
navigate to the spiders start the CodeWorks spider
```commandline
cd scrapy_proj/scrapy_proj/spiders
scrapy crawl CodeWorks 
```

