from Action.Base import Base


class DanChao(Base):
    url = "http://zq.win007.com/cn/SubLeague/7.html"

    def __init__(self):
        print("DanChao")
        super(DanChao, self).__init__("丹超")
        self.team_dict = self.get_team_array(self.url)


if __name__ == "__main__":

    kk = DanChao()

    for k, v in kk.team_dict.items():
        print(k)
        print(kk.parse_fail_team(v))