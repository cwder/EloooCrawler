from Action.Base import Base


class Xijia(Base):
    url = "http://zq.win007.com/cn/League/31.html"

    def __init__(self):
        print("Xijia")
        super(Xijia, self).__init__("西甲")
        self.team_dict = self.get_team_array(self.url)

if __name__ == "__main__":

    kk = Xijia()

    for k, v in kk.team_dict.items():
        print(k)
        print(kk.parse_fail_team(v))

