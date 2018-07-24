from Action.Base import Base


class JapanOne(Base):
    url = "http://zq.win007.com/cn/SubLeague/25.html"

    def __init__(self):
        self.team_dict = self.get_team_array(self.url)


if __name__ == "__main__":

    kk = JapanOne()

    for k, v in kk.team_dict.items():
        print(k)
        print(kk.parse_no_win_goal(v[:50]))

        # print(kk.parse_team(v[:50]))
        # print("50----------------------------------------------")
        # print(kk.parse_team(v[50:100]))
        # print("100----------------------------------------------")
        # length = len(v)
        # print(kk.parse_team(v[100:length]))
        # print("full----------------------------------------------")
        # print(kk.parse_team(v))
    print("----------------------------------------------")
    print("----------------------------------------------")
    # for k, v in kk.team_dict.items():
    #     print(k)
    #     print(kk.parse_fail_team(v))
