import urllib2
import BeautifulSoup as BS

# open or create CSV file
csv_file = open("email_scrape_nec.csv", "w")

if __name__ == '__main__':
    url = 'https://scrapebook22.appspot.com/'
    response = urllib2.urlopen(url).read()
    soup = BS.BeautifulSoup(response)

    links = soup.table.findAll("a")
    for link in links:
        subpage_link = url + link["href"]
        subresponse = urllib2.urlopen(subpage_link).read()
        subsoup = BS.BeautifulSoup(subresponse)
        names = subsoup.findAll("h1")[1].string
        email = subsoup.ul.findAll("span", attrs={"class": "email"})[0].string
        gender = subsoup.ul.findAll("span", attrs={"data-gender":True})[0].string
        city = subsoup.ul.findAll("span", attrs={"data-city":True})[0].string

        csv_file.write(names+","+email+","+city+"\n")  # \n will create a new line

# close CSV file
csv_file.close()