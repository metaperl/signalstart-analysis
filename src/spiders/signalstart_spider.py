import scrapy
from behold import Behold


class SignalStartSpider(scrapy.Spider):
    name = 'signalstart'
    start_urls = [
        'https://www.signalstart.com/search-signals',
    ]

    def parse(self, response):
        for provider in response.xpath("//div[@class='row']//tr"):

            yield {
                'rank': provider.xpath('td[1]/text()').get(),
                'name': provider.xpath('td[2]/text()').get(),
            }

        # next_page = response.css('.fa-angle-right').get()
        # if next_page is not None:
        #     yield response.follow(next_page, self.parse)