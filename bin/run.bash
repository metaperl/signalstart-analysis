#!/usr/bin/bash -x

cd signalstart
rm data.csv
scrapy crawl signalstart -o data.csv
wc -l data.csv
cp data.csv ../docs/data

git add ../docs/data
git commit -a -m 'scrape run'
git push
