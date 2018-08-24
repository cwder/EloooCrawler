from Action.Base import Base


class GermanyTwo(Base):
    url = "http://zq.win007.com/cn/SubLeague/9.html"

    def __init__(self):
        print("GermanyTwo")
        super(GermanyTwo, self).__init__("德乙")
        self.team_dict = self.get_team_array(self.url)


if __name__ == "__main__":

    kk = GermanyTwo()

    for k, v in kk.team_dict.items():
        print(k)
        print(kk.parse_team(v))
