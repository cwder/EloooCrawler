from Action.Base import Base


class Korea(Base):
    url = "http://zq.win007.com/cn/SubLeague/15.html"


    def __init__(self):
        self.team_dict = self.get_team_array(self.url)





if __name__ == "__main__":

    kk = Korea()

    for k , v in kk.team_dict.items():
        print(k)
        print(kk.parse_team(v))



    # for i in range(5):
    #     locals()['count_' + str(i)] = 0
    #
    # print(count_0);
    # print(count_1);
    # print(count_2);
    # print(count_3);
    # print(count_4);


