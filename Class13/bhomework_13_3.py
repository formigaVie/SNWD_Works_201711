'''Bonus Homework 13-3 Game of Thrones'''

import urllib2
import BeautifulSoup as BS

if __name__ == '__main__':
    url = 'https://en.wikipedia.org/wiki/Game_of_Thrones'
    response = urllib2.urlopen(url).read()
    soup = BS.BeautifulSoup(response)
    #print soup

    #links = soup.table.findAll("a", attrs={"scope": "row"})
    #print links
    #links = soup.findAll(["th", "a"], attrs={"title": True})
    #print links
    #tables = soup.findAll(["a", "th"], attrs={"title": True})[1]
    #print tables
    source = soup.findAll("a", attrs={"title": True})
    print source
    #sourcewi = soup.findAll("table", attrs={"class": "wikitable plainrowheaders"})
    #print sourcewi

#    linkprep = BS.BeautifulSoup(sourcewi)
#    linkswi = linkprep.soup.findAll("a")
#    print linkswi

#    for link in links:
 #       subpage_link = url + link["href"]
  #      subresponse = urllib2.urlopen(subpage_link).read()
   #     subsoup = BS.BeautifulSoup(subresponse)
    # print subsoup
