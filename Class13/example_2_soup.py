import urllib2
import BeautifulSoup as BS

if __name__ == '__main__':
    url = 'https://scrapebook22.appspot.com/'
    response = urllib2.urlopen(url).read()
    soup = BS.BeautifulSoup(response)
    print soup.title
    print soup.title.string