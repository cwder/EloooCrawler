from Action.Base import Base


class WuKeLanChao(Base):
    url = "http://zq.win007.com/cn/SubLeague/119.html"

    def __init__(self):
        print("WuKeLanChao")
        super(WuKeLanChao, self).__init__("乌克兰超")
        self.team_dict = self.get_team_array(self.url)


if __name__ == "__main__":

    kk = WuKeLanChao()

    for k, v in kk.team_dict.items():
        print(k)
        print(kk.parse_fail_team(v))
