import requests
from bs4 import BeautifulSoup

from Bean.league import League


class LeaguParser():
    root_url = 'http://league.aicai.com/'

    @classmethod
    def league_list(cls):
        response = requests.get(cls.root_url)
        response.encoding = 'utf8'
        html = response.text
        soup = BeautifulSoup(html, "html.parser")
        games_jq_list = soup.find_all(class_='jq_league')
        league_list = []
        for game in games_jq_list:
            url = cls.root_url + game.find('dt').find('a').get('href').strip()
            name = game.text.strip()
            item = League(url, name)
            print(item.__dict__)
            league_list.append(item)

        return league_list

