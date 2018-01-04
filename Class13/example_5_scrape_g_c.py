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
        # print subsoup.ul.findAll("span","email")
        email = subsoup.ul.findAll("span", attrs={"class": "email"})[0].string
        gender = subsoup.ul.findAll("span", attrs={"data-gender":True})[0].string
        city = subsoup.ul.findAll("span", attrs={"data-city":True})[0].string
        print "email: {}, city: {}, gender:{}" .format(email,gender,city)
        print email, city, gender