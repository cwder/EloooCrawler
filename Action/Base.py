import re
import time
from copy import deepcopy

import requests

from Bean.team_fight_bean import TeamFight
from Public import const


class Base:


    # 获取所以球队所有战绩列表
    def get_team_array(self,url):
        resp = self.gets_response(url)
        html = resp.text
        js = re.search(r"/jsData/matchResult(.+?)>", html)

        url = (const.root_url + js.group())[:-2];

        response_teams = self.gets_response(url)
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
            text = self.gets_a_team_datas(info[0], info[1])
            team_dict[info[1]] = text


        return team_dict


    def parse_team(self, array):


        error_count = 0;
        flag = False
        is_suc_flag = False;
        # 目前保持不胜的场次
        begin_fail_couint = 0
        result = {}
        for i in range(len(array)):
            if array[i].win != 3:
                if flag == False:
                    is_suc_flag = True
                    begin_fail_couint = begin_fail_couint + 1
                    continue
                error_count = error_count + 1;

            else:
                flag = True
                if error_count == 0:
                    continue
                # key = str(error_count) + "场不胜次数"
                value = result.get(error_count,0)
                value = value + 1
                result[error_count] = value
                error_count = 0

        result2 = deepcopy(result)
        keys = sorted(result2)

        if is_suc_flag:
            print("该队可统计马上会胜的可能性，已",begin_fail_couint,"场不胜,百分比越高表示胜的可能越大")

        for i in range(len(keys)):

            if keys[i] == begin_fail_couint:
                print("统计这次信息：")

            self.cal_percent(result2)
            result2.pop(keys[i])



        return result

    def parse_fail_team(self, array):

        error_count = 0;
        flag = False
        is_fail_flag = False;
        # 目前保持不败的场次
        begin_no_fail_couint = 0
        result = {}
        for i in range(len(array)):
            if array[i].win != 0:
                if flag == False:
                    is_fail_flag = True
                    begin_no_fail_couint = begin_no_fail_couint + 1
                    continue
                # 代表不败的表式值：n场不败统计
                error_count = error_count + 1;

            else:
                flag = True
                if error_count == 0:
                    continue
                key = str(error_count) + "场不败次数"
                value = result.get(error_count, 0)
                # 代表表式值次数：n场不败的次数
                value = value + 1
                result[error_count] = value
                error_count = 0
        # 复制一个
        result2 = deepcopy(result)
        # 因为key是不败的表式值，从小到大排下序
        keys = sorted(result2)
        if is_fail_flag:
            print("该队可统计马上会败的可能性，已",begin_no_fail_couint,"场不败,百分比越高表示败的可能越大")
        for i in range(len(keys)):
            # 当i为0时，统计keys[0]=1场不败次数。。。n场不败次数
            # 当i为1时，统计keys[1]=2场不败次数。。。n场不败次数

            if keys[i] == begin_no_fail_couint:
                print("统计这次信息：")
            self.cal_percent(result2)
            result2.pop(keys[i])

        return result


    def cal_percent(self,data):

        # keys = sorted(data)
        # for i in range(len(keys)):
        #     self.cal_percent(data)
        #     data.pop(keys[i])
        res = 0
        count = 0
        keys = sorted(data)
        core = 0;
        others = 0;
        a = 0;
        a2 = 0;
        for i in range(len(keys)):

            if i == 0:
                core = data[keys[i]];

                if (len(keys) == 1):
                    res = core / core

            else:
                sum = data[keys[i]]
                others = others + sum;
                count = core + others;
                res = core / count

                s = (keys[i] - keys[0]) * sum;
                a = s + a
                # a2 = core / a ;
        a2 = core / (a + core)
        if a2 == 0:
            a2 = 1

        print(keys[0], "   core: ", core, "others: ", others," 百分比：",'%.2f%%' % (res * 100),"全数：",a,"全百分比",'%.2f%%' % (a2 * 100))
        print("====")

        return (core,others)



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

    def gets_a_team_datas(self, id, name):
        url = const.team_url.format(id)
        resp = self.gets_response(url)
        html = resp.text

        a = re.search(r"/jsData/teamInfo(.+?)>", html)
        url2 = (const.root_url + a.group())[:-2];
        response = self.gets_response(url2)
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
                d_name = team_array[8].split('^')[0]
                home = 1
                insite = int(team_array[9])
                outside = int(team_array[10])

            else:
                d_name = team_array[7].split('^')[0]
                home = 0
                insite = int(team_array[10])
                outside = int(team_array[9])

            if insite > outside:
                win = 3
            elif insite == outside:
                win = 1
            else:
                win = 0

            data.append(TeamFight(name, d_name,win, home, insite, outside, time_info))

        return data


    def gets_response(self,url):
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
    def parse_team_1234567(self, array):
        count_one = 0;
        count_two = 0;
        count_three = 0;
        count_four = 0;
        count_five = 0;
        count_six = 0;
        count_seven = 0;
        error_count = 0;
        flag = False
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
                if error_count == 6:
                    count_six = count_six + 1
                if error_count == 7:
                    count_seven = count_seven + 1
                error_count = 0;

        return (count_one, count_two, count_three, count_four, count_five,count_six,count_seven)


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

