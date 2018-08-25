from Action.Base import Base


class RussuiaTwo(Base):
    url = "http://zq.win007.com/cn/SubLeague/235.html"

    def __init__(self):
        print("RussuiaTwo")
        super(RussuiaTwo, self).__init__("俄甲")
        self.team_dict = self.get_team_array(self.url)

if __name__ == "__main__":

    kk = RussuiaTwo()

    for k , v in kk.team_dict.items():
        print(k)
        print(kk.parse_fail_team(v))