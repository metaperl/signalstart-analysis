I am attempting to paginate through the data table on [this page](https://www.signalstart.com/search-signals), located below the search form.

My code successfully scrapes the first page and I successfully click the next button (using Selenium) to get the next page of results.

However, attempting to create a `Response` instance and passing it to `self.parse()` does not work:

```python
            page_source = self.driver.page_source
            r = scrapy.http.HtmlResponse('://!', body=page_source, encoding='utf-8')
            print(" >>>> calling self.parse again")
            return self.parse(r)
```

Also, even though if you analyze the call stack, I am returning `None` from `self.parse`, I get this warning when running this scrapy spider:

>  The "SignalStartSpider.parse" method is a generator and includes a "return" statement with a value different than None. This could lead to unexpected behaviour. Please see https://docs.python.org/3/reference/simple_stmts.html#the-return-statement for details about the semantics of the "return" statement within generators
  warn_on_generator_with_return_value(spider, callback)

Here is my current source code:

```python
# -*- coding: utf-8 -*-
import scrapy
from behold import Behold
import html_text
import durations
from selenium import webdriver


URL_20 = "https://www.signalstart.com/search-signals"
URL_1000="https://www.signalstart.com/paging.html?pt=1&sb=48&st=1&ts=705&yieldType=&yieldVal=&drawType=&drawVal=&pipsType=&pipsVal=&type=&ageType=&tradesType=&tradesVal=&priceType=&priceVal=&fifoVal=&searchVal=&serversMultiSearch=&ps=1000&p=1&z=0.410257937140464"

class Provider(scrapy.Item):
    rank = scrapy.Field()
    name = scrapy.Field()
    gain = scrapy.Field()
    pips = scrapy.Field()
    drawdown = scrapy.Field()
    trades = scrapy.Field()
    type = scrapy.Field()
    monthly = scrapy.Field()
    # chart = scrapy.Field()
    price = scrapy.Field()
    age = scrapy.Field()
    # added = scrapy.Field()
    # action = scrapy.Field()
    won = scrapy.Field()
    profit_factor = scrapy.Field()
    daily = scrapy.Field()
    monthly = scrapy.Field()

def raw_page_url(i=1):
    """
    Return raw page of 100 results. There are 8 such pages
    :param i: which page number
    :return:
    """
    return "https://www.signalstart.com/paging.html?pt=1&sb=48&st=1&ts=705&yieldType=&yieldVal=&drawType=&drawVal=&pipsType=&pipsVal=&type=&ageType=&tradesType=&tradesVal=&priceType=&priceVal=&fifoVal=&searchVal=&serversMultiSearch=&ps=100&p={}&z=0.024967722664414493".format(i)

class SignalStartSpider(scrapy.Spider):

    page = 1

    name = 'signalstart'
    start_urls = [
        # raw_page_url(page),
        URL_20
    ]

    def __init__(self):
        #self.driver = webdriver.Firefox(executable_path = r'C:\Users\terre\AppData\Local\Taurus\bin\geckodriver.exe')
        self.driver = webdriver.Firefox(executable_path=r'/cygdrive/c/Users/terre/AppData/Local/Taurus/bin/geckodriver.exe')

    def parse_details(self, response):

        class Details(scrapy.Item):
            xpath = scrapy.Field()
            extractor = scrapy.Field() # I thought different fields would be extracted differently. But turns out they dont.

        fields = {
            'won': Details(),
            'profit_factor': Details(),
            'daily': Details(),
            'monthly': Details()
        }

        fields['won']['xpath'] = "//li[contains(text(),'Won:')]"
        fields['profit_factor']['xpath'] = "//li[@class='list-group-item popovers']"
        fields['daily']['xpath'] = "//li[contains(text(),'Daily:')]"
        fields['monthly']['xpath'] = "//li[contains(text(),'Monthly:')]"

        for field, field_processor in fields.items():
            print(f"     Process {field}")
            elem = response.xpath(field_processor['xpath'])
            _, value = html_text.extract_text(elem.get()).split(':')
            response.meta["data_row"][field] = value
        yield response.meta["data_row"]

    def parse(self, response):

        print(" >>>>>> URL of the response object is {}".format(response.url))
        if len (response.url) > 10:
            self.driver.get(response.url)

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
            data_row = Provider()
            Behold().show('provider')
            details_url = None

            for i, datum in enumerate(provider.xpath('td')):
                Behold().show('i', 'datum')
                if i == 1: # name
                    details_url = datum.css("a::attr(href)").get()
                if i in skip:
                    print(".....skipping")
                    continue
                text = html_text.extract_text(datum.get())
                column_name = td[i]
                if column_name in postprocess:
                    text = postprocess[column_name](text)
                data_row[column_name] = text
            if details_url:
                yield scrapy.Request(url=details_url, callback=self.parse_details, meta={'data_row': data_row})

        print("------------------------------- next page logic --------------------------------------")

        next = self.driver.find_element_by_css_selector('.fa-angle-right')
        if next is not None:
            print(" **** NEXT IS -NOT- NONE")
            next.click()
            page_source = self.driver.page_source
            r = scrapy.http.HtmlResponse('://!', body=page_source, encoding='utf-8')
            print(" >>>> calling self.parse again")
            return self.parse(r)
        else:
            print(" **** NEXT IS NONE")
            return None

        # next_page = response.css('.fa-angle-right').get()
        # if next_page is not None:
        #     yield response.follow(next_page, self.parse)
```