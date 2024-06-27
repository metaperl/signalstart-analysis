set YEAR=%DATE:~10,4%
set MONTH=%DATE:~4,2%
set DAY=%DATE:~7,2%
set FILENAME=Backup SignalStart data %YEAR%-%MONTH%-%DAY%.csv

cd %~dp0\signalstart
scrapy crawl signalstart -O ..\docs\data\data.csv
copy ..\docs\data\data.csv ..\docs\data\"%FILENAME%"
cd ..
echo "Scrape completed!"
pause
