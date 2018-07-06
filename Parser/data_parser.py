import json
import re
import urllib
from urllib import request

import numpy as np
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
        respone = requests.get(const.league_url, timeout=10, headers=headers)
        html = respone.text
        s = requests.session()

        s.keep_alive = False
        lea_arr = html.replace('var arrArea = new Array();','')
        arrArea = [0] * 6;
        exec (lea_arr);
        contry_w = []
        for i in range(len(arrArea)):
            for j in range(len(arrArea[i])):
                contry_w.append(arrArea[i][j])
        contry = []
        for i in range(len(contry_w)):
            contry.append(contry_w[i][4])

        league_list = []
        for i in range(len(contry)):
            for j in range(len(contry[i])):
                league_list.append(contry[i][j])


        return league_list

    # 根据名字获取联赛url
    @staticmethod
    def get_league_id(name):
        contry = DataParser.league_list()

        for i in range(len(contry)):
            if name in contry[i]:
                if i == 0:
                    url = const.root_first_league_url + str(contry[i][0]) + ".html"
                else:
                    url = const.root_sub_league_url + str(contry[i][0]) + ".html"
                return url



    #球队列表
    @staticmethod
    def team_list(league_name='英超'):
        url = DataParser.get_league_id(league_name)

        headers = {
            "Accept": "*/*",
            "Accept-Encoding": "gzip, deflate",
            "Accept-Language": "zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2",
            "Host": "zq.win007.com",
            "Referer": "http://zq.win007.com/cn/League/36.html",
            "Connection": "keep-alive",
            "Upgrade-Insecure-Requests": "1",
            "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36"

        }

        requests.adapters.DEFAULT_RETRIES = 5
        response = requests.get(url, timeout=10, headers=headers)

        response.encoding = 'utf8'
        html = response.text
        a = re.search(r"/jsData/matchResult(.+?)>", html)

        url = (const.root_url + a.group())[:-2];

        response_teams = requests.get(url, timeout=10,headers = headers)
        team_html = response_teams.text
        data = team_html.split(";")

        team_data = []
        for i in range(len(data)):
            if "var arrTeam" in data[i]:
                team_data = data[i]
                break

        team_data = team_data.replace("var arrTeam = ","").strip()
        arr = eval(team_data)

        print(arr[0])


        # for i in range(len(team_data)):
        #     print(team_data[i])

        # print(data[1])



        #
        #
        # soup = BeautifulSoup(html, "html.parser")
        # j = soup.find_all("script")
        # print(html)


        # team_list = soup.find_all(class_ = 'f_l leftSide')
        # # print(team_list)
        # team = []
        # for item in team_list[0].select('.tabGroup')[0].select('.acc_container')[1].\
        # select('.block')[0].select('.clearfix')[0].find_all('a'):
        #     # aa[const.root_url + item.get('href')] = item.text
        #     team.append(Team((const.root_url + item.get('href')),item.text,league_name))
        # return team

    @staticmethod
    def play_list(url = '/team/111/'):
        url = const.root_url + url
        response  = requests.get(url)
        response.encoding = 'utf8'
        html = response.text
        soup = BeautifulSoup(html, "html.parser")
        game_list = soup.select('#jq_team_tbody')[0].select('.')
        # print(game_list)




if __name__ == '__main__':
    print(DataParser.team_list())






