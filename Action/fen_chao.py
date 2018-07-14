from Action.Base import Base
from Parser.game_parser import Parse

# 芬超
class FenChao(Base):
    url = "http://zq.win007.com/cn/SubLeague/13.html"


    @classmethod
    def parse_list(cls):
        arr_teams = cls.gets_teams()
        for info in arr_teams:
            text = cls.gets_a_team_datas(info[0], info[1])
            print(info[1])
            print(text)

    @classmethod
    def parse_one_more(cls):
        arr_teams = cls.gets_teams()

        for info in arr_teams:
            text = cls.gets_a_team_datas(info[0], info[1])
            print(info[1])
            print(cls.parse_one_more_suctime(text[:50]))


if __name__ == '__main__':
    FenChao.parse_list()