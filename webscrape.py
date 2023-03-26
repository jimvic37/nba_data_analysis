# importing modules for web scraping
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.common.exceptions import NoSuchElementException
import pandas as pd
import time


class Webscrape:
    # initialize the class with your driver path
    def __init__(self, your_driver_path):
        # specifying the driver path
        driver_path = Service(your_driver_path)
        # initializing Chrome web driver
        options = webdriver.ChromeOptions()
        options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(service=driver_path, options=options)
        # maximizes the windows when webdriver is opened
        self.driver.maximize_window()

    # call this method in the main.py with the file path of your own and from_season, and to_season
    def scrape_player(self, file_path, from_season, to_season):
        player_list = []
        counter = 1
        while from_season <= to_season:
            to = from_season - 1999
            NBA_URL = f"https://www.nba.com/stats/leaders?Season={from_season}-{to}"
            self.driver.get(NBA_URL)
            time.sleep(2)
            # closing ad for the first page
            if counter == 1:
                self.driver.find_element(By.CLASS_NAME, "ab-close-button").click()
                self.driver.find_element(By.CLASS_NAME, "onetrust-close-btn-ui").click()
                counter += 1
            # closing ad for the second page
            # it takes about 10 seconds for closing ad button appears
            elif counter == 2:
                time.sleep(10)
                self.driver.find_element(By.ID, "bx-close-inside-2078917").click()
                counter += 1
            # closing ad for third page, there are three different random ad comes out with three different ID, so
            # used try and catch to handle NoSuchElementException
            # it takes about 10 seconds for closing ad button appears
            elif counter == 3:
                time.sleep(10)
                try:
                    self.driver.find_element(By.ID, "bx-close-inside-2107034").click()
                except NoSuchElementException:
                    try:
                        self.driver.find_element(By.ID, "bx-close-inside-2107035").click()
                    except NoSuchElementException:
                        self.driver.find_element(By.ID, "bx-close-inside-2107036").click()
                counter += 1

            # while there is next page
            next_page = True
            while next_page:
                # aggregates all the stat for each player
                stats = self.driver.find_elements(By.XPATH, "/html/body/div/div/div/div/section"
                                                            "/div/div/div/table/tbody/tr")
                # for each player's stat
                for stat in stats:
                    row = stat.text.split(" ")[1:]
                    # some players have name length of three so use of slicing and negative index to get the player name
                    temp = row[:-21]
                    player = ""
                    for char in temp:
                        player += char
                        player += " "
                    # use of try and catch in case of index error since selenium is a bot and it
                    # is sensitive to user activity during scraping so an unexpected index error might occur
                    try:
                        # appending to a list to put it into a data frame
                        player_list.append({
                            "Season": f"{from_season}-{to}",
                            "Player": player,
                            "Team": row[-21],
                            "GP": row[-20],
                            "MIN": row[-19],
                            "PTS": row[-18],
                            "FGM": row[-17],
                            "FGA": row[-16],
                            "FG%": row[-15],
                            "3PM": row[-14],
                            "3PA": row[-13],
                            "3P%": row[-12],
                            "FTM": row[-11],
                            "FTA": row[-10],
                            "FT%": row[-9],
                            "OREB": row[-8],
                            "DREB": row[-7],
                            "REB": row[-6],
                            "AST": row[-5],
                            "STL": row[-4],
                            "BLK": row[-3],
                            "TOV": row[-2],
                            "EFF": row[-1]
                        })
                    except IndexError:
                        continue
                next_page_button = self.driver.find_element(By.XPATH, "//body/div/div/div/div/section/div/div/div/div/"
                                                                      "div/button[@title='Next Page Button']")
                # click the next page button only when it is enabled to prevent infinite loop
                if next_page_button.is_enabled():
                    next_page_button.click()
                # else no next page so end the loop
                else:
                    next_page = False
            # moves to the next season
            from_season += 1
        # after while loop create a dataframe and put it as csv file
        df = pd.DataFrame(player_list)
        df.to_csv(file_path)

    # call this method in the main.py with the file path of your own and from_season, and to_season
    def scrape_standing(self, file_path, from_season, to_season):
        team_list = []
        # counter for closing ad
        counter = 1
        while from_season <= to_season:
            to = from_season - 1999
            nba_url = f"https://www.nba.com/standings?Season={from_season}-{to}"
            self.driver.get(nba_url)

            # Use this block if you are scraping two file separately to close the ad
            # if counter == 1:
            #     time.sleep(2)
            #     self.driver.find_element(By.CLASS_NAME, "ab-close-button").click()
            #     self.driver.find_element(By.CLASS_NAME, "onetrust-close-btn-ui").click()
            #     counter +=1

            # counter for conference column
            conf_counter = 0
            stats = self.driver.find_elements(By.XPATH, "/html/body/div/div/div/div/section/div/div/div/table/tbody/tr")
            for stat in stats:
                row = stat.text.split("\n")[-1].split(" ")
                rank = stat.text.split("\n")[0]
                team_name = stat.text.split("\n")[1] + stat.text.split("\n")[2]
                if conf_counter < 15:
                    conference = "Eastern"
                else:
                    conference = "Western"
                team_list.append({
                    "Season": f"{from_season}-{to}",
                    "Conference": conference,
                    "Rank": rank,
                    "Team": team_name,
                    "W": row[0],
                    "L": row[1],
                    "WIN%": row[2]
                })
                conf_counter += 1
            from_season += 1
        df = pd.DataFrame(team_list)
        df.to_csv(file_path)




























