#IMPORT LIBRARIES
import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import requests

#REQUEST WEBPAGE AND STORE IT AS A VARIABLE
page_to_scrape = input("Enter URL: ")
page_to_scrape = requests.get(page_to_scrape)
#page_to_scrape = requests.get("https://www.cert-bund.de/advisoryshort/CB-K22-0052")

#USE BEAUTIFULSOUP TO PARSE THE HTML AND STORE IT AS A VARIABLE
soup = BeautifulSoup(page_to_scrape.text, 'html.parser')

#FIND ALL THE ITEMS IN THE PAGE WITH A CLASS ATTRIBUTE OF 'TEXT'
#AND STORE THE LIST AS A VARIABLE 
quotes = soup.findAll('table', attrs={'class':'information-table'})
#quotes = soup.findAll('div', attrs={'class':'search-results'})


#FIND ALL THE ITEMS IN THE PAGE WITH A CLASS ATTRIBUTE OF 'AUTHOR'
#AND STORE THE LIST AS A VARIABLE
tags = soup('a')
authors = soup.findAll('a', attrs={"class":"external"}) 



#LOOP THROUGH BOTH LISTS USING THE 'ZIP' FUNCTION
#AND PRINT AND FORMAT THE RESULTS
for quote, author, tag in zip(quotes, authors, tags):
    #print(quote.text + " & " + author.text + tag.get('href', None))
    print(quote.text + "https://www.cert-bund.de" + author.get('href', None), end = "\n")