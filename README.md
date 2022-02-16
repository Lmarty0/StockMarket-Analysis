# StockMarket-Analysis

## Goal :

This project aims to graw the evolution of the stock market value based on sentiment analysis.

## Data

We used the data taken from the website Finviz. It has the advantage to list and add a link to every article published on a given compagny with the corresponding date. 

## Process

  - We started by scraping data from FinViz by using its hml source code and the library "BeautifulSoup" on python
  - We created a dataframe associating the title of the article with the date of the publication
  - We used the sentiment analyser Vader which give a score to a sentence based on its level of positivity
  - We plot the mean of these scores on a given day and plot its evolution across time
  
  ## Stepping back
  
  This project is a first approach of the financial field. It is quite naive and has many ways to evolve. Indeed : Vader has not the best accuracy in the sentiment analysis tools for NLP. 
  Then, reducing our study on the title of the article could be the source of mistakes, especially if the title is meant to be catchy. Finaly it would the great to study the correlation betweet the positivity score avec the evolution of the value on the stockmarket. 
