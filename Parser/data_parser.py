import urllib
from urllib import request

import requests
from bs4 import BeautifulSoup

from Bean.league import League
from Bean.team import Team
from Public import const


class DataParser():

    #联赛列表
    @staticmethod
    def league_list():
        headers = {
            "Accept": "*/*",
            "Accept-Encoding": "gzip, deflate",
            "Accept-Language": "zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2",
            "Host": "zq.win007.com",
            "Referer":"http://zq.win007.com/cn/League/36.html",
            "Cookie":"UM_distinctid=1645ef22e2f209-0424a4a5c8cb8a-143f7040-15f900-1645ef22e303ad; CNZZDATA1261430177=1230666043-1530598710-null%7C1530609603",
            "Connection":"keep-alive",
            "Upgrade-Insecure-Requests": "1",
            "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36"
        }
        requests.adapters.DEFAULT_RETRIES = 5
        respone = requests.get("http://zq.win007.com/jsData/leftData/leftData.js", timeout=10, headers=headers)
        html = respone.text
        s = requests.session()
        s.keep_alive = False
        # print(html)
        # soup = BeautifulSoup(html, "lxml")
        # games_jq_list = soup.select('.left_list3')
        # print(games_jq_list)

        # league_list = []
        # for game in games_jq_list:
        #     url = const.root_url + game.find('dt').find('a').get('href').strip()
        #     name = game.text.strip()
        #     item = League(url, name)
        #     print(item.__dict__)
        #     league_list.append(item)

        # league = dict()
        # for game in games_jq_list:
        #     url = const.root_url + game.find('dt').find('a').get('href').strip()
        #     name = game.text.strip()
        #     league[name] = url



        return html


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

    @staticmethod
    def play_list(url = '/team/111/'):
        url = const.root_url + url
        response  = requests.get(url)
        response.encoding = 'utf8'
        html = response.text
        soup = BeautifulSoup(html, "html.parser")
        game_list = soup.select('#jq_team_tbody')[0].select('.')
        print(game_list)




if __name__ == '__main__':
    print("aaa")
    print(DataParser.league_list())






