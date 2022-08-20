import scrapy
from scrapy_selenium import SeleniumRequest


class BlogspiderSpider(scrapy.Spider):
    name = 'blogspider'
    allowed_domains = ['www.zyte.com']
    start_urls = ['https://www.zyte.com/blog/']

    def start_requests(self):
        yield SeleniumRequest(
            url ='https://www.zyte.com/blog/',
            wait_time = 3,
            # screenshot = True,
            callback = self.parse, 
            dont_filter = True    
        )

    
    def parse(self, response):
        for title in response.css('.oxy-post-title'):
            yield {'title': title.css('::text').get()}

        for next_page in response.css('a.next'):
            yield response.follow(next_page, self.parse)
