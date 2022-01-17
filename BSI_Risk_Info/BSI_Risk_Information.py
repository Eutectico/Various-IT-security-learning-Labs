#!/usr/bin/python3
#IMPORT LIBRARIES
from ast import If
import sys
import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import requests
from datetime import datetime

#IMPORT CSV LIBRARY
import csv

#Banner
print("oooooooooo.   .oooooo..o ooooo      ooooooooo.    o8o           oooo             ooooo              .o88o.           ")
print("`888\'   `Y8b d8P\'    `Y8 `888\'      `888   `Y88.  `\"\'           `888             `888\'              888 `\"           ")
print(" 888     888 Y88bo.       888        888   .d88\' oooo   .oooo.o  888  oooo        888  ooo. .oo.   o888oo   .ooooo.  ")
print(" 888oooo888\'  `\"Y8888o.   888        888ooo88P\'  `888  d88(  \"8  888 .8P\'         888  `888P\"Y88b   888    d88\' `88b ")
print(" 888    `88b      `\"Y88b  888        888`88b.     888  `\"Y88b.   888888.          888   888   888   888    888   888 ")
print(" 888    .88P oo     .d8P  888        888  `88b.   888  o.  )88b  888 `88b.        888   888   888   888    888   888 ")
print("o888bood8P\'  8\"\"88888P\'  o888o      o888o  o888o o888o 8\"\"888P\' o888o o888o      o888o o888o o888o o888o   `Y8bod8P\' ")
print("________________________________________________________________________________________________________________________________")





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
DateFrom = input("Enter DateFrom 01.01.2022: ")
DateTo =  input("Enter Date To: ")
page_to_scrape = requests.get("https://www.cert-bund.de/overview/AdvisoryShort?PageSize=" + PageSize + "&DateFrom=" + DateFrom + "&DateTo=" + DateTo)

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

def scrape_1(Pass):
    if Pass == "Tt4Z6UqZhv3xJ#U5yGR*":
        #LOOP THROUGH BOTH LISTS USING THE 'ZIP' FUNCTION
        #AND PRINT AND FORMAT THE RESULTS
        #    for quote, author in zip(quotes, authors):
        for date, link in zip(dates, links):
            #USE BEAUTIFULSOUP TO PARSE THE HTML AND STORE IT AS A VARIABLE
            url_1 = ("https://www.cert-bund.de" + link.get('href', None))
            #print (url_1)
            #scrape(date, url_1)        
            #REQUEST WEBPAGE AND STORE IT AS A VARIABLE    
            page_to_scrape = requests.get(url_1)
        
            #USE BEAUTIFULSOUP TO PARSE THE HTML AND STORE IT AS A VARIABLE
            soup = BeautifulSoup(page_to_scrape.text, 'html.parser')
    
            #FIND ALL THE ITEMS IN THE PAGE WITH A CLASS ATTRIBUTE OF 'top-header'
            #    AND STORE THE LIST AS A VARIABLE 
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
            
                #print(quote.text + c + "\n")
                #print(quote.text)
                d = quote.text.split("\n\n")
                print (d[0])
                print (d[1])
                print (d[2])
                print (d[3])
                print (d[4])
                print (d[5])
                print (d[6])
                print (d[7])
                print (d[8])
                print (d[9])
                print (d[10])            
                print (d[11])
                print (c)

                    
            #WRITE EACH ITEM AS A NEW ROW IN THE CSV
            writer.writerow([date.text, d[1], sev.text + " " + d[7] , info.text, quote.text + c, url_1])    
            #writer.writerow([date.text, title.text, sev.text, info.text, quote.text + c, url_1])     
            print("__________________________________________________________________________________")   
     
        #CLOSE THE CSV FILE
        file.close()
    #print("wrong password!!!") 
    sys.exit(-1)

def main():
    if len(sys.argv) !=2:
        print("(+) Usage: %s <Password>" % sys.argv[0])
        print("(+) Example: %s Tt4Z6UqZhv3xJ#U5yGR*" % sys.argv[0])                                                                                                               
        print("__________________________________________________________________________________")   
        #scrape_1()
        sys.exit(-1)

    Pass = sys.argv[1]
    print("(+) Retreiving Information...")
    print("__________________________________________________________________________________")   
    scrape_1(Pass)


if __name__ == "__main__":
    main() 

