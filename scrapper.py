import cloudscraper
from bs4 import BeautifulSoup
import time
import pandas as pd
import re

scraper = cloudscraper.create_scraper() 


year = input("Enter league year (exp. 2015-2016): ")

if not re.fullmatch(r"\d{4}-\d{4}", year):
    print("Wrong year, defaulting to (2015-2016)")
    year = "2015-2016"

list_of_leagues = ["Premier Leauge", "La Liga", "Bundesliga", "Serie A"
                   "Ligue 1"]

print("Choose A league from the list below")
print("=" * 40)
for index,league in enumerate(list_of_leagues):
    print(f"{index + 1}: {league}")

league_number =  int(input("Your choice: ")) - 1
chosen_league = list_of_leagues[league_number].replace(" ", "-")
print("=" * 40)

url = f"https://fbref.com/en/comps/9/{year}/{year}-{chosen_league}-Stats"
page = scraper.get(url) 

if page.status_code == 200:
    soup = BeautifulSoup(page.content, "html.parser") 
    all_squads  = soup.find("tbody").find_all("tr")
    final_all_players = []

    for squad in all_squads:
        link_tag = squad.find("a")
        squad_name = squad.find("a").text
        
        squad_link = "https://fbref.com" + link_tag["href"]

        team_page = scraper.get(squad_link)
        
        team_soup = BeautifulSoup(team_page.content, "html.parser")

        all_players = team_soup.find("tbody").find_all("tr")
        print("Started with team " + squad_name)
        index = 0
        for player in all_players:  
  
            player_data = {
                "Name": player.find("th", attrs={"data-stat": "player"}).get_text(strip=True),
                "Team": squad_name,
                "Nationality": player.find("td", attrs={"data-stat": "nationality"}).get_text(strip=True)[-3:], # Usually gets the country code like 'EGY'
                "Position": player.find("td", attrs={"data-stat": "position"}).get_text(strip=True),
                "Age": player.find("td", attrs={"data-stat": "age"}).get_text(strip=True),
                "Matches Played": player.find("td", attrs={"data-stat": "games"}).get_text(strip=True),
                "Starts": player.find("td", attrs={"data-stat": "games_starts"}).get_text(strip=True),
                "Minutes": player.find("td", attrs={"data-stat": "minutes"}).get_text(strip=True),
                "90s Played": player.find("td", attrs={"data-stat": "minutes_90s"}).get_text(strip=True),
                "Goals": player.find("td", attrs={"data-stat": "goals"}).get_text(strip=True),
                "Assists": player.find("td", attrs={"data-stat": "assists"}).get_text(strip=True),
                "G+A": player.find("td", attrs={"data-stat": "goals_assists"}).get_text(strip=True),
                "Non-Penalty Goals": player.find("td", attrs={"data-stat": "goals_pens"}).get_text(strip=True),
                "Penalties Scored": player.find("td", attrs={"data-stat": "pens_made"}).get_text(strip=True),
                "Penalties Attempted": player.find("td", attrs={"data-stat": "pens_att"}).get_text(strip=True),
                "Yellow Cards": player.find("td", attrs={"data-stat": "cards_yellow"}).get_text(strip=True),
                "Red Cards": player.find("td", attrs={"data-stat": "cards_red"}).get_text(strip=True),
                "Goals per 90": player.find("td", attrs={"data-stat": "goals_per90"}).get_text(strip=True),
                "Assists per 90": player.find("td", attrs={"data-stat": "assists_per90"}).get_text(strip=True),
                "G+A per 90": player.find("td", attrs={"data-stat": "goals_assists_per90"}).get_text(strip=True),
                "G-PK per 90": player.find("td", attrs={"data-stat": "goals_pens_per90"}).get_text(strip=True),
                "G+A-PK per 90": player.find("td", attrs={"data-stat": "goals_assists_pens_per90"}).get_text(strip=True),
            }






            final_all_players.append(player_data)
            index+=1
            print(f"Added Player {index}")

        time.sleep(4)
    df = pd.DataFrame(final_all_players)
    print(f"Total players scraped: {len(df)}")
    print(df.head())

    df.to_csv("players_data.csv", index=False, encoding='utf-8-sig')
else:
    print(f"Still blocked. Status: {page.status_code}")
