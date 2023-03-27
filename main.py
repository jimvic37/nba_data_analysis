from webscrape import Webscrape

your_driver_path = "your_driver_path"
player_file_path = r"your_file_path_for_player_stat"
team_file_path = r"your_file_path_for_team_stand"

# put the year input as integer type
from_season = 2017
to_season = 2022

webscrape = Webscrape(your_driver_path)
webscrape.scrape_player(player_file_path, from_season, to_season)
webscrape.scrape_standing(team_file_path, from_season, to_season)
