import requests
from bs4 import BeautifulSoup

from Bean.league import League
from Bean.team import Team
from Public import const


class DataParser():

    #联赛列表
    @staticmethod
    def league_list():
        response = requests.get(const.root_url)
        response.encoding = 'utf8'
        html = response.text
        soup = BeautifulSoup(html, "html.parser")
        games_jq_list = soup.find_all(class_='jq_league')
        # league_list = []
        # for game in games_jq_list:
        #     url = const.root_url + game.find('dt').find('a').get('href').strip()
        #     name = game.text.strip()
        #     item = League(url, name)
        #     print(item.__dict__)
        #     league_list.append(item)

        league = dict()
        for game in games_jq_list:
            url = const.root_url + game.find('dt').find('a').get('href').strip()
            name = game.text.strip()
            league[name] = url



        return league


    #球队列表
    @staticmethod
    def team_list(league_name='英超'):
        url = DataParser.league_list().get(league_name)

        response = requests.get(url)
        response.encoding = 'utf8'
        html = response.text
        soup = BeautifulSoup(html, "html.parser")

        team_list = soup.find_all(class_ = 'f_l leftSide')
        # print(team_list)
        team = []
        for item in team_list[0].select('.tabGroup')[0].select('.acc_container')[1].\
        select('.block')[0].select('.clearfix')[0].find_all('a'):
            # aa[const.root_url + item.get('href')] = item.text
            team.append(Team((const.root_url + item.get('href')),item.text,league_name))

        return team







if __name__ == '__main__':
    print("aaa")
    print(DataParser.team_list())






