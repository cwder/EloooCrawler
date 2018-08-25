from Action.Base import Base


class GermanyOne(Base):
    url = "http://zq.win007.com/cn/League/8.html"

    def __init__(self):
        print("GermanyOne")
        super(GermanyOne, self).__init__("德甲")
        self.team_dict = self.get_team_array(self.url)


if __name__ == "__main__":

    kk = GermanyOne()

    for k, v in kk.team_dict.items():
        print(k)
        print(kk.parse_team(v))