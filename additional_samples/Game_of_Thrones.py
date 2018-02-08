import urllib2
import BeautifulSoup as BS
import re

if __name__ == '__main__':

    url = "https://en.wikipedia.org/wiki/Game_of_Thrones"
    urlwiki = "https://en.wikipedia.org"
    page = urllib2.urlopen(url).read()
    soup = BS.BeautifulSoup(page)
    viewers = 0

    adaptation_link = soup.find("li", attrs={"class": "toclevel-2 tocsection-10"}).a["href"]
    adaptation_url = url + adaptation_link
    adaptation_page = urllib2.urlopen(adaptation_url).read()
    adaptation_soup = BS.BeautifulSoup(adaptation_page)

    season_links = adaptation_soup.findAll("a", attrs={"href": re.compile(r"/wiki/Game_of_Thrones_\(season_\d+\)")})
    season_links = set([link["href"] for link in season_links])

    for season_link in season_links:
        full_season_url = urlwiki + season_link
        season_page = urllib2.urlopen(full_season_url).read()
        season_soup = BS.BeautifulSoup(season_page)
        table = season_soup.find("table", attrs={"class": "wikitable plainrowheaders wikiepisodetable"})

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

