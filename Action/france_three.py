from Action.Base import Base


class FranceThree(Base):
    url = "http://zq.win007.com/cn/SubLeague/203.html"

    def __init__(self):
        print("FranceThree")
        super(FranceThree, self).__init__("法丙")
        self.team_dict = self.get_team_array(self.url)


if __name__ == "__main__":

    kk = FranceThree()

    for k, v in kk.team_dict.items():
        print(k)
        print(kk.parse_fail_team(v))


