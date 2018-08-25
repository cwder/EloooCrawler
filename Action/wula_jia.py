from Action.Base import Base


class WulaJia(Base):
    url = "http://zq.win007.com/cn/SubLeague/240.html"

    def __init__(self):
        print("WulaJia")
        super(WulaJia, self).__init__("乌拉圭甲")
        self.team_dict = self.get_team_array(self.url)


if __name__ == "__main__":

    kk = WulaJia()

    for k, v in kk.team_dict.items():
        print(k)
        print(kk.parse_team(v))