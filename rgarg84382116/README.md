# COVID_ANALYSIS

#### What does it do?
This repo is for analysis on the [corona virus / covid-19](https://www.who.int/health-topics/coronavirus) that will extract the latest data and generate reports. This repo will be **updated daily**
- Creates a time series dataset
- Creates a daily stats dataset 
- Generates a number of visualizations
- You can also filter reports for a given country
- Generates an excel report including all of the above 
- List all countries affected by covid-19
- All results are saved to the output `reports` folder



##### Trend Line

This is an accumulative sum trendline for all the confirmed cases, deaths and recoveries.

##### Daily Trend Line

This is a daily sum trendline for all the confirmed cases, deaths and recoveries.

##### Stacked Daily Confirmed Cases

This stacked bar chart shows a daily sum of people who are currently confirmed (<i>red</i>) and the number of people who have been been confirmed on that day (<i>blue</i>)


##### Daily Confirmed Cases

A count for new cases recorded on that given date, does not take past confirmations into account. 

##### Daily Deaths

A count for deaths due to the virus recorded on that given date, does not take past deaths into account. 

##### Daily Recoveries

A count for new recoveries recorded on that given date, does not take past recoveries into account. 

##### Currently Infected

A count for all the people who are currently infected for a given date (confirmed cases - (recoveries + deaths))


<hr>

### Data Source
- The data comes from the **Novel Coronavirus (COVID-19) Cases**, which is a live dataset provided by JHU CSSE. 
- Data available [here](https://github.com/CSSEGISandData/2019-nCoV).

