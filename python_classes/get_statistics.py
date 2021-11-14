import json
from constants import colors

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
Enter the player id of the player you want to look up.
""")
        #Find the games whrere the player did things.
        games_to_scan = []
        players_sabotages = []
        players_payments = []
        for game in data:
            for team in game["teams"]:
                for player in team["players"]:
                    if player["id"] == i:
                        games_to_scan.append(game)
        #Find all sabotages by the player.
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
        average_sabotage = int(total_payed / number_of_payments)
        most_payed_location = max(payed_locations, key=payed_locations.get)
        most_often_location = max(often_locations, key=often_locations.get)

        print(f"""{colors.dark_green}
Payment stats:
{colors.green}{total_payed} lifetime coins payed.
{number_of_payments} indivival payments.
Biggest payment: {max_payment} coins.
Smallest payment: {min_payment} coins.
Average payment: {average_sabotage} coins.
Lifetime highest payed for location: {most_payed_location} with {payed_locations[most_payed_location]} coins payed!
Lifetime most often payed for location: {most_often_location} traveled to {often_locations[most_often_location]} times!
{colors.default}""")

        #Find sabotage stats.
        total_sabotaged = 0
        number_of_sabotages = 0
        max_sabotage = 0
        min_sabotage = 100000 #Need to set it to an obsured number so the min function works.
        average_sabotage = 0
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
        average_sabotage = int(total_sabotaged / number_of_sabotages)
        most_sabotaged_location = max(sabotaged_locations, key=sabotaged_locations.get)
        highest_sabotaged_location = max(sabotaged_locations, key=sabotaged_locations.get)

        print(f"""{colors.dark_red}
Sabotages stats:
{colors.red}{total_sabotaged} lifetime coins sabotaged.
{number_of_sabotages} indivival sabotages.
Biggest sabotage: {max_sabotage} coins.
Smallest sabotage: {min_sabotage} coins.
Average sabotage: {average_sabotage} coins.
Lifetime highest sabotaged location: {highest_sabotaged_location} with {highest_locations[highest_sabotaged_location]} coins payed!
Lifetime most often sabotaged location: {most_sabotaged_location} traveled to {sabotaged_locations[most_sabotaged_location]} times!
{colors.default}""")

        #Find win stats
        