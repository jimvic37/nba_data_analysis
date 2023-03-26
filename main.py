from webscrape import Webscrape

your_driver_path = "C:\Development\chromedriver_win32\chromedriver.exe"
player_file_path = r"C:\Users\jimvi\OneDrive\Documents\job\Projects\nba_project_data_analysis + web_scraper" \
                 r"\webscrapeNba\nba_player_data.csv"
team_file_path = r"C:\Users\jimvi\OneDrive\Documents\job\Projects\nba_project_data_analysis + web_scraper" \
                 r"\webscrapeNba\nba_team_data.csv"

# put the year input as integer type
from_season = 2017
to_season = 2021

webscrape = Webscrape(your_driver_path)
webscrape.scrape_player(player_file_path, from_season, to_season)
webscrape.scrape_standing(team_file_path, from_season, to_season)
