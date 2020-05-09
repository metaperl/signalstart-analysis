import scrapy
from behold import Behold
import html_text
import durations


class SignalStartSpider(scrapy.Spider):
    name = 'signalstart'
    start_urls = [
        'https://www.signalstart.com/search-signals',
    ]

    def parse(self, response):

        cols = "rank name gain pips drawdown trades type monthly chart price age added action"

        skip = [7, 8, 11, 12]

        def age_to_months(t):
            t = t.replace('m', 'M')
            d = durations.Duration(t);
            return d.to_months()

        postprocess = {
            'age': lambda t: age_to_months(t)
        }

        td = dict()
        for i, col in enumerate(cols.split()):
            td[i] = col

        Behold().show('td')

        for provider in response.xpath("//div[@class='row']//tr"):
            data_row = dict()
            Behold().show('provider')
            for i, datum in enumerate(provider.xpath('td')):
                Behold().show('i', 'datum')
                if i in skip:
                    print(".....skipping")
                    continue
                text = html_text.extract_text(datum.get())
                column_name = td[i]
                if column_name in postprocess:
                    text = postprocess[column_name](text)
                data_row[column_name] = text
            yield data_row

        # next_page = response.css('.fa-angle-right').get()
        # if next_page is not None:
        #     yield response.follow(next_page, self.parse)