# -*- coding: utf-8 -*-
import scrapy
from behold import Behold
import html_text
import durations
from selenium import webdriver
import time

from loguru import logger


URL_20 = "https://www.signalstart.com/search-signals"
URL_1000="https://www.signalstart.com/paging.html?pt=1&sb=48&st=1&ts=705&yieldType=&yieldVal=&drawType=&drawVal=&pipsType=&pipsVal=&type=&ageType=&tradesType=&tradesVal=&priceType=&priceVal=&fifoVal=&searchVal=&serversMultiSearch=&ps=1000&p=1&z=0.410257937140464"

class Provider(scrapy.Item):
    rank = scrapy.Field()
    name = scrapy.Field()
    link = scrapy.Field()
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

        logger.debug("--------------------------------------- Details parse")

        for field, field_processor in fields.items():
            logger.debug(f"     Processing {field}")
            elem = response.xpath(field_processor['xpath'])
            elem_get = elem.get()
            logger.debug(f"Elem get() returned {elem_get}")

            text = html_text.extract_text(elem_get)
            logger.debug(f"Extracted text = {text}")

            _, value = text.split(':')
            logger.debug(f"Parsed value = {value}")

            response.meta["data_row"][field] = value
        yield response.meta["data_row"]

    def parse(self, response):

        exit_parse = False

        print(" >>>>>> URL of the response object is {}".format(response.url))
        self.driver.get(response.url)
        self.driver.find_element_by_xpath("//a[contains(text(),'Gain')]").click()

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

        while True:
            for provider in response.xpath("//div[@class='row']//tr"):
                data_row = Provider()
                Behold().show('provider')
                details_url = None

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
                    if i == 1:  # name
                        details_url = datum.css("a::attr(href)").get()
                        data_row['link'] = details_url
                if details_url:
                    yield scrapy.Request(url=details_url, callback=self.parse_details, meta={'data_row': data_row})

            print("------------------------------- next page logic --------------------------------------")

            def get_page_source():
                page_source = self.driver.page_source
                r = scrapy.http.HtmlResponse('://!', body=page_source, encoding='utf-8')
                print(" >>>> looping self.parse again")
                return r

            time.sleep(10)
            next = self.driver.find_element_by_css_selector('.fa-angle-right')

            if next is not None:
                print(" *** NEXT IS -NOT- NONE: there is another page to navigate to")
                next.click()
                response = get_page_source()
            else:
                if not exit_parse:
                    exit_parse = True
                    response = get_page_source()
                    print(" *** there is not another page to navigate to.. but we need to parse the final page")
                else:
                    print(" *** Now we shall exit!")
                    break


        # next_page = response.css('.fa-angle-right').get()
        # if next_page is not None:
        #     yield response.follow(next_page, self.parse)