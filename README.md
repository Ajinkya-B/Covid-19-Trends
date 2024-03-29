# Covid-19-Trends

## Introduction

The COVID-19 pandemic has caused severe financial stress for many Canadians. A  national poll from October of 2020 reported that nearly **1 in 3 Canadians** are 
worried they may never financially recover from the pandemic. Roughlyhalf of Canadians under the age of 35 have borrowed money from institutions to 
make ends meet, while roughly the same amount have taken advantage of the Government’s emergency assistance. This is largely due to two major reasons.


First, the pandemic drove the unemployment rate as high as **13.7 percent in May of 2020**, an all time high, leaving many Canadians with reduced household income 
or without a source of income at all. Secondly, the price of almost everything has been driven up by the pandemic - for example, Canada’s Food Price Report is 
estimating an increase of anywhere between **3 to 5 percent** in the 2021 calendar year largely due to transport difficulties caused by border and facility closures,
employment difficulties, and shortages of goods all caused by the pandemic.


Employment shortages have significantly slowed the economy, especially in shipping companies like Fedex, who cited that one example facility was only operated at
65 percent capacity due to labour shortages. These types of shortages are causing prices of goods and services to skyrocket. Furthermore, rent prices across Canada
are continuing to recover after dropping, with September being the sixth consecutive month of average rental price increasing.


With all of these financial constraints, we wanted to evaluate the direct impact on Canadians :
* Has the pandemic caused Canada to be overly unaffordable for its inhabitants? 
* Have the rising costs of food caused Canadians to sacrifice other expenditures? 
* How exactly has the pandemic affected how much Canadians spend and what Canadians are spending their money on?

## Datasets

Each dataset can be downloaded from the clickable hyperlink ’download link’ next to each dataset title.

1. Monthly adjusted consumer expenditure basket weights: download link (rename to: weighted-baskets dataset.csv)

* This data was sourced from Statistics Canada (csv format). It shows the fluctuations/growth of consumer expenditure in various products that vary from food, 
clothing, transport, internet and even more. For the purpose of this project we will be focusing in on the changes that take place for food items particularly.

* From this dataset, the first column containing the date, the fourth column containing the name of the commodity, and the tenth column containing the value are used. The rows which contain relevant months (specified inside the program) are used to produce visuals.

2. Consumer Price Index, monthly, not seasonally adjusted: download link (rename to: consumer-price-index dataset.csv)

* This data was sourced from Statistics Canada (csv format). Shows the growth in goods and services pricing compared to 2002, where 2002 is 1.0 (ratio)

* From this dataset, the first column containing the date, the second column containing the region, the fourth column containing the name of the commodity, and 
the tenth column containing the value are used. The rows which contain relevant months (specified inside the program) are used to produce visuals.

3. Epidemiologic data on the COVID 19 Outbreak in Canada: download link (rename to: covid-19 dataset.csv)

* This data was sourced from Statistics Canada (csv format). We will use epidemiological surveillance data to show how the COVID-19 situation is evolving in Canada 
and how it correlates to consumer expenditure.

* From this dataset, the first column containing the region ID, the fourth column containing the date, and the sixteenth column containing the daily number of cases
are used. The rows which contain relevant months (specified inside the program) are used to produce visuals.

4. Canadian unemployment data: download link (rename to: unemployment-rate dataset.csv)

* This data was sourced from the Federal Reserve Economic Data (csv format). We will use monthly unemploynment data to correlate the effect Covid-19 has had on 
unemployment and the correlation of it towards the price index.

* From this dataset, both of the two columns, containing date and unemployment rate are used. The rows which contain relevant months (specified inside the program) 
are used to produce visuals.
