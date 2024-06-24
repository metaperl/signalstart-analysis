cd %~dp0
cd signalstart
scrapy crawl signalstart -o data.csv
copy data.csv ..\docs\data
