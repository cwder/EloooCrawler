import re

import time


from Action.Base import Base
from Bean.team_fight_bean import TeamFight
from Parser.game_parser import Parse
from Public import const


class EngGuan(Base):
    # 英冠联赛的url
    url = "http://zq.win007.com/cn/SubLeague/37.html"

    def __init__(self):
        print("EngGuan")
        super(EngGuan, self).__init__("英冠")
        self.team_dict = self.get_team_array(self.url)


if __name__ == "__main__":

    kk = EngGuan()

    for k, v in kk.team_dict.items():
        print(k)
        print(kk.parse_fail_team(v))