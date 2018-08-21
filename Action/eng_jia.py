from Action.Base import Base


class EngJia(Base):
    url = "http://zq.win007.com/cn/SubLeague/39.html"

    def __init__(self):
        print("EngJia")
        super(EngJia, self).__init__("英甲")
        self.team_dict = self.get_team_array(self.url)


if __name__ == "__main__":

    kk = EngJia()

    for k, v in kk.team_dict.items():
        print(k)
        print(kk.parse_fail_team(v))