from Action.Base import Base


class Bilishi(Base):
    url = "http://zq.win007.com/cn/SubLeague/5.html"

    def __init__(self):
        print("Bilishi")
        super(Bilishi, self).__init__("比甲")
        self.team_dict = self.get_team_array(self.url)


if __name__ == "__main__":

    kk = Bilishi()

    for k, v in kk.team_dict.items():
        print(k)
        print(kk.parse_fail_team(v))

