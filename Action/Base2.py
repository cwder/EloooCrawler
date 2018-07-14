import re
import time

import requests

from Bean.team_fight_bean import TeamFight
from Public import const


class Base:


    # 获取所以球队所有战绩列表
    def get_team_array(self):
        resp = cls.gets_response(cls.url)
        html = resp.text
        js = re.search(r"/jsData/matchResult(.+?)>", html)

        url = (const.root_url + js.group())[:-2];

        response_teams = cls.gets_response(url)
        team_html = response_teams.text
        data = team_html.split(";")

        for i in range(len(data)):
            if "var arrTeam" in data[i]:
                team_data = data[i]
                break

        team_data = team_data.replace("var arrTeam = ", "").strip()
        teams = eval(team_data)

        team_dict = {}

        for info in teams:
            text = cls.gets_a_team_datas(info[0], info[1])
            team_dict[info[1]] = text


        return team_dict





    # 获取所有球队
    @classmethod
    def gets_teams(cls):

        resp = cls.gets_response(cls.url)
        html = resp.text
        js = re.search(r"/jsData/matchResult(.+?)>", html)

        url = (const.root_url + js.group())[:-2];

        response_teams = cls.gets_response(url)
        team_html = response_teams.text
        data = team_html.split(";")

        for i in range(len(data)):
            if "var arrTeam" in data[i]:
                team_data = data[i]
                break

        team_data = team_data.replace("var arrTeam = ", "").strip()
        teams = eval(team_data)

        return teams

    # 一只球队的所有战绩表
    @classmethod
    def gets_a_team_datas(cls, id, name):
        url = const.team_url.format(id)
        resp = cls.gets_response(url)
        html = resp.text

        a = re.search(r"/jsData/teamInfo(.+?)>", html)
        url2 = (const.root_url + a.group())[:-2];
        response = cls.gets_response(url2)
        response.encoding = 'utf8'
        js_html = response.text
        data = js_html.split(";")
        arr = []
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

            data.append(TeamFight(name, win, home, insite, outside, time_info))

        return data

    @classmethod
    def gets_response(cls,url):
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
        flag = True

        while flag:
            try:
                response = requests.get(url, timeout=10, headers=headers)
                response.encoding = 'utf8'
                flag = False
            except:
                time.sleep(5)
                flag = True



        return response




    # 解析球队的战绩表,array 是一个联赛集合 tfb对象
    # 1，2，3，4，5场不胜后取胜的次数
    @classmethod
    def parse_team_123(cls, array):
        count_one = 0;
        count_two = 0;
        count_three = 0;
        count_four = 0;
        count_five = 0;
        error_count = 0;
        flag = False
        test = array[:50]
        for i in range(len(array)):
            if array[i].win != 3:
                if flag == False:
                    continue
                error_count = error_count + 1;

            else:
                flag = True
                if error_count == 1:
                    count_one = count_one + 1
                if error_count == 2:
                    count_two = count_two + 1
                if error_count == 3:
                    count_three = count_three + 1
                if error_count == 4:
                    count_four = count_four + 1
                if error_count == 5:
                    count_five = count_five + 1
                error_count = 0;

        return (count_one, count_two, count_three, count_four, count_five)


    # 比较一只球队一胜，跟连胜次数
    @classmethod
    def parse_one_more_suctime(cls, array):
        count_one = 0;
        count_more = 0;
        last = array[0]
        for i in range(len(array)):

            if i+1 < len(array):
               if array[i].win == 3 and array[i+1].win != 3:
                   if i>0 and array[i-1] != 3:
                       count_one = count_one + 1

               if array[i].win == 3 and array[i + 1].win == 3:
                   count_more = count_more + 1;

        return (count_one, count_more)

