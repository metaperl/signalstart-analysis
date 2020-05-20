# signalstart-analysis
Scrape the data for the forex signal providers at
www.SignalStart.com and provide data for 
deeper analysis of provider results.

In a hurry [feast your eyes](https://metaperl.github.io/signalstart-analysis/)
on the results.

## Synopsis of Problem

The [sortable, searchable list of forex signal providers provided by SignalStart](https://www.signalstart.com/search-signals) 
is nice, but it suffers from a few defects:

### No ability to search/sort by details of trader

While you can search and sort for a signal based on the information
provided in the summary table, when you click on the trader, there
are a number of other statistics (e.g. profit-factor, monthly profit) 
that are not available in their search table. It is available here.

### No CSV available for all traders
That's why I wrote this web scraper. You can obtain a CSV by running 
this scraper or [grabbing this file](https://github.com/metaperl/signalstart-analysis/blob/master/docs/data/data.csv).
I asked them for a downloadable CSV and am in dialog with them
about it.

### No composite calculations available
The stats for a trader show their absolute gain, but not their
gain per months of trading. This is easy to do in a spreadsheet.

### Spurious "age" parameter

If you sort the [ list of forex signal providers provided by SignalStart](https://www.signalstart.com/search-signals) 
by age, you will that some signals are purportedly 50 years old but when you
go to the details of that trader, you only see a month or two of trade results.
This has been reported to them.

# Installation

```shell
cd signalstart-analysis
pip install -r requirements.txt
```


# Usage

```shell
cd signalstart-analysis/signalstart
scrapy crawl signalstart -o data.csv
cp data.csv ../docs/data
```

or simply

```shell
cd signalstart-analysis # NO NEED TO CD DOWN FURTHER!!!
./bin/run.sh
```

## Visualization

Upload data.csv to Google Sheets and analyze. 

### Or push to github 

In concert with https://github.com/derekeder/csv-to-html-table
I simply render my latest CSV on github:
https://metaperl.github.io/signalstart-analysis/

My `docs` folder was created via:

    $ git clone git@github.com:derekeder/csv-to-html-table.git docs
    
and then I simply set it up as documented [there](https://github.com/derekeder/csv-to-html-table).


# Discussion

* http://mymoneymagick.com/investing/advanced-analysis-of-signalstart-forex-signal-providers/
* https://www.reddit.com/r/scrapy/comments/ghjygm/success_clicking_ajax_pagination_links/

# Bugs

For some reason, I never seem to iterate through all the pages
of the providers. I think I'm getting a stale element error or
something.

That's why I sort by `gain` before scraping results - I really
dont need traders with very poor performance in my analysis.

But ideally, I would get them all before my scraper barfs. Patches welcome!
