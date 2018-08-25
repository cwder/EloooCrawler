from Action.Base import Base


class DanTwo(Base):
    url = "http://zq.win007.com/cn/SubLeague/127.html"

    def __init__(self):
        print("DanTwo")
        super(DanTwo, self).__init__("丹乙")
        self.team_dict = self.get_team_array(self.url)


if __name__ == "__main__":

    kk = DanTwo()

    for k, v in kk.team_dict.items():
        print(k)
        print(kk.parse_fail_team(v))