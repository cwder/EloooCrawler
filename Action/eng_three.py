from Action.Base import Base


class EngThree(Base):
    url = "http://zq.win007.com/cn/SubLeague/35.html"

    def __init__(self):
        print("EngThree")
        super(EngThree, self).__init__("英乙")
        self.team_dict = self.get_team_array(self.url)


if __name__ == "__main__":

    kk = EngThree()

    for k, v in kk.team_dict.items():
        print(k)
        print(kk.parse_team(v))