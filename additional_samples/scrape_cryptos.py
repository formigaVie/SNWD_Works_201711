import urllib2
import BeautifulSoup as BS
import re

url = 'https://www.finanzen.net/devisen/kryptowaehrungen'
#url = 'https://www.coingecko.com/de'
# die Seite Coingecko verursacht Fehler
response = urllib2.urlopen(url).read()
soup = BS.BeautifulSoup(response)
#soupE= soup.div.findAll("div", attrs={"id":"cryptoList_EUR"})
#print soupE
#soupEl = soup.div.findAll("a", attrs={"title":"Euro"})
#soupEl = soup.div.findAll("a")
#print soupEl
cryptolist = soup.findAll("div",attrs={"id":"cryptoList_EUR"})
print cryptolist
#links = soup.findAll("a",attrs={"title": "Euro"})
#print links
#for link in links:
#    subpage_link = url + link["href"]
#    subresponse = urllib2.urlopen(subpage_link).read()
#    subsoup = BS.BeautifulSoup(subresponse)
    #print subsoup.findAll("h1",attrs={"class": "font-resize"})
#    print subsoup.h1.findAll("span", attrs={"class": "instrument-id"})
    #print soup.html.head.title.string