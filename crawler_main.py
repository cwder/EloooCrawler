import requests
from bs4 import BeautifulSoup

from Bean.league import League

# root_url = 'http://league.aicai.com/'
#
# response = requests.get(root_url)
# response.encoding = 'utf8'
#
# html = response.text
#
# soup = BeautifulSoup(html,"html.parser")
# games_jq_list = soup.find_all(class_='jq_league')
#
# # print(games_jq_list[0].find('dt'))
# # print(games_jq_list[0].find('dt').a['href'])
# # print(games_jq_list[0].find('dt').find('a').get('href'))
# league_list = []
# for game in games_jq_list:
#     url = game.find('dt').find('a').get('href').strip()
#     name = game.text.strip()
#     item = League(url,name)
#     print(item.__dict__)
#     league_list.append(item)
from Parser.leagu_parser import LeaguParser

LeaguParser.league_list()



