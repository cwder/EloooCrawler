from Action.Base import Base


class XilaChao(Base):
    url = "http://zq.win007.com/cn/SubLeague/32.html"

    def __init__(self):
        print("XilaChao")
        super(XilaChao,self).__init__("希腊超")
        self.team_dict = self.get_team_array(self.url)


if __name__ == "__main__":

    kk = XilaChao()

    for k, v in kk.team_dict.items():
        print(k)
        print(kk.parse_fail_team(v))

