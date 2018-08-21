import re

import time


from Action.Base import Base
from Bean.team_fight_bean import TeamFight
from Parser.game_parser import Parse
from Public import const


class EngChao(Base):

    url = "http://zq.win007.com/cn/League/36.html"

    def __init__(self):
        self.team_dict = self.get_team_array(self.url)


if __name__ == "__main__":

    kk = EngChao()

    for k, v in kk.team_dict.items():
        print(k)
        print(kk.parse_fail_team(v))