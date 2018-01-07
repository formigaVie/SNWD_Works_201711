import urllib2
import BeautifulSoup as BS

if __name__ == '__main__':
    url = 'http://quotes.yourdictionary.com/theme/marriage/'
    response = urllib2.urlopen(url).read()
    soup = BS.BeautifulSoup(response)
    quotes = soup.findAll("a")

    for i in range (0,5):
        quote = soup.findAll("p", attrs={"class": "quoteContent"})[i].string
        print quote