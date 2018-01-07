import urllib2
import BeautifulSoup as BS

# open or create CSV file
csv_file = open("email_scrape_list.csv", "w")

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

        csv_file.write(email+"\n")  # \n will create a new line

# close CSV file
csv_file.close()
