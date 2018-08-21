from Action.Base import Base


class NuoWeiTwo(Base):
    url = "http://zq.win007.com/cn/SubLeague/123.html"

    def __init__(self):
        print("NuoWeiTwo")
        super(NuoWeiTwo, self).__init__("挪甲")
        self.team_dict = self.get_team_array(self.url)


if __name__ == "__main__":

    kk = NuoWeiTwo()

    for k, v in kk.team_dict.items():
        print(k)
        print(kk.parse_fail_team(v))