import urllib2
import BeautifulSoup as BS
import random

if __name__ == '__main__':
    url = 'http://quotes.yourdictionary.com/theme/marriage/'
    response = urllib2.urlopen(url).read()
    soup = BS.BeautifulSoup(response)
    quotes = soup.findAll("p", attrs={"class":"quoteContent"})
    output = random.sample(quotes, 5)

    for x in output:
        print x.text

# zweiter Ansatz