I am trying to parse the data table at [this](https://www.signalstart.com/search-signals) page. 

The second column in the table, `Name`, has a link in it with further data on that row.

I want to click on that link and add more data to `data_row`, a dictionary where each key points to the value for a `<td>` cell in that row.

My [code for iterating over the rows of the data table](https://github.com/metaperl/signalstart-analysis/blob/master/src/spiders/signalstart_spider.py#L34) works just fine. 

But I need to enhance it to click the link, parse some fields on the details page for that data row and then go back to the previous page, `yield` the `data_row` and then continue iteration with the next row.

# Answered 
https://stackoverflow.com/questions/61705231/how-to-click-a-link-in-scrapy-parse-some-data-on-the-new-page-and-then-return-t
https://docs.scrapy.org/en/latest/topics/request-response.html#topics-request-response-ref-request-callback-arguments
