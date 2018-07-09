import re

import time

from Action.base import Base
from Bean.team_fight_bean import TeamFight
from Public import const


class EngGuan(Base):
    url = "http://zq.win007.com/cn/SubLeague/37.html"

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
    def gets_a_team_datas(cls,id,name):
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

            data.append(TeamFight(name,win, home, insite, outside, time_info))




        return data

    # 解析球队的战绩表,array 是 tfb对象
    @classmethod
    def parse_team_123(cls,array):
        count_one = 0;
        count_two = 0;
        count_three = 0;
        count_four = 0;
        count_five = 0;
        error_count = 0;
        flag = False
        test = array[:50]
        for i in range(len(test)):
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

        return (count_one,count_two,count_three,count_four,count_five)


if __name__ == '__main__':
    arr_teams = EngGuan.gets_teams()
    id = arr_teams[:1][0][0]
    name = arr_teams[:1][0][1]
    print(name)
    text = EngGuan.gets_a_team_datas(id,name)
    print(EngGuan.parse_team_123(text))


    # for i in range(len(text)):
    #     print(text[i].__dict__)