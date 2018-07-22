from Action.Base import Base


class Brazol(Base):
    url = "http://zq.win007.com/cn/League/4.html"

    def __init__(self):
        self.team_dict = self.get_team_array(self.url)


if __name__ == "__main__":

    kk = Brazol()

    for k, v in kk.team_dict.items():
        print(k)
        print(kk.parse_fail_team(v))