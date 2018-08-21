from Action.germany_three import GermanyThree
from Action.xi_jia import Xijia
from Action.xi_two import XiTwo

kk = XiTwo()
for k, v in kk.team_dict.items():
    kk.parse_unique_team(v)
kk = Xijia()
for k, v in kk.team_dict.items():
    kk.parse_unique_team(v)
kk = GermanyThree()
for k, v in kk.team_dict.items():
    kk.parse_unique_team(v)