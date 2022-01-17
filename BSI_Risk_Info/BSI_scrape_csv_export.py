#IMPORT LIBRARIES
import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import requests

#IMPORT CSV LIBRARY
import csv

#OPEN A NEW CSV FILE. IT CAN BE CALLED ANYTHING
file = open('BSI.csv', 'w')
#CREATE A VARIABLE FOR WRITING TO THE CSV
writer = csv.writer(file)

#CREATE THE HEADER ROW OF THE CSV
writer.writerow(['Date', 'Title', 'Risk', 'ID#', 'Link'])

#REQUEST WEBPAGE AND STORE IT AS A VARIABLE
#page_to_scrape = input("Enter URL: ")
#page_to_scrape = requests.get(page_to_scrape)
#page_to_scrape = requests.get("https://www.cert-bund.de/advisoryshort/CB-K22-0052")
page_to_scrape = requests.get("https://www.cert-bund.de/overview/AdvisoryShort?PageSize=50")

#USE BEAUTIFULSOUP TO PARSE THE HTML AND STORE IT AS A VARIABLE
soup = BeautifulSoup(page_to_scrape.text, 'html.parser')

#FIND ALL THE ITEMS IN THE PAGE WITH A CLASS ATTRIBUTE OF 'TEXT'
#AND STORE THE LIST AS A VARIABLE 
#quotes = soup.findAll('table', attrs={'class':'information-table'})
#quotes = soup.findAll('tr', attrs={'class':'search-result-0'})
dates = soup.findAll('td', attrs={'class':'search-results-col-1'})
risks = soup.findAll('td', attrs={'class':'search-results-col-2'})
ids = soup.findAll('td', attrs={'class':'search-results-col-3'})
titles = soup.findAll('td', attrs={'class':'search-results-col-4'})



#FIND ALL THE ITEMS IN THE PAGE WITH A CLASS ATTRIBUTE OF 'AUTHOR'
#AND STORE THE LIST AS A VARIABLE
#authors = soup.findAll('a', attrs={"class":"external"}) 
links = soup.findAll('a', attrs={'class':'search-result-link'})

#LOOP THROUGH BOTH LISTS USING THE 'ZIP' FUNCTION
#AND PRINT AND FORMAT THE RESULTS
#for quote, author in zip(quotes, authors):
for date, risk, id, title, link in zip(dates, risks, ids, titles, links):
    print(title.text + date.text + "\nRisk" + risk.text + id.text)
    print("https://www.cert-bund.de" + link.get('href', None), end = "\n")
    print("__________________________________________________________________________________")
    #print(quote.text + "https://www.cert-bund.de" + author.get('href', None))
    #WRITE EACH ITEM AS A NEW ROW IN THE CSV
    writer.writerow([date.text, title.text, risk.text, id.text, "https://www.cert-bund.de" + link.get('href', None)])

    #writer.writerow([quote.text, author.text])
    #writer.writerow([quote.text + "|", "https://www.cert-bund.de" + author.get('href', None)])
#CLOSE THE CSV FILE
file.close()