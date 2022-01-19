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

import os
os.system('cls' if os.name == 'nt' else 'clear')

#Banner
print("oooooooooo.   .oooooo..o ooooo      ooooooooo.    o8o           oooo             ooooo              .o88o.           ")
print("`888\'   `Y8b d8P\'    `Y8 `888\'      `888   `Y88.  `\"\'           `888             `888\'              888 `\"           ")
print(" 888     888 Y88bo.       888        888   .d88\' oooo   .oooo.o  888  oooo        888  ooo. .oo.   o888oo   .ooooo.  ")
print(" 888oooo888\'  `\"Y8888o.   888        888ooo88P\'  `888  d88(  \"8  888 .8P\'         888  `888P\"Y88b   888    d88\' `88b ")
print(" 888    `88b      `\"Y88b  888        888`88b.     888  `\"Y88b.   888888.          888   888   888   888    888   888 ")
print(" 888    .88P oo     .d8P  888        888  `88b.   888  o.  )88b  888 `88b.        888   888   888   888    888   888 ")
print("o888bood8P\'  8\"\"88888P\'  o888o      o888o  o888o o888o 8\"\"888P\' o888o o888o      o888o o888o o888o o888o   `Y8bod8P\' ")
print("________________________________________________________________________________________________________________________________")
print("https://raw.githubusercontent.com/Eutectico/Various-IT-security-learning-Labs/main/LICENSE")
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
CurrPage = input("Enter Page number: ")
PageSize = input("Enter number between 1-50: ")
DateFrom = input("Enter DateFrom (01.01.2022): ")
DateTo =  input("Enter Date To: ")
page_to_scrape = requests.get("https://www.cert-bund.de/overview/AdvisoryShort?CurrPage=" + CurrPage + "&PageSize=" + PageSize + "&DateFrom=" + DateFrom + "&DateTo=" + DateTo)

#USE BEAUTIFULSOUP TO PARSE THE HTML AND STORE IT AS A VARIABLE
soup = BeautifulSoup(page_to_scrape.text, 'html.parser')

#FIND ALL THE ITEMS IN THE PAGE WITH A CLASS ATTRIBUTE OF 'search-results-col-1', 'search-results-col-2', 'search-results-col-3' and 'search-results-col-4'
#AND STORE THE LIST AS A VARIABLE 
dates = soup.findAll('td', attrs={'class':'search-results-col-1'})
risks = soup.findAll('td', attrs={'class':'search-results-col-2'})
ids = soup.findAll('td', attrs={'class':'search-results-col-3'})
titles = soup.findAll('td', attrs={'class':'search-results-col-4'})

#FIND ALL THE ITEMS IN THE PAGE WITH A CLASS ATTRIBUTE OF 'search-result-link'
#AND STORE THE LIST AS A VARIABLE
links = soup.findAll('a', attrs={'class':'search-result-link'})

def scrape_1():
    if CurrPage != "":
        #LOOP THROUGH BOTH LISTS USING THE 'ZIP' FUNCTION
        #AND PRINT AND FORMAT THE RESULTS
        for date, link in zip(dates, links):
            #USE BEAUTIFULSOUP TO PARSE THE HTML AND STORE IT AS A VARIABLE
            url_1 = ("https://www.cert-bund.de" + link.get('href', None))
            
            #REQUEST WEBPAGE AND STORE IT AS A VARIABLE    
            page_to_scrape = requests.get(url_1)
        
            #USE BEAUTIFULSOUP TO PARSE THE HTML AND STORE IT AS A VARIABLE
            soup = BeautifulSoup(page_to_scrape.text, 'html.parser')
    
            #FIND ALL THE ITEMS IN THE PAGE WITH A CLASS ATTRIBUTE OF 'info-col-2''
            #    AND STORE THE LIST AS A VARIABLE 
            titles = soup.findAll('td', attrs={'class':'info-col-2'})

            #FIND ALL THE ITEMS IN THE PAGE WITH A CLASS ATTRIBUTE OF 'top-header'
            #AND STORE THE LIST AS A VARIABLE 
            infos = soup.findAll('h1', attrs={'class':'top-header'})

            #FIND ALL THE ITEMS IN THE PAGE WITH A CLASS ATTRIBUTE OF 'severity-nr'
            #AND STORE THE LIST AS A VARIABLE 
            severity = soup.findAll('span', attrs={'class':'severity-nr'})

            #FIND ALL THE ITEMS IN THE PAGE WITH A CLASS ATTRIBUTE OF 'information-table'
            #AND STORE THE LIST AS A VARIABLE 
            quotes = soup.findAll('table', attrs={'class':'information-table'})
    
            #FIND ALL THE ITEMS IN THE PAGE WITH A CLASS ATTRIBUTE OF 'external'
            #AND STORE THE LIST AS A VARIABLE
            tags = soup('a')
            authors = soup.findAll('a', attrs={"class":"external"}) 

            #LOOP THROUGH BOTH LISTS USING THE 'ZIP' FUNCTION
            #AND PRINT AND FORMAT THE RESULTS
            for title, info, sev, quote, author, tag in zip(titles, infos, severity, quotes, authors, tags):
                source = author.get('href', None)
                b = source.split("URL=")
                c = urllib.parse.unquote(b[1])

                print (title.text)
                print (url_1)
            
                
                d = quote.text.split("\n\n")             

            #WRITE EACH ITEM AS A NEW ROW IN THE CSV
            writer.writerow([date.text, d[1], sev.text + " " + d[7] , info.text, quote.text + c, url_1])    
            #writer.writerow([date.text, title.text, sev.text, info.text, quote.text + c, url_1])     
            print("__________________________________________________________________________________")   
     
        #CLOSE THE CSV FILE
        file.close()
    sys.exit(-1)

def main():
    print("(+) Retreiving Information...")
    print("__________________________________________________________________________________")   
    scrape_1()


if __name__ == "__main__":
    main() 

