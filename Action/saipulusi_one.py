from Action.Base import Base


class SaipuOne(Base):
    url = "http://zq.win007.com/cn/SubLeague/159.html"

    def __init__(self):
        print("SaipuOne")
        super(SaipuOne, self).__init__("塞浦露斯")
        self.team_dict = self.get_team_array(self.url)


if __name__ == "__main__":

    kk = SaipuOne()

    for k, v in kk.team_dict.items():
        print(k)
        # print(kk.parse_team(v))
        print(kk.parse_fail_team(v))