import scrapy
from behold import Behold


class SignalStartSpider(scrapy.Spider):
    name = 'signalstart'
    start_urls = [
        'https://www.signalstart.com/search-signals',
    ]

    def parse(self, response):

        cols = "rank name gain pips drawdown trades type monthly chart price age added action"

        skip = [9,13]

        td = dict()
        for i, col in enumerate(cols.split()):
            td[i] = col

        Behold().show('td')

        for provider in response.xpath("//div[@class='row']//tr"):
            data_row = dict()
            for i, datum in enumerate(provider.xpath('td/text()')):
                if i in skip:
                    continue
                data_row[td[i]] = datum.get()
                # Behold().show('datum')
            yield data_row

            # yield {
            #     'rank': provider.xpath('td[1]/text()').get(),
            #     'name': provider.xpath('td[2]/text()').get(),
            # }

        # next_page = response.css('.fa-angle-right').get()
        # if next_page is not None:
        #     yield response.follow(next_page, self.parse)