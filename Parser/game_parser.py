class Parse():

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

        return (count_one, count_two, count_three, count_four, count_five)

