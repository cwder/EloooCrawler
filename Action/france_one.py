from Action.Base import Base


class FranceOne(Base):
    url = "http://zq.win007.com/cn/League/11.html"

    def __init__(self):
        print("FranceOne")
        super(FranceOne, self).__init__("法甲")
        self.team_dict = self.get_team_array(self.url)


if __name__ == "__main__":

    kk = FranceOne()

    for k, v in kk.team_dict.items():
        print(k)
        print(kk.parse_fail_team(v))


