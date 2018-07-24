from Action.Base import Base


class JapanTwo(Base):

    url = "http://zq.win007.com/cn/SubLeague/284.html"

    def __init__(self):
        self.team_dict = self.get_team_array(self.url)

if __name__ == "__main__":

    kk = JapanTwo()

    for k , v in kk.team_dict.items():
        print(k)
        print(kk.parse_no_win_goal(v[:50]))

        # print(kk.parse_fail_team(v))
