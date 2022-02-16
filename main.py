from urllib.request import urlopen, Request
from bs4 import BeautifulSoup
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import pandas as pd
import matplotlib.pyplot as plt

#Base of URL to be explored

finviz_url="https://finviz.com/quote.ashx?t="

#Tickers of the compagnies we want to study

tickers=['AMZN', 'DIS', 'FB']
news_tables={}

for ticker in tickers:
    url=finviz_url+ticker

    req=Request(url=url, headers={'user-agent':'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:96.0) Gecko/20100101 Firefox/96.0'})
    response = urlopen(req)

    html=BeautifulSoup(response,'html')
    news_table=html.find(id="news-table")
    news_tables[ticker]=news_table


parsed_data=[]

for ticker, news_table in news_tables.items():
    for row in news_table.findAll('tr'):
        title=row.a.get_text()
        date_data=row.td.text.split(' ')

        if len(date_data)==1:
            time=date_data[0]
        else:
            time=date_data[1]
            date=date_data[0]
        parsed_data.append([ticker, date, time, title])

#Creation of the data frame

df=pd.DataFrame(parsed_data, columns=('ticker','date','time','title'))

#Initialisation of the Sentiment Analyser 

vader=SentimentIntensityAnalyzer()

#Creation of a new column in the dataframe to indicate the score

vad=lambda title : vader.polarity_scores(title)['compound']

df['compound']=df['title'].apply(vad)

#Visualization of sentiment analysis

df['date']=pd.to_datetime(df.date).dt.date

plt.figure(figsize=(10,8))

mean_df=df.groupby(['ticker','date']).mean()


mean_df=mean_df.unstack()
mean_df=mean_df.xs('compound',axis='columns').transpose()
mean_df.plot(kind='bar')
plt.show()