from Action.Base import Base
from Parser.game_parser import Parse

# 芬超
class FenChao(Base):
    url = "http://zq.win007.com/cn/SubLeague/13.html"

    def __init__(self):
        self.team_dict = self.get_team_array(self.url)


if __name__ == '__main__':
    kk = FenChao()

    for k, v in kk.team_dict.items():
        print(k)
        # print(kk.parse_team(v))
        print(kk.parse_fail_team(v))