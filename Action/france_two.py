from Action.Base import Base


class FranceTwo(Base):
    url = "http://zq.win007.com/cn/SubLeague/12.html"

    def __init__(self):
        print("FranceTwo")
        super(FranceTwo, self).__init__("法乙")
        self.team_dict = self.get_team_array(self.url)


if __name__ == "__main__":

    kk = FranceTwo()

    for k, v in kk.team_dict.items():
        print(k)
        print(kk.parse_team(v))

