# signalstart-analysis
Scrape www.SignalStart.com and provide data for deeper analysis of providers.

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

## Visualization

Upload data.csv to Google Sheets and analyze. 

### Or push to github 

In concert with https://github.com/derekeder/csv-to-html-table
I simply render there. My `docs` folder was created via:

    $ git clone git@github.com:derekeder/csv-to-html-table.git docs
    
and then I simply set it up as documented there.




# Discussion

* http://mymoneymagick.com/investing/advanced-analysis-of-signalstart-forex-signal-providers/
* https://www.reddit.com/r/scrapy/comments/ghjygm/success_clicking_ajax_pagination_links/
