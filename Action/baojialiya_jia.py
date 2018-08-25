from Action.Base import Base


class BaoChao(Base):
    url = "http://zq.win007.com/cn/SubLeague/131.html"

    def __init__(self):
        print("BaoChao")
        super(BaoChao, self).__init__("保超")
        self.team_dict = self.get_team_array(self.url)


if __name__ == "__main__":

    kk = BaoChao()

    for k, v in kk.team_dict.items():
        print(k)
        # print(kk.parse_team(v))
        print(kk.parse_fail_team(v))