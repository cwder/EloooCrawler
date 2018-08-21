from Action.Base import Base


class BrazolTwo(Base):
    url = "http://zq.win007.com/cn/League/358.html"

    def __init__(self):
        print("BrazolTwo")
        super(BrazolTwo, self).__init__("巴乙")
        self.team_dict = self.get_team_array(self.url)


if __name__ == "__main__":

    kk = BrazolTwo()

    for k, v in kk.team_dict.items():
        print(k)
        print(kk.parse_fail_team(v))