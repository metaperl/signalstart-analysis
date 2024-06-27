cd %~dp0\signalstart
scrapy crawl signalstart -O ..\docs\data\data.csv
cd ..
echo "Scrape completed!"
pause
