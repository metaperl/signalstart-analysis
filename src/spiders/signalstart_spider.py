import scrapy
from behold import Behold
import html_text


class SignalStartSpider(scrapy.Spider):
    name = 'signalstart'
    start_urls = [
        'https://www.signalstart.com/search-signals',
    ]

    def parse(self, response):

        cols = "rank name gain pips drawdown trades type monthly chart price age added action"

        skip = [7, 8]

        td = dict()
        for i, col in enumerate(cols.split()):
            td[i] = col

        print("about to behold td...")
        Behold().show('td')

        for provider in response.xpath("//div[@class='row']//tr"):
            data_row = dict()
            Behold().show('provider')
            for i, datum in enumerate(provider.xpath('td')):
                print("showing i and datum..")
                Behold().show('i', 'datum')
                # if i in skip:
                #     pass
                data_row[td[i]] = html_text.extract_text(datum.get())
                # Behold().show('datum')
            yield data_row



            # yield {
            #     'rank': provider.xpath('td[1]/text()').get(),
            #     'name': provider.xpath('td[2]/text()').get(),
            # }

        # next_page = response.css('.fa-angle-right').get()
        # if next_page is not None:
        #     yield response.follow(next_page, self.parse)