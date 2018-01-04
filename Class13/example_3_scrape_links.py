import urllib2
import BeautifulSoup as BS

if __name__ == '__main__':
    url = 'https://scrapebook22.appspot.com/'
    response = urllib2.urlopen(url).read()
    soup = BS.BeautifulSoup(response)

    links = soup.table.findAll("a")
    for link in links:
        subpage_link = url + link["href"]
        subresponse = urllib2.urlopen(subpage_link).read()
        subsoup = BS.BeautifulSoup(subresponse)
        # in den Unterseiten finde alle h1 UeBerschriften in dieser Liste gehe auf den zweiten Eintrag und dort nur den string
        names = subsoup.findAll("h1")[1].string
        print names