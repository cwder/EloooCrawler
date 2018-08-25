from Action.Base import Base


class AierlanChao(Base):
    url = "http://zq.win007.com/cn/SubLeague/1.html"

    def __init__(self):
        print("AierlanChao")
        super(AierlanChao, self).__init__("爱尓兰超")
        self.team_dict = self.get_team_array(self.url)


if __name__ == "__main__":

    kk = AierlanChao()

    for k, v in kk.team_dict.items():
        print(k)
        print(kk.parse_fail_team(v))

