from Action.Base import Base


class BingDdao(Base):
    url = "http://zq.win007.com/cn/SubLeague/166.html"

    def __init__(self):
        print("BingDdao")
        super(BingDdao, self).__init__("冰超")
        self.team_dict = self.get_team_array(self.url)


if __name__ == '__main__':
    kk = BingDdao()

    for k, v in kk.team_dict.items():
        print(k)
        # print(kk.parse_team(v))
        print(kk.parse_fail_team(v))