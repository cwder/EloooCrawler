from Action.Base import Base


class RuishiChao(Base):
    url = "http://zq.win007.com/cn/League/27.html"

    def __init__(self):
        self.team_dict = self.get_team_array(self.url)


if __name__ == "__main__":

    kk = RuishiChao()

    for k, v in kk.team_dict.items():
        print(k)
        # print(kk.parse_team(v))
        print(kk.parse_fail_team(v))