from Action.Base import Base


class PuTaoChao(Base):
    url = "http://zq.win007.com/cn/SubLeague/23.html"

    def __init__(self):
        print("PuTaoChao")
        super(PuTaoChao, self).__init__("葡超")
        self.team_dict = self.get_team_array(self.url)


if __name__ == "__main__":

    kk = PuTaoChao()

    for k, v in kk.team_dict.items():
        print(k)
        print(kk.parse_team(v))