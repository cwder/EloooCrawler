import json
import re
import time
import urllib
from urllib import request

import numpy as np
import requests

from Bean.team_fight_bean import TeamFight
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
    def get_base_list():
        contry = DataParser.league_list()

        data = []

        for i in range(len(contry)):
            if i == 0:
                url = const.root_first_league_url + str(contry[i][0]) + ".html"
            else:
                url = const.root_sub_league_url + str(contry[i][0]) + ".html"

            team = []
            team.append(contry[i][1]);
            team.append(url)
            data.append(team)


        return data

    # 球队列表
    @staticmethod
    def get_team_list(url):
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

        response_teams = requests.get(url, timeout=10, headers=headers)
        team_html = response_teams.text
        data = team_html.split(";")

        team_data = []
        for i in range(len(data)):
            if "var arrTeam" in data[i]:
                team_data = data[i]
                break

        team_data = team_data.replace("var arrTeam = ", "").strip()
        arr = eval(team_data)

        return arr

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

        return arr

    @staticmethod
    def get_team_socre_url(name ="阿森纳"):
        arr = DataParser.team_list("英超")
        url = "";
        for i in range(len(arr)):
            if name in arr[i]:
                url = const.team_url.format(arr[i][0])
                break

        return url

    @staticmethod
    def get_team_url(id):
        url = const.team_url.format(id)
        return url

    @staticmethod
    def get_team_score_list(name):
        url = DataParser.get_team_socre_url(name)

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

        a = re.search(r"/jsData/teamInfo(.+?)>", html)
        url = (const.root_url + a.group())[:-2];
        response = requests.get(url, timeout=10, headers=headers)
        response.encoding = 'utf8'
        js_html = response.text
        data = js_html.split(";")
        for i in range(len(data)):
           if "teamCount" in data[i]:
               team_data = data[i].replace("var teamCount = ", "").strip()
               arr = eval(team_data)
               break

        data = []
        for i in range(len(arr)):
            team_array = arr[i]

            timestring = arr[i][3]
            time_info = time.strptime(timestring, "%Y-%m-%d %H:%M")
            if name in team_array[7]:
                home = 1
                insite = int(team_array[9])
                outside = int(team_array[10])

            else:
                home = 0
                insite = int(team_array[10])
                outside = int(team_array[9])

            if insite > outside:
                win = 3
            elif insite == outside:
                win = 1
            else:
                win = 0

            data.append(TeamFight(win,home,insite,outside,time_info))

        return data

    @staticmethod
    def parse_score_list(name ="阿森纳"):
        arr = DataParser.get_team_score_list(name)
        count_one = 0;
        count_two = 0;
        count_three = 0;
        error_count = 0;

        for i in range(len(arr[:20])):
            if arr[i].win != 3:
                error_count = error_count+1;

            else:
                if error_count == 1:
                    count_one = count_one + 1
                if error_count == 2:
                    count_two = count_two + 1
                if error_count == 3:
                    count_three = count_three + 1
                error_count = 0;


        print(count_one)
        print(count_two)
        print(count_three)

    # 完整解析
    @staticmethod
    def full_parse():

       league_list = DataParser.get_base_list();

       league_list = league_list[:3]

       for i in range(len(league_list)):
           arr = DataParser.get_team_list(league_list[i][1])
           for j in range(len(arr)):
               DataParser.parse_score_list(arr[j][1])
               print(arr[j][1])

       # print(league_list)
       pass




if __name__ == '__main__':
    # DataParser.parse_team("伯恩茅斯")
    # DataParser.parse_score_list()
    # arr = DataParser.get_base_list()
    # data = []
    # for i in range(len(arr[:3])):
    #     url = arr[i][1]
    #     arr_1 = DataParser.get_team_list(url);
    #     for j in range(len(arr_1)):
    #         array = []
    #         array.append(arr_1[j][1])
    #         array.append(DataParser.get_team_url(arr_1[j][0]))
    #         data.append(array)
    DataParser.full_parse()






