from Action.Base import Base


class WeiershiChao(Base):
    url = "http://zq.win007.com/cn/SubLeague/135.html"

    def __init__(self):
        self.team_dict = self.get_team_array(self.url)


if __name__ == "__main__":

    kk = WeiershiChao()

    for k, v in kk.team_dict.items():
        print(k)
        print(kk.parse_team(v))

