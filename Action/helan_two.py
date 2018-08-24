from Action.Base import Base


class HelanTwo(Base):
    url = "http://zq.win007.com/cn/SubLeague/17.html"

    def __init__(self):
        print("HelanTwo")
        super(HelanTwo, self).__init__("荷乙")
        self.team_dict = self.get_team_array(self.url)


if __name__ == "__main__":

    kk = HelanTwo()

    for k, v in kk.team_dict.items():
        print(k)
        print(kk.parse_team(v))