'''Bonus Homework 13-3 Game of Thrones'''

import urllib2
import BeautifulSoup as BS
import re

if __name__ == '__main__':
    url = 'https://en.wikipedia.org/wiki/Game_of_Thrones'
    urlwp = 'https://https://en.wikipedia.org'
    response = urllib2.urlopen(url).read()
    soup = BS.BeautifulSoup(response)
    viewers = 0
    #print soup

    adapt_link = soup.find("li", attrs={"class": "toclevel-2 tocsection-10"}).a["href"]
    adapt_url = url + adapt_link
    adapt_page = urllib2.urlopen(adapt_url).read()
    adapt_soup = BS.BeautifulSoup(adapt_page)

    links = adapt_soup.findAll("a", attrs={"href": re.compile(r"/wiki/Game_of_Thrones_\(season_\d+\)")})
    links = set([link["href"] for link in links])

    for link in links:
        full_season_url = urlwp + link
        season_link = urllib2.urlopen(url).read()
        sl_soup = BS.BeautifulSoup(season_link)
        table = sl_soup.find("table", attrs={"class": "wikitable plainrowheaders wikiepisodetable"})

        if table:
            episode_views = table.findAll("tr", attrs={"class": "vevent"})
            for idx, episode_view in enumerate(episode_views):
                if episode_view:
                    almost = episode_view.findAll("td")[-1].text
                    episode_viewers = float(re.findall("\d+\.\d{0,4}", almost)[0])
                    viewers += episode_viewers
                    print episode_viewers, viewers, season_link, idx
                    # viewers += float(re.sub("\[[0-9]\]", "", almost)) # hab's mit findAll nicht loesen koennen

        print "Game of Thrones had a total of " + str(viewers) + " million viewers when it originally aired."


    #links = soup.table.findAll("a", attrs={"scope": "row"})
    #print links
    #links = soup.findAll(["th", "a"], attrs={"title": True})
    #print links
    #tables = soup.findAll(["a", "th"], attrs={"title": True})[1]
    #print tables
    #source = soup.findAll("a", attrs={"title": True})
    #print source
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
