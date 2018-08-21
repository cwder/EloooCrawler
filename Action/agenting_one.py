from Action.Base import Base


class AgentingOne(Base):
    url = "http://zq.win007.com/cn/League/29.html"

    def __init__(self):
        super(AgentingOne, self).__init__("阿甲")
        self.team_dict = self.get_team_array(self.url)


if __name__ == "__main__":

    kk = AgentingOne()

    for k, v in kk.team_dict.items():
        print(k)
        # print(kk.parse_team(v))
        print(kk.parse_fail_team(v))