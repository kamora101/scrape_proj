import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy_proj.items import CitsItem
from bs4 import BeautifulSoup
from scrapy.linkextractors import LinkExtractor
class CodeITS(CrawlSpider):
    name = "CodeWorks"
    allowed_domains = ['www.codeintheschools.org']
    start_urls = ["https://www.codeintheschools.org/"]
    base_url = 'https://www.codeintheschools.org/'

    rules = [
        Rule(LinkExtractor(allow='/*'), callback="parse_item", follow=True)
    ]

    def parse_item(self, response):
        print(f"Parsing {response.url}")
        #links = response.css("p a")
        soup = BeautifulSoup(response.body, 'html.parser')
        for link in soup.select("p > a"):
            item = CitsItem()
            item["title"] = link.get_text()
            item["url"] = link['href']
            if link.find_previous_sibling('strong') is not None:
                item["author"] = link.find_previous_sibling('strong').get_text()

            yield item #response.follow(item["url"], self.parse_item, cb_kwargs=dict(item=item))
        #next_page - response.css('li.')
    #def parse_page(self, response, item):




