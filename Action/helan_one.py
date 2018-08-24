from Action.Base import Base


class HelanOne(Base):
    url = "http://zq.win007.com/cn/SubLeague/16.html"

    def __init__(self):
        print("HelanOne")
        super(HelanOne, self).__init__("荷甲")
        self.team_dict = self.get_team_array(self.url)


if __name__ == "__main__":

    kk = HelanOne()

    for k, v in kk.team_dict.items():
        print(k)
        print(kk.parse_fail_team(v))