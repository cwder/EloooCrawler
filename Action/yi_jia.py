from Action.Base import Base


class Yijia(Base):
    url = "http://zq.win007.com/cn/League/34.html"

    def __init__(self):
        print("Yijia")
        super(Yijia, self).__init__("意甲")
        self.team_dict = self.get_team_array(self.url)


if __name__ == "__main__":

    kk = Yijia()

    for k, v in kk.team_dict.items():
        print(k)
        print(kk.parse_fail_team(v))

