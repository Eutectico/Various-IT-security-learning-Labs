#!/usr/bin/python3
#IMPORT LIBRARIES
import sys
import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import requests
from datetime import datetime

#IMPORT CSV LIBRARY
import csv

#OPEN A NEW CSV FILE. IT CAN BE CALLED ANYTHING
dt = datetime.now()
timestamp = datetime.timestamp(dt) 
date_time = datetime.fromtimestamp(timestamp)
str_date_time = date_time.strftime("%Y%m%d%m%Y%H%M%S")
file = open('BSI_' + str_date_time + '.csv', 'w')
#CREATE A VARIABLE FOR WRITING TO THE CSV
writer = csv.writer(file)

#CREATE THE HEADER ROW OF THE CSV
writer.writerow(['Date', 'Title', 'Risk', 'ID#', 'Information','Link'])

#REQUEST WEBPAGE AND STORE IT AS A VARIABLE
#page_to_scrape = input("Enter URL: ")
#page_to_scrape = requests.get(page_to_scrape)
#page_to_scrape = requests.get("https://www.cert-bund.de/advisoryshort/CB-K22-0052")
PageSize = input("Enter number between 1-50: ")
page_to_scrape = requests.get("https://www.cert-bund.de/overview/AdvisoryShort?PageSize=" + PageSize)

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

def scrape(date, url_1):
    #REQUEST WEBPAGE AND STORE IT AS A VARIABLE    
    page_to_scrape = requests.get(url_1)
    
    #USE BEAUTIFULSOUP TO PARSE THE HTML AND STORE IT AS A VARIABLE
    soup = BeautifulSoup(page_to_scrape.text, 'html.parser')

    #FIND ALL THE ITEMS IN THE PAGE WITH A CLASS ATTRIBUTE OF 'top-header'
    #AND STORE THE LIST AS A VARIABLE 
    titles = soup.findAll('td', attrs={'class':'info-col-2'})

    #FIND ALL THE ITEMS IN THE PAGE WITH A CLASS ATTRIBUTE OF 'top-header'
    #AND STORE THE LIST AS A VARIABLE 
    infos = soup.findAll('h1', attrs={'class':'top-header'})

    #FIND ALL THE ITEMS IN THE PAGE WITH A CLASS ATTRIBUTE OF 'top-header'
    #AND STORE THE LIST AS A VARIABLE 
    severity = soup.findAll('span', attrs={'class':'severity-nr'})

    #FIND ALL THE ITEMS IN THE PAGE WITH A CLASS ATTRIBUTE OF 'TEXT'
    #AND STORE THE LIST AS A VARIABLE 
    quotes = soup.findAll('table', attrs={'class':'information-table'})
    
    #FIND ALL THE ITEMS IN THE PAGE WITH A CLASS ATTRIBUTE OF 'AUTHOR'
    #AND STORE THE LIST AS A VARIABLE
    tags = soup('a')
    authors = soup.findAll('a', attrs={"class":"external"}) 

    #LOOP THROUGH BOTH LISTS USING THE 'ZIP' FUNCTION
    #AND PRINT AND FORMAT THE RESULTS
    for title, info, sev, quote, author, tag in zip(titles, infos, severity, quotes, authors, tags):
        source = author.get('href', None)
        b = source.split("URL=")
        #print (b[1])
        c = urllib.parse.unquote(b[1])

        print (title.text)
        print (url_1)
        print ("Source: " + c)
        print(quote.text + c + "\n")
                
        #WRITE EACH ITEM AS A NEW ROW IN THE CSV
        writer.writerow([date.text, title.text, sev.text, info.text, quote.text + c, url_1])
    #CLOSE THE CSV FILE
#    file.close()    

def scrape_1():
    #LOOP THROUGH BOTH LISTS USING THE 'ZIP' FUNCTION
    #AND PRINT AND FORMAT THE RESULTS
    #for quote, author in zip(quotes, authors):
    for date, link in zip(dates, links):
        #USE BEAUTIFULSOUP TO PARSE THE HTML AND STORE IT AS A VARIABLE
        url_1 = ("https://www.cert-bund.de" + link.get('href', None))
        #print (url_1)
        scrape(date, url_1)            
        print("__________________________________________________________________________________")   
     
    #CLOSE THE CSV FILE
    file.close()

def main():
    if len(sys.argv) !=2:
        print("(+) Usage: %s <PageSize>" % sys.argv[0])
        print("(+) Example: %s 1-50" % sys.argv[0])
        print("(+) Retreiving Information...")
        scrape_1()
        #sys.exit(-1)

    PageSize = sys.argv[1]
    print("(+) Retreiving Information...")
    scrape_1()


if __name__ == "__main__":
    main() 