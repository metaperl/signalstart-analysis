# -*- coding: utf-8 -*-
import scrapy
from behold import Behold
import html_text
import durations
from scrapy.utils.log import configure_logging
from selenium import webdriver
from selenium.webdriver.common.by import By
import chromedriver_autoinstaller
import time
import re

from loguru import logger

configure_logging({'LOG_LEVEL': 'ERROR'})

URL = "https://www.signalstart.com/search-signals"

chromedriver_autoinstaller.install()


class Provider(scrapy.Item):
    rank = scrapy.Field()
    name = scrapy.Field()
    link = scrapy.Field()
    gain = scrapy.Field()
    pips = scrapy.Field()
    drawdown = scrapy.Field()
    trades = scrapy.Field()
    price = scrapy.Field()
    age = scrapy.Field()
    # added = scrapy.Field()
    balance = scrapy.Field()
    expectancy = scrapy.Field()
    lots = scrapy.Field()
    won = scrapy.Field()
    profit_factor = scrapy.Field()
    daily = scrapy.Field()
    monthly = scrapy.Field()
    currency = scrapy.Field()  # added currency
    profit = scrapy.Field()
    leverage = scrapy.Field()


def infinite_loop():
    while True:
        pass


def extract_number(text: str) -> float:
    """
    Extracts and return the number from a given text string, removing non-numeric characters.
    Used for cleaning balance and profit fields.
    """
    number_str = re.search("[+-]?", text).group()+re.search("[0-9.]+", text).group()
    return float(number_str)


class SignalStartSpider(scrapy.Spider):
    page = 1

    name = "signalstart"
    start_urls = [URL]

    def __init__(self):
        self.driver = webdriver.Chrome()

    def parse_details(self, response):
        # Example page: https://www.signalstart.com/analysis/scalex/271455

        class Details(scrapy.Item):
            xpath = scrapy.Field()
            extractor = scrapy.Field()

        fields = {
            "expectancy": Details(),
            "lots": Details(),
            "balance": Details(),
            "won": Details(),
            "profit_factor": Details(),
            "daily": Details(),
            "monthly": Details(),
            "currency": Details(),  # added currency to fields
            "profit": Details(),
            "leverage": Details(),
        }

        fields["lots"]["xpath"] = "//li[contains(text(),'Lots')]"
        fields["balance"]["xpath"] = "//li[contains(text(),'Balance')]"
        fields["expectancy"]["xpath"] = "//li[span[contains(text(),'Expectancy')]]"
        fields["won"]["xpath"] = "//li[contains(text(),'Won:')]"
        fields["profit_factor"]["xpath"] = "//li[@class='list-group-item popovers']"
        fields["daily"][
            "xpath"
        ] = "//body//div[@class='row']//div[@class='row']//div[3]//ul[1]//li[2]"
        fields["monthly"][
            "xpath"
        ] = "//body//div[@class='row']//div[@class='row']//div[3]//ul[1]//li[3]"

        # Updated xpaths:
        fields["profit"][
            "xpath"
        ] = "//body/div[2]/div[2]/div/div[2]/div/span/div[1]/div[3]/button/div[2]/div[1]"
        fields["leverage"][
            "xpath"
        ] = "//div[contains(@class, 'caption-helper font-blue-sharp bold master-description-container')]"

        # added currency xpath, same as leverage - both are located on the same line
        fields["currency"][
            "xpath"
        ] = "//div[contains(@class, 'caption-helper font-blue-sharp bold master-description-container')]"

        # logger.debug("--------------------------------------- Details parse")

        for field, field_processor in fields.items():
            # logger.debug(f"     Processing {field}")
            elem = response.xpath(field_processor["xpath"])
            elem_get = elem.get()
            # logger.debug(f"Elem get() returned {elem_get}")

            text = html_text.extract_text(elem_get)
            # logger.debug(f"Extracted text = {text}")

            # Parsing text to get values based on format of fields
            if field == "expectancy":
                value = re.search(r"([+-]?\d+)\s+[Pp]ips", text).group(1)
            elif field == "leverage":
                value = text.split(",")[4].split(":")[1]
            elif field == "currency":
                value = text.split(",")[2].strip()
            elif field == "profit":
                value = extract_number(text)
            elif field == "balance":
                value = extract_number(text.split()[1])
            else:
                _, value = text.split(":")
            # logger.debug(f"Parsed value = {value}")
            response.meta["data_row"][field] = value
        yield response.meta["data_row"]

    def parse(self, response):
        print(" >>>>>> URL of the response object is {}".format(response.url))
        self.driver.get(response.url)
        # Do 100 at a time:
        self.driver.find_element(
            By.XPATH,
            value="/html/body/div[3]/div/div/div[2]/div/div[2]/div[3]/div[2]/div[1]/label/select/option[5]",
        ).click()

        #       0    1    2    3    4        5      6       7     8     9   10    11
        cols = (
            "rank name gain pips drawdown trades monthly chart price age added action"
        )

        skip = [6, 7, 10, 11]  # skip monthly, chart, added, action

        def age_to_months(t):
            # logger.debug(f"age_to_months on {t=}")
            t = t.replace("m", "M")
            d = durations.Duration(t)
            return d.to_months()

        postprocess = {"age": lambda t: age_to_months(t)}

        td = dict()
        for i, col in enumerate(cols.split()):
            td[i] = col

        # Behold().show('td')

        # Extracting code for processing providers into function
        def process_providers(response):
            for provider in response.xpath("//div[@class='row']//tr"):
                data_row = Provider()
                details_url = None

                for i, datum in enumerate(provider.xpath("td")):
                    if i in skip:
                        continue
                    text = html_text.extract_text(datum.get())
                    column_name = td[i]
                    if column_name in postprocess:
                        text = postprocess[column_name](text)
                    data_row[column_name] = text
                    if i == 1:  # name
                        details_url = datum.css("a::attr(href)").get()
                        data_row["link"] = details_url
                if details_url:
                    yield scrapy.Request(
                        url=details_url,
                        callback=self.parse_details,
                        meta={"data_row": data_row}
                    )
                    # print("Processing page: " + details_url)

        while True:
            yield from process_providers(response)
            time.sleep(5)
            try:
                # Go to next page if next button is not disabled
                next_button = self.driver.find_element(by=By.CSS_SELECTOR, value="a.btn.btn-sm.default.next")
                response = scrapy.http.HtmlResponse("://!", body=self.driver.page_source, encoding="utf-8")
                if "disabled" in next_button.get_attribute("class"):
                    print("Reached last page.")
                    yield from process_providers(response)
                    break
                next_button.click()
                print("Next page...")
            except Exception as e:
                break
