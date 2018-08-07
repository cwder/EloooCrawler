from Action.Base import Base


class AustraliaOne(Base):
    url = "http://zq.win007.com/cn/SubLeague/2018-2019/273.html"

    def __init__(self):
        self.team_dict = self.get_team_array(self.url)


if __name__ == "__main__":

    kk = AustraliaOne()

    for k, v in kk.team_dict.items():
        print(k)
        # print(kk.parse_team(v))
        print(kk.parse_fail_team(v))