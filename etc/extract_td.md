# Problem extracting td from table row (tr)

Hello, I am parsing the following URL:
https://www.signalstart.com/search-signals

In particular, I am trying to extract the data from the table rows.

The table row has a series of table-data cells:

```html

<table class="table table-striped table-bordered dataTable table-hover" id="searchSignalsTable">
                <thead>
                <tr>
                                                                                                        <th class="sorting sorting_asc"><a href="javascript:void(0)" onclick="sortTable(this,1,48,'searchSignalsData', '&amp;ps=20&amp;ts=706&amp;yieldType=&amp;yieldVal=&amp;drawType=&amp;drawVal=&amp;pipsType=&amp;pipsVal=&amp;type=&amp;ageType=&amp;tradesType=&amp;tradesVal=&amp;priceType=&amp;priceVal=&amp;fifoVal=&amp;searchVal=&amp;serversMultiSearch=', false, true, true, 'Search Signals');" order="0">Rank</a></th>
                                        <th class="sorting "><a href="javascript:void(0)" onclick="sortTable(this,1,3,'searchSignalsData', '&amp;ps=20&amp;ts=706&amp;yieldType=&amp;yieldVal=&amp;drawType=&amp;drawVal=&amp;pipsType=&amp;pipsVal=&amp;type=&amp;ageType=&amp;tradesType=&amp;tradesVal=&amp;priceType=&amp;priceVal=&amp;fifoVal=&amp;searchVal=&amp;serversMultiSearch=', false, true, true, 'Search Signals');" order="0">Name</a></th>
                    <th class="sorting "><a href="javascript:void(0)" onclick="sortTable(this,1,19,'searchSignalsData','&amp;ps=20&amp;ts=706&amp;yieldType=&amp;yieldVal=&amp;drawType=&amp;drawVal=&amp;pipsType=&amp;pipsVal=&amp;type=&amp;ageType=&amp;tradesType=&amp;tradesVal=&amp;priceType=&amp;priceVal=&amp;fifoVal=&amp;searchVal=&amp;serversMultiSearch=', false, true, true, 'Search Signals');" order="0">Gain</a></th>
                    <th class="sorting "><a href="javascript:void(0)" onclick="sortTable(this,1,37,'searchSignalsData','&amp;ps=20&amp;ts=706&amp;yieldType=&amp;yieldVal=&amp;drawType=&amp;drawVal=&amp;pipsType=&amp;pipsVal=&amp;type=&amp;ageType=&amp;tradesType=&amp;tradesVal=&amp;priceType=&amp;priceVal=&amp;fifoVal=&amp;searchVal=&amp;serversMultiSearch=', false, true, true, 'Search Signals');" order="0">Pips</a></th>
                    <th class="sorting "><a href="javascript:void(0)" onclick="sortTable(this,1,23,'searchSignalsData','&amp;ps=20&amp;ts=706&amp;yieldType=&amp;yieldVal=&amp;drawType=&amp;drawVal=&amp;pipsType=&amp;pipsVal=&amp;type=&amp;ageType=&amp;tradesType=&amp;tradesVal=&amp;priceType=&amp;priceVal=&amp;fifoVal=&amp;searchVal=&amp;serversMultiSearch=', false, true, true, 'Search Signals');" order="0">DD</a></th>
                    <th class="sorting "><a href="javascript:void(0)" onclick="sortTable(this,1,100,'searchSignalsData','&amp;ps=20&amp;ts=706&amp;yieldType=&amp;yieldVal=&amp;drawType=&amp;drawVal=&amp;pipsType=&amp;pipsVal=&amp;type=&amp;ageType=&amp;tradesType=&amp;tradesVal=&amp;priceType=&amp;priceVal=&amp;fifoVal=&amp;searchVal=&amp;serversMultiSearch=', false, true, true, 'Search Signals');" order="0">Trades</a></th>
                    <th class="sorting "><a href="javascript:void(0)" onclick="sortTable(this,1,26,'searchSignalsData','&amp;ps=20&amp;ts=706&amp;yieldType=&amp;yieldVal=&amp;drawType=&amp;drawVal=&amp;pipsType=&amp;pipsVal=&amp;type=&amp;ageType=&amp;tradesType=&amp;tradesVal=&amp;priceType=&amp;priceVal=&amp;fifoVal=&amp;searchVal=&amp;serversMultiSearch=', false, true, true, 'Search Signals');" order="0">Type</a></th>
                    <th>Monthly</th>
                    <th>Chart</th>
                    <th class="sorting "><a href="javascript:void(0)" onclick="sortTable(this,1,102,'searchSignalsData','&amp;ps=20&amp;ts=706&amp;yieldType=&amp;yieldVal=&amp;drawType=&amp;drawVal=&amp;pipsType=&amp;pipsVal=&amp;type=&amp;ageType=&amp;tradesType=&amp;tradesVal=&amp;priceType=&amp;priceVal=&amp;fifoVal=&amp;searchVal=&amp;serversMultiSearch=', false, true, true, 'Search Signals');" order="0">Price</a></th>
                    <th class="sorting " style="width: 40px"><a href="javascript:void(0)" onclick="sortTable(this,1,103,'searchSignalsData','&amp;ps=20&amp;ts=706&amp;yieldType=&amp;yieldVal=&amp;drawType=&amp;drawVal=&amp;pipsType=&amp;pipsVal=&amp;type=&amp;ageType=&amp;tradesType=&amp;tradesVal=&amp;priceType=&amp;priceVal=&amp;fifoVal=&amp;searchVal=&amp;serversMultiSearch=', false, true, true, 'Search Signals');" order="0">Age</a></th>
                    <th class="sorting " style="width: 70px"><a href="javascript:void(0)" onclick="sortTable(this,1,1,'searchSignalsData','&amp;ps=20&amp;ts=706&amp;yieldType=&amp;yieldVal=&amp;drawType=&amp;drawVal=&amp;pipsType=&amp;pipsVal=&amp;type=&amp;ageType=&amp;tradesType=&amp;tradesVal=&amp;priceType=&amp;priceVal=&amp;fifoVal=&amp;searchVal=&amp;serversMultiSearch=', false, true, true, 'Search Signals');" order="0">Added</a></th>
                    <th>Action</th>
                </tr>
                </thead>
                <tbody>
                                                                                <tr>
                                                    <td style="text-align: center;">            -    </td>
                                                <td><a class="pointer" target="_blank" href="https://www.signalstart.com/analysis/joker-1k/110059">Joker 1k</a> </td>
                        <td><span class="red">-9.99%</span></td>
                        <td><span class="green">2,092.3</span></td>
                        <td>15.3%</td>
                        <td>108</td>
                        <td>Real</td>
                        <td><span class="monthlySparkline" id="monthlySpark110059"><canvas width="12" height="25" style="display: inline-block; vertical-align: top; width: 12px; height: 25px;"></canvas></span></td>
                        <td><span class="dayliSparkline" id="dayliSpark110059"><canvas width="100" height="25" style="display: inline-block; vertical-align: top; width: 100px; height: 25px;"></canvas></span></td>
                        <td>$30</td>
                        <td>
                                                                                        1m 24d
                                                    </td>
                        <td>
                                                        Mar 29, 2020
                        </td>
                        <td><a onclick="getMasterPricingData('110059');" data-toggle="modal"><button id="subscribeToMasterBtn110059" class="btn btn-circle btn-sm green" type="button">Copy</button></a>
                            <div style="display: none;">
                                <input type="hidden" class="monthlyData" oid="110059" value="-1.78,-3.68,-4.86">
                                <input type="hidden" class="dailyGrowthData" oid="110059" value="0.00,-0.03,-1.78,-5.69,-6.75,-5.59,-7.61,-5.31,-6.20,-3.81,-4.40,-8.00,-2.88,-3.78,-4.38,-0.20,-5.40,-10.66,-13.69,-12.51,-13.23,-9.99">
                                <input type="hidden" class="dailyEquityData" oid="110059" value="0.00,-0.23,-1.41,-5.02,-6.25,-4.29,-6.68,-3.91,-5.37,-4.10,-4.40,-3.59,-1.78,-1.75,-2.65,-0.21,-4.87,-10.76,-13.90,-11.58,-13.23,-10.18">
                            </div>
                        </td>
                    </tr>
                                                                                <tr>
                                                    <td style="text-align: center;">            -    </td>
                                                <td><a class="pointer" target="_blank" href="https://www.signalstart.com/analysis/fxabakus/56043">FXabakus</a> </td>
                        <td><span class="red">-19.57%</span></td>
                        <td><span class="red">-8,615.2</span></td>
                        <td>42%</td>
                        <td>1642</td>
                        <td>Real</td>
                        <td><span class="monthlySparkline" id="monthlySpark56043"><canvas width="80" height="25" style="display: inline-block; vertical-align: top; width: 80px; height: 25px;"></canvas></span></td>
                        <td><span class="dayliSparkline" id="dayliSpark56043"><canvas width="100" height="25" style="display: inline-block; vertical-align: top; width: 100px; height: 25px;"></canvas></span></td>
                        <td>$30</td>
                        <td>
                                                                                        1y 7m
                                                    </td>
                        <td>
                                                        May 4, 2019
                        </td>
                        <td><a onclick="getMasterPricingData('56043');" data-toggle="modal"><button id="subscribeToMasterBtn56043" class="btn btn-circle btn-sm green" type="button">Copy</button></a>
                            <div style="display: none;">
                                <input type="hidden" class="monthlyData" oid="56043" value="1.22,1.35,3.92,1.35,-1.57,1.77,2.01,1.11,0.38,-14.89,-14.70,-5.21,5.97,7.03,-17.54,2.92,3.11,-8.94,13.38,1.77">
                                <input type="hidden" class="dailyGrowthData" oid="56043" value="-27.87,-29.29,-29.01,-26.76,-25.76,-25.59,-30.57,-30.13,-29.78,-29.60,-29.25,-28.34,-28.07,-27.89,-25.20,-25.08,-23.66,-23.46,-21.54,-21.02,-21.62,-20.28,-18.31,-26.97,-27.48,-27.00,-28.21,-24.20,-23.46,-30.04,-31.37,-34.62,-33.84,-32.87,-32.20,-30.99,-30.43,-30.30,-29.75,-27.64,-27.45,-24.34,-24.71,-24.09,-24.15,-21.48,-21.08,-20.97,-19.54,-19.57">
                                <input type="hidden" class="dailyEquityData" oid="56043" value="-27.87,-29.29,-28.89,-26.76,-25.76,-28.10,-34.47,-32.34,-31.54,-40.80,-32.76,-32.90,-33.50,-30.65,-25.37,-25.05,-22.88,-23.29,-21.54,-21.02,-21.54,-20.90,-19.11,-27.76,-35.15,-29.17,-27.79,-24.20,-26.23,-34.32,-35.95,-51.20,-33.84,-32.76,-32.71,-31.62,-30.43,-39.93,-29.75,-27.64,-28.35,-27.62,-28.41,-24.20,-24.51,-22.06,-21.08,-20.97,-18.82,-30.27">
                            </div>
                        </td>
                    </tr>
                                                                                <tr>
                                                    <td style="text-align: center;">            -    </td>
                                                <td><a class="pointer" target="_blank" href="https://www.signalstart.com/analysis/af-investing-pro-final/122603">AF Investing Pro Final</a> </td>
                        <td><span class="green">56.69%</span></td>
                        <td><span class="green">29,812</span></td>
                        <td>8.6%</td>
                        <td>476</td>
                        <td>Real</td>
                        <td><span class="monthlySparkline" id="monthlySpark122603"><canvas width="8" height="25" style="display: inline-block; vertical-align: top; width: 8px; height: 25px;"></canvas></span></td>
                        <td><span class="dayliSparkline" id="dayliSpark122603"><canvas width="100" height="25" style="display: inline-block; vertical-align: top; width: 100px; height: 25px;"></canvas></span></td>
                        <td>$250</td>
                        <td>
                                                                                        17d 12h
                                                    </td>
                        <td>
                                                        Apr 30, 2020
                        </td>
                        <td><a onclick="getMasterPricingData('122603');" data-toggle="modal"><button id="subscribeToMasterBtn122603" class="btn btn-circle btn-sm green" type="button">Copy</button></a>
                            <div style="display: none;">
                                <input type="hidden" class="monthlyData" oid="122603" value="55.18,0.98">
                                <input type="hidden" class="dailyGrowthData" oid="122603" value="-0.02,0.04,54.78,55.02,55.18,55.82,55.86,55.99,56.06,56.25,56.69">
                                <input type="hidden" class="dailyEquityData" oid="122603" value="-8.60,16.85,54.86,54.11,55.44,55.85,54.38,52.15,45.00,51.07,56.25">
                            </div>
                        </td>
                    </tr>
                                                                                <tr>
                                                    <td style="text-align: center;">            -    </td>
                                                <td><a class="pointer" target="_blank" href="https://www.signalstart.com/analysis/rapid-growth/111340">Rapid growth</a> </td>
                        <td><span class="green">130.78%</span></td>
                        <td><span class="green">1,102.9</span></td>
                        <td>44.3%</td>
                        <td>126</td>
                        <td>Real</td>
                        <td><span class="monthlySparkline" id="monthlySpark111340"><canvas width="12" height="25" style="display: inline-block; vertical-align: top; width: 12px; height: 25px;"></canvas></span></td>
                        <td><span class="dayliSparkline" id="dayliSpark111340"><canvas width="100" height="25" style="display: inline-block; vertical-align: top; width: 100px; height: 25px;"></canvas></span></td>
                        <td>$31</td>
                        <td>
                                                                                        2m 8d
                                                    </td>
                        <td>
                                                        Apr 1, 2020
                        </td>
                        <td><a onclick="getMasterPricingData('111340');" data-toggle="modal"><button id="subscribeToMasterBtn111340" class="btn btn-circle btn-sm green" type="button">Copy</button></a>
                            <div style="display: none;">
                                <input type="hidden" class="monthlyData" oid="111340" value="87.85,18.28,3.87">
                                <input type="hidden" class="dailyGrowthData" oid="111340" value="0.00,0.64,1.40,1.40,1.90,2.91,7.53,8.21,11.19,11.30,17.60,19.60,23.03,37.74,47.75,54.75,59.91,69.79,73.60,79.36,87.85,93.14,93.40,94.70,95.93,96.01,99.95,100.71,101.85,102.10,102.12,104.36,108.76,110.11,110.14,110.23,112.58,115.10,115.54,117.17,121.24,122.19,123.40,124.18,124.88,124.89,130.09,130.78">
                                <input type="hidden" class="dailyEquityData" oid="111340" value="-1.80,0.67,0.97,1.91,-0.64,2.58,6.82,6.72,8.65,8.46,16.29,17.71,19.96,34.10,47.24,51.91,59.07,69.79,73.58,79.26,88.01,91.03,93.43,87.85,96.19,95.80,100.29,95.63,98.94,101.71,98.33,104.12,108.26,108.46,86.24,108.42,112.83,114.51,94.42,116.29,120.16,121.93,123.05,115.67,122.81,124.45,130.47,130.14">
                            </div>
                        </td>
                    </tr>
                                                                                <tr>
                                                    <td style="text-align: center;">            -    </td>
                                                <td><a class="pointer" target="_blank" href="https://www.signalstart.com/analysis/dream-presentation-1/66543">Dream Presentation 1</a> </td>
                        <td><span class="red">-99.9%</span></td>
                        <td><span class="red">-2,724.1</span></td>
                        <td>99.9%</td>
                        <td>1612</td>
                        <td>Real</td>
                        <td><span class="monthlySparkline" id="monthlySpark66543"><canvas width="28" height="25" style="display: inline-block; vertical-align: top; width: 28px; height: 25px;"></canvas></span></td>
                        <td><span class="dayliSparkline" id="dayliSpark66543"><canvas width="100" height="25" style="display: inline-block; vertical-align: top; width: 100px; height: 25px;"></canvas></span></td>
                        <td>$30</td>
                        <td>
                                                                                        6m 13d
                                                    </td>
                        <td>
                                                        Nov 8, 2019
                        </td>
                        <td><a onclick="getMasterPricingData('66543');" data-toggle="modal"><button id="subscribeToMasterBtn66543" class="btn btn-circle btn-sm green" type="button">Copy</button></a>
                            <div style="display: none;">
                                <input type="hidden" class="monthlyData" oid="66543" value="-100.14,-98.54,-98.79,-91.71,-98.23,-100.00,-88.82">
                                <input type="hidden" class="dailyGrowthData" oid="66543" value="24.18,-99.90,-99.89,-99.88,-99.88,-99.88,-99.87,-99.87,-99.86,-99.84,-99.83,-99.90,-99.89,-99.90,-99.90,-99.81,-99.81,-99.80,-99.90,-99.90,-99.86,-99.83,-99.79,-99.90,-99.90,-99.90,-99.88,-99.89,-99.89,-99.88,-99.82,-99.74,-99.85,-99.37,-99.88,-99.90,-99.90,-99.90,-99.90,-99.87,-99.83,-99.80,-99.75,-99.64,-99.56,-99.90,-99.90">
                                <input type="hidden" class="dailyEquityData" oid="66543" value="7.87,-99.90,-99.89,-99.88,-99.88,-99.88,-99.88,-99.87,-99.86,-99.84,-99.83,-99.90,-99.89,-99.90,-99.89,-99.83,-99.88,-99.88,-99.90,-99.90,-99.87,-99.83,-99.84,-99.72,-99.90,-99.90,-99.88,-99.89,-99.88,-99.92,-99.86,-99.74,-99.86,-99.39,-99.88,-99.90,-99.90,-99.90,-99.90,-99.87,-99.83,-99.79,-99.76,-99.63,-99.55,-100.16,-99.83">
                            </div>
                        </td>
                    </tr>
                                                                                <tr>
                                                    <td style="text-align: center;">            -    </td>
                                                <td><a class="pointer" target="_blank" href="https://www.signalstart.com/analysis/limerence-ea-suite-3/93679">Limerence EA Suite 3</a> </td>
                        <td><span class="green">1,246.66%</span></td>
                        <td><span class="green">199.8</span></td>
                        <td>34.2%</td>
                        <td>8</td>
                        <td>Real</td>
                        <td><span class="monthlySparkline" id="monthlySpark93679"><canvas width="20" height="25" style="display: inline-block; vertical-align: top; width: 20px; height: 25px;"></canvas></span></td>
                        <td><span class="dayliSparkline" id="dayliSpark93679"><canvas width="100" height="25" style="display: inline-block; vertical-align: top; width: 100px; height: 25px;"></canvas></span></td>
                        <td>$75</td>
                        <td>
                                                                                        7m 11d
                                                    </td>
                        <td>
                                                        Feb 11, 2020
                        </td>
                        <td><a onclick="getMasterPricingData('93679');" data-toggle="modal"><button id="subscribeToMasterBtn93679" class="btn btn-circle btn-sm green" type="button">Copy</button></a>
                            <div style="display: none;">
                                <input type="hidden" class="monthlyData" oid="93679" value="95.40,82.01,94.38,87.49,3.90">
                                <input type="hidden" class="dailyGrowthData" oid="93679" value="0.00,95.40,255.64,591.28,552.49,1234.12,1196.10,1246.66">
                                <input type="hidden" class="dailyEquityData" oid="93679" value="0.00,95.40,255.64,591.28,1034.76,1234.12,1196.10,1246.66">
                            </div>
                        </td>
                    </tr>
                                                                                <tr>
                                                    <td style="text-align: center;">            -    </td>
                                                <td><a class="pointer" target="_blank" href="https://www.signalstart.com/analysis/easy-money/31727">Easy Money</a> </td>
                        <td><span class="red">-99.9%</span></td>
                        <td><span class="green">2,430.6</span></td>
                        <td>100%</td>
                        <td>1095</td>
                        <td>Real</td>
                        <td><span class="monthlySparkline" id="monthlySpark31727"><canvas width="96" height="25" style="display: inline-block; vertical-align: top; width: 96px; height: 25px;"></canvas></span></td>
                        <td><span class="dayliSparkline" id="dayliSpark31727"><canvas width="100" height="25" style="display: inline-block; vertical-align: top; width: 100px; height: 25px;"></canvas></span></td>
                        <td>$30</td>
                        <td>
                                                                                        2y 2m
                                                    </td>
                        <td>
                                                        Apr 1, 2018
                        </td>
                        <td><a onclick="getMasterPricingData('31727');" data-toggle="modal"><button id="subscribeToMasterBtn31727" class="btn btn-circle btn-sm green" type="button">Copy</button></a>
                            <div style="display: none;">
                                <input type="hidden" class="monthlyData" oid="31727" value="6.22,-6.15,22.04,-5.08,0.08,12.08,-69.31,-99.82,245.26,88.44,113.73,52.29,25.38,77.72,-29.07,-24.73,-86.48,-89.27,195.77,-7.65,-99.98,278.89,-69.98,-65.48">
                                <input type="hidden" class="dailyGrowthData" oid="31727" value="-99.66,-99.69,-99.72,-99.73,-99.77,-99.77,-99.78,-99.81,-99.90,-99.90,-99.89,-99.84,-99.83,-99.82,-99.81,-99.75,-99.78,-99.77,-99.79,-99.78,-99.77,-99.48,-99.46,-99.36,-99.34,-99.33,-99.33,-99.31,-99.33,-99.34,-99.40,-99.45,-99.33,-99.58,-99.65,-99.73,-99.71,-99.70,-99.68,-99.68,-99.69,-99.68,-99.71,-99.68,-99.80,-99.80,-99.77,-99.81,-99.84,-99.90">
                                <input type="hidden" class="dailyEquityData" oid="31727" value="-99.66,-99.69,-99.73,-99.70,-99.85,-99.89,-99.95,-99.77,-99.85,-99.90,-99.88,-99.84,-99.83,-99.82,-99.79,-99.75,-99.78,-99.77,-99.70,-99.68,-99.59,-99.48,-99.46,-99.36,-99.34,-99.33,-99.32,-99.25,-99.30,-99.34,-99.37,-99.37,-99.35,-99.58,-99.61,-99.73,-99.71,-99.69,-99.68,-99.68,-99.68,-99.68,-99.71,-99.68,-99.80,-99.76,-99.73,-99.79,-99.80,-99.89">
                            </div>
                        </td>
                    </tr>
                                                                                
                                    </tbody>
            </table>
```

My code successfully extracts the data from the first table-data cell (the rank). But it is showing as blank for the second table data cell (the name). What is wrong with this source code:

```python

import scrapy
from behold import Behold


class SignalStartSpider(scrapy.Spider):
    name = 'signalstart'
    start_urls = [
        'https://www.signalstart.com/search-signals',
    ]

    def parse(self, response):
        for provider in response.xpath("//div[@class='row']//tr"):

            yield {
                'rank': provider.xpath('td[1]/text()').get(),
                'name': provider.xpath('td[2]/text()').get(),
            }

```