from Action.Base import Base


class SlowfuckChao(Base):
    url = "http://zq.win007.com/cn/SubLeague/132.html"

    def __init__(self):
        print("SlowfuckChao")
        super(SlowfuckChao, self).__init__("斯洛伐克超")
        self.team_dict = self.get_team_array(self.url)


if __name__ == "__main__":

    kk = SlowfuckChao()

    for k, v in kk.team_dict.items():
        print(k)
        # print(kk.parse_team(v))
        print(kk.parse_fail_team(v))