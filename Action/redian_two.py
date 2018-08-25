from Action.Base import Base


class RuiTwo(Base):
    url = "http://zq.win007.com/cn/SubLeague/122.html"

    def __init__(self):
        print("RuiTwo")
        super(RuiTwo, self).__init__("瑞甲")
        self.team_dict = self.get_team_array(self.url)

if __name__ == "__main__":

    kk = RuiTwo()

    for k , v in kk.team_dict.items():
        print(k)
        print(kk.parse_fail_team(v))