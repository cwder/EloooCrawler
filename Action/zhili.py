from Action.Base import Base


class Zhili(Base):
    url = "http://zq.win007.com/cn/SubLeague/415.html"

    def __init__(self):
        self.team_dict = self.get_team_array(self.url)


if __name__ == "__main__":

    kk = Zhili()

    for k, v in kk.team_dict.items():
        print(k)
        # print(kk.parse_team(v))
        # print("不败场次统计-----------------------------------------------------")
        print(kk.parse_fail_team(v))
