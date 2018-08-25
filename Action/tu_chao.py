from Action.Base import Base


class Tuchao(Base):
    url = "http://zq.win007.com/cn/SubLeague/30.html"

    def __init__(self):
        print("Tuchao")
        super(Tuchao, self).__init__("土超")
        self.team_dict = self.get_team_array(self.url)


if __name__ == "__main__":

    kk = Tuchao()

    for k, v in kk.team_dict.items():
        print(k)
        # print(kk.parse_team(v))
        print(kk.parse_fail_team(v))