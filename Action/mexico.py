from Action.Base import Base


class Mexico(Base):
    url = "http://zq.win007.com/cn/SubLeague/140.html"

    def __init__(self):
        print("Mexico")
        super(Mexico, self).__init__("墨西联")
        self.team_dict = self.get_team_array(self.url)


if __name__ == "__main__":

    kk = Mexico()

    for k, v in kk.team_dict.items():
        print(k)
        print(kk.parse_team(v))