from Action.Base import Base


class GermanyThree(Base):
    url = "http://zq.win007.com/cn/League/693.html"

    def __init__(self):
        self.team_dict = self.get_team_array(self.url)
        print("德丙")

if __name__ == "__main__":

    kk = GermanyThree()

    for k, v in kk.team_dict.items():
        print(k)
        print(kk.parse_fail_team(v))