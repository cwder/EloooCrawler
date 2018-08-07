from Action.Base import Base


class FenTwo(Base):

    url = "http://zq.win007.com/cn/SubLeague/212.html"

    def __init__(self):
        self.team_dict = self.get_team_array(self.url)

if __name__ == "__main__":

    kk = FenTwo()

    for k , v in kk.team_dict.items():
        print(k)
        kk.parse_fail_team(v)


        # print(kk.parse_fail_team(v))
