from Action.Base import Base


class SaierweiyaChao(Base):
    url = "http://zq.win007.com/cn/SubLeague/129.html"

    def __init__(self):
        print("SaierweiyaChao")
        super(SaierweiyaChao, self).__init__("塞尓维亚超")
        self.team_dict = self.get_team_array(self.url)


if __name__ == "__main__":

    kk = SaierweiyaChao()

    for k, v in kk.team_dict.items():
        print(k)
        # print(kk.parse_team(v))
        print(kk.parse_fail_team(v))