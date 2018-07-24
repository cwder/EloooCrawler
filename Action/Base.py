import re
import time
from copy import deepcopy

import requests

from Bean.team_fight_bean import TeamFight
from Public import const


class Base:


    # 获取所以球队所有战绩列表,获取球队名，球队战绩的map
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


    def parse_no_win_goal(self, array):
        no_win_count = 0;
        have_goal_game = 0;
        for info in array:
            if info.win == 0:
                no_win_count = no_win_count + 1
                if info.insite > 0:
                    have_goal_game = have_goal_game + 1


        res = have_goal_game / no_win_count
        print("输球总场次：",no_win_count,"  ","输球进球场：",have_goal_game," 百分比： ",'%.2f%%' % (res * 100))

    
    # 判断球队在不胜的时侯，有多少概率胜
    def parse_team(self, array):
        print("解析比赛数量",len(array))
        # 需要统计的失败数量
        error_count = 0;
        # 是否是第一次循环
        isFirst = True
        # 当前的战绩是否可以直接进行下一场的预测
        is_suc_flag = False;
        # 目前保持不胜的场次
        begin_fail_count = 0
        result = {}
        for i in range(len(array)):
            # 如果没有赢
            if array[i].win != 3:
                # 如果是第一次统计
                if isFirst :
                    # 当前最新一场都没胜，可以进行是否赢的统计了
                    is_suc_flag = True
                    # 把最新的不胜次数统计次数加一
                    begin_fail_count = begin_fail_count + 1
                    continue
                # 统计一下总的不胜场次
                error_count = error_count + 1;

            else:
                # 说明已经有胜场了，begin_fail_count参数停止统计
                isFirst = False
                # 在胜场的情况下如果之前的error_count为0，表明之前也是胜，不统计不胜次数
                if error_count == 0:
                    continue
                # key = str(error_count) + "场不胜次数"
                # 以不胜场次，不胜场次出现的次数，建立map
                value = result.get(error_count,0)
                value = value + 1
                result[error_count] = value
                
                # 将计数清零
                error_count = 0
        
        # 复制一个（不胜场，不胜场次数）的map
        result2 = deepcopy(result)
        # 把key = 不胜场，进行排列
        keys = sorted(result2)
        # 如果可以进行赢球统计：
        if is_suc_flag:
            print("该队可统计马上会胜的可能性，已",begin_fail_count,"场不胜,百分比越高表示胜的可能越大")
            # 统计到的不胜场次，大于最大的统计后不胜场次
            if (begin_fail_count > keys[-1]):
                print("该队处于破记录中，可考虑投")

        # 统计每个不胜场的百分比
        for i in range(len(keys)):
            
            self.cal_percent(result2,begin_fail_count)
            result2.pop(keys[i])


        return result

    def parse_fail_team(self, array):
        print("解析比赛数量", len(array))

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
        # 复制一个{不败场次，不败场次数}的map
        result2 = deepcopy(result)
        # 因为key是不败的表式值，从小到大排下序
        keys = sorted(result2)
        if is_fail_flag:
            print("该队可统计马上会败的可能性，已",begin_no_fail_couint,"场不败,百分比越高表示败的可能越大")

            if (begin_no_fail_couint > keys[-1]):
                print("该队处于破记录中，可考虑投")

        for i in range(len(keys)):
            # 当i为0时，统计keys[0]=1场不败次数。。。n场不败次数
            # 当i为1时，统计keys[1]=2场不败次数。。。n场不败次数


            self.cal_percent(result2,begin_no_fail_couint)
            result2.pop(keys[i])

        return result


    # data：{不败场次，不败场次数}的map
    # final_data：现有的最大场
    def cal_percent(self,data,final_data):
        # 按胜场类型区分的百分比
        count_percent = 0
        # 按特性场次，进行排序
        keys = sorted(data)
        # 符合条件的场次
        core_data = 0;
        # 其他不符合条件的场次
        others = 0;
        # 全量计算里不符合条件的所有场次
        no_match_full_data = 0;
        # 符合条件是胜负场序号
        result_list = []

        for i in range(len(keys)):

            if i == 0:
                # 第一个统计场次的数量
                core = data[keys[i]];

                if (len(keys) == 1):
                    count_percent = core / core

            else:
                sum = data[keys[i]]
                others = others + sum;
                count = core + others;
                count_percent = core / count

                s = (keys[i] - keys[0]) * sum;
                no_match_full_data = s + no_match_full_data


        full_res = core / (no_match_full_data + core)

        if count_percent >= 0.6 or full_res >= 0.4:
            if final_data == keys[0]:
                print("以下可以进入判断条件：")
        print(keys[0], "   core: ", core, "others: ", others," 百分比：",'%.2f%%' % (count_percent * 100),"全数：",no_match_full_data,"全百分比",'%.2f%%' % (full_res * 100))
        print("====")

        return (keys[0],count_percent,full_res)



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

