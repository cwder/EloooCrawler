from Action.Base import Base


class JackOne(Base):
    url = "http://zq.win007.com/cn/League/137.html"

    def __init__(self):
        print("JackOne")
        super(JackOne, self).__init__("捷甲")
        self.team_dict = self.get_team_array(self.url)


if __name__ == "__main__":

    kk = JackOne()

    for k, v in kk.team_dict.items():
        print(k)
        # print(kk.parse_team(v))
        print(kk.parse_fail_team(v))