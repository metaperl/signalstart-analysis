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
```

Upload data.csv to Google Sheets and analyze. Or: commit the 
CSV to a github repo and use [Github's automatic CSV rendering](https://help.github.com/en/github/managing-files-in-a-repository/rendering-csv-and-tsv-data) 
to render the CSV.


# Discussion

* http://mymoneymagick.com/investing/advanced-analysis-of-signalstart-forex-signal-providers/
* https://www.reddit.com/r/scrapy/comments/ghjygm/success_clicking_ajax_pagination_links/
