import json
from time import time
from constants import colors
from os import name, system

def s(i):
    if i != 1:
        return "s"
    else:
        return ""

try:
    with open("../output.json", "r") as f:
        pass
except:
    i = input(f"""
No existing data found! Would you like to download the data? {colors.green}(Press 1 and Enter for yes){colors.default}
""")
    if i == 1:
        import get_data
    else:
        quit()

with open("../output.json", "r") as f:
    data = json.loads(f.read())
    i = input(f"""
What statistic would you like to get? 
{colors.green}(Press 1 for player look up){colors.default}
{colors.green}(Press 2 for team look up){colors.default}
{colors.green}(Any other key to exit){colors.default}
""")
    if i == "1":
        i = input("""
Enter the player id or name of the player you want to look up.
""")
        system('cls' if name == 'nt' else 'clear')
        #Find the games whrere the player did things.
        player_id = ""
        player_name = ""
        games_to_scan = []
        players_sabotages = []
        players_payments = []
        for game in data:
            for team in game["teams"]:
                for player in team["players"]:
                    if player_id != "":
                        if player["id"] == player_id:
                            games_to_scan.append(game)
                    elif player["id"] == i:
                        games_to_scan.append(game)
                        player_id = player["id"]
                        player_name = player["name"]
                    elif player["name"].lower() == i.lower(): #If the name of a player was entered change 'i' to be the player id.
                        i = player["id"]
                        games_to_scan.append(game)
                        player_id = player["id"]
                        player_name = player["name"]
        if games_to_scan == []:
            raise Exception("Player did nothing!")

        print(f"""{colors.purple}
Statistics for {player_name} with id of {player_id}:
        {colors.default}""")

        #Find all sabotages/payments by the player.
        for game in games_to_scan:
            for team in game["teams"]:
                for sabotage in team["sabotages"]:
                    if sabotage["player_id"] == i:
                        players_sabotages.append(sabotage)
                for payment in team["payments"]:
                    if payment["player_id"] == i:
                        players_payments.append(payment)

        #Find payment stats.
        total_payed = 0
        number_of_payments = 0
        max_payment = 0
        min_payment = 100000 #Need to set it to an obsured number so the min function works.
        average_payment = 0
        payed_locations = {}
        most_payed_location = ""
        often_locations = {}
        most_often_location = ""
        
        for payment in players_payments:
            number_of_payments += 1
            total_payed += payment["amount"]
            max_payment = max(max_payment, payment["amount"])
            min_payment = min(min_payment, payment["amount"])
            if payment["location"] in payed_locations:
                payed_locations[payment["location"]] += payment["amount"]
            else:
                payed_locations[payment["location"]] =  payment["amount"]
            if payment["location"] in often_locations:
                often_locations[payment["location"]] += 1
            else:
                often_locations[payment["location"]] =  1
        average_payment = int(total_payed / number_of_payments)
        most_payed_location = max(payed_locations, key=payed_locations.get)
        most_often_location = max(often_locations, key=often_locations.get)

        print(f"""{colors.dark_green}
Payment stats:
{colors.green}{total_payed} lifetime coin{s(total_payed)} payed.
{number_of_payments} indivival payment{s(number_of_payments)}.
Biggest payment: {max_payment} coin{s(max_payment)}.
Smallest payment: {min_payment} coin{s(min_payment)}.
Average payment: {average_payment} coin{s(average_payment)}.
Lifetime highest payed for location: {most_payed_location} with {payed_locations[most_payed_location]} coin{s(payed_locations[most_payed_location])} payed!
Lifetime most often payed for location: {most_often_location} traveled to {often_locations[most_often_location]} time{s(often_locations[most_often_location])}!
{colors.default}""")

        #Find sabotage stats.
        total_sabotaged = 0
        number_of_sabotages = 0
        max_sabotage = 0
        min_sabotage = 100000 #Need to set it to an obsured number so the min function works.
        average_payment = 0
        sabotaged_locations = {}
        most_sabotaged_location = ""
        highest_locations = {}
        highest_sabotaged_location = ""
        
        for sabotage in players_sabotages:
            number_of_sabotages += 1
            total_sabotaged += sabotage["amount"]
            max_sabotage = max(max_sabotage, sabotage["amount"])
            min_sabotage = min(min_sabotage, sabotage["amount"])
            if sabotage["location"] in highest_locations:
                highest_locations[sabotage["location"]] += sabotage["amount"]
            else:
                highest_locations[sabotage["location"]] =  sabotage["amount"]
            if sabotage["location"] in sabotaged_locations:
                sabotaged_locations[sabotage["location"]] += 1
            else:
                sabotaged_locations[sabotage["location"]] =  1
        average_payment = int(total_sabotaged / number_of_sabotages)
        most_sabotaged_location = max(sabotaged_locations, key=sabotaged_locations.get)
        highest_sabotaged_location = max(sabotaged_locations, key=sabotaged_locations.get)

        print(f"""{colors.dark_red}
Sabotages stats:
{colors.red}{total_sabotaged} lifetime coin{s(total_sabotaged)} sabotaged.
{number_of_sabotages} indivival sabotages{s(number_of_sabotages)}.
Biggest sabotage: {max_sabotage} coin{s(max_sabotage)}.
Smallest sabotage: {min_sabotage} coin{s(min_sabotage)}.
Average sabotage: {average_payment} coin{s(average_payment)}.
Lifetime highest total sabotaged location: {highest_sabotaged_location} with {highest_locations[highest_sabotaged_location]} coin{s(highest_locations[highest_sabotaged_location])} sabotaged!
Lifetime most often sabotaged location: {most_sabotaged_location} sabotaged {sabotaged_locations[most_sabotaged_location]} time{s(sabotaged_locations[most_sabotaged_location])}!
{colors.default}""")

        #Find win and team stats
        total_wins = 0
        total_games = 0
        win_rate = 0
        times_boars = 0
        times_wolves = 0
        times_stallions = 0

        for game in games_to_scan:
            for iter, team in enumerate(game["teams"]):
                for player in team["players"]:
                    if player["id"] == i:
                        total_games += 1
                        if team["place"] == 1:
                            total_wins += 1
                        if iter == 0:
                            times_boars += 1
                        elif iter == 1:
                            times_wolves += 1
                        elif iter == 2:
                            times_stallions += 1
        
        win_rate = (total_wins / total_games) * 100

        print(f"""{colors.dark_blue}
Win stats:
{colors.blue}{total_wins} total win{s(total_wins)}.
{total_games} total game{s(total_games)}.
{win_rate}% win rate.

{colors.dark_yellow}
Team stats:
{colors.yellow}Player was on the {colors.default}Argent Boars{colors.yellow} {times_boars} time{s(times_boars)}!
Player was on the {colors.cyan}Azure Wolves{colors.yellow} {times_wolves} time{s(times_wolves)}!
Player was on the {colors.red}Crimson Stallions{colors.yellow} {times_stallions} time{s(times_stallions)}!
{colors.default}""")
    elif i == 2:
        print("This feature is not yet implemented.")