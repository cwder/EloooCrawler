from Action.Base import Base


class AierlanTwo(Base):
    url = "http://zq.win007.com/cn/SubLeague/139.html"

    def __init__(self):
        print("AierlanTwo")
        super(AierlanTwo, self).__init__("爱尓兰甲")
        self.team_dict = self.get_team_array(self.url)


if __name__ == "__main__":

    kk = AierlanTwo()

    for k, v in kk.team_dict.items():
        print(k)
        print(kk.parse_fail_team(v))

