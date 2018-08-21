from Action.Base import Base


class XiTwo(Base):
    url = "http://zq.win007.com/cn/SubLeague/33.html"

    def __init__(self):
        self.team_dict = self.get_team_array(self.url)
        print("西乙")

if __name__ == "__main__":

    kk = XiTwo()

    for k, v in kk.team_dict.items():
        print(k)
        print(kk.parse_fail_team(v))

