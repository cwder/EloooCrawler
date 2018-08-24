from Action.Base import Base


class RussuiaChao(Base):
    url = "http://zq.win007.com/cn/SubLeague/10.html"

    def __init__(self):
        print("RussuiaChao")
        super(RussuiaChao, self).__init__("俄超")
        self.team_dict = self.get_team_array(self.url)

if __name__ == "__main__":

    kk = RussuiaChao()

    for k , v in kk.team_dict.items():
        print(k)
        print(kk.parse_team(v))