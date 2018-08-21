from Action.Base import Base


class RuiChao(Base):
    url = "http://zq.win007.com/cn/SubLeague/26.html"

    def __init__(self):
        self.team_dict = self.get_team_array(self.url)

if __name__ == "__main__":

    kk = RuiChao()

    for k , v in kk.team_dict.items():
        print(k)
        print(kk.parse_team(v))
