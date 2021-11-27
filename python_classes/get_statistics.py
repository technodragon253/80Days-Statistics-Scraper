import json
from python_classes.constants import colors, team_lookup_table
from os import name, system
import python_classes.data_types as data_types
from python_classes.data_types import Payment, Sabotage

#Short function for gammer stuff.
def s(i):
    if i != 1:
        return "s"
    else:
        return ""

#Short function for player name look ups.
player_lookup_table = {}
def p(player_id):
    try:
        return player_lookup_table[player_id]
    except:
        return str(player_id)

#Short function for team name look up.
def t(team_id):
    try:
        return team_lookup_table[team_id]
    except:
        return team_id

try:
    with open("output.json", "r") as f:
        pass
except:
    i = input(f"""
No existing data found! Would you like to download the data? {colors.green}(Press 1 and Enter for yes){colors.default}
""")
    if i == 1:
        import python_classes.get_data
    else:
        quit()

with open("output.json", "r") as f:
    data = data_types.from_json(json.loads(f.read()))
i = input(f"""
What statistic would you like to get? 
{colors.green}(Press '1' and 'Enter' for player look up){colors.default}
{colors.green}(Press '2' and 'Enter' for team look up){colors.default}
{colors.green}(Press '3' and 'Enter' for hall of fame){colors.default}
{colors.green}(Press 'Enter' to exit){colors.default}
""")
#Get the player lookup table
for game in data:
    for team in game.teams:
        for player in team.players:
            if player.id != "" or player.id != None:
                if player.name != "" or player.name != None:
                    player_lookup_table[player.id] = player.name

#Further user prompting
if i == "1":
    i = input("""
Enter the player id or name of the player you want to look up.
""")
    system('cls' if name == 'nt' else 'clear')
    #Find all the info we need from the data.
    player_id = ""
    player_name = ""
    players_sabotages = []
    players_payments = []
    total_wins = 0
    total_games = 0
    win_rate = 0
    times_boars = 0
    times_wolves = 0
    times_stallions = 0
    for game in data:
        for team in game.teams:
            #Find player sabotages.
            for sabotage in team.sabotages:
                if player_id != "": #If the player id has been found,
                    if sabotage.player_id == player_id: #Check if the player were looking for is the player we're iterating over.
                        players_sabotages.append(sabotage)
                elif sabotage.player_id == i:
                    players_sabotages.append(sabotage)
                    player_id = sabotage.player_id
                    player_name = p(sabotage.player_id)
                elif p(sabotage.player_id).lower() == i.lower(): #If the name of a player was entered change 'i' to be the player id.
                    players_sabotages.append(sabotage)
                    player_id = sabotage.player_id
                    player_name = p(sabotage.player_id)
            #Find player payments.
            for payment in team.payments:
                if player_id != "": #If the player id has been found,
                    if payment.player_id == player_id: #Check if the player were looking for is the player we're iterating over.
                        players_payments.append(payment)
                elif payment.player_id == i:
                    players_payments.append(payment)
                    player_id = payment.player_id
                    player_name = p(payment.player_id)
                elif p(payment.player_id).lower() == i.lower(): #If the name of a player was entered change 'i' to be the player id.
                    players_payments.append(payment)
                    player_id = payment.player_id
                    player_name = p(payment.player_id)
                    
            #Find the teams the player was on.
            for player in team.players:
                if player_id != "":
                    if player.id == player_id:
                        total_games += 1
                        if team.place == 1:
                            total_wins += 1
                        if team.id == 1:
                            times_boars += 1
                        elif team.id == 2:
                            times_wolves += 1
                        elif team.id == 3:
                            times_stallions += 1
                elif player.id == i:
                    player_id = player.id
                    player_name = player.name
                    if player.id == player_id:
                        total_games += 1
                        if team.place == 1:
                            total_wins += 1
                        if team.id == 1:
                            times_boars += 1
                        elif team.id == 2:
                            times_wolves += 1
                        elif team.id == 3:
                            times_stallions += 1
                elif player.name.lower() == i.lower():
                    player_id = player.id
                    player_name = player.name
                    if player.id == player_id:
                        total_games += 1
                        if team.place == 1:
                            total_wins += 1
                        if team.id == 1:
                            times_boars += 1
                        elif team.id == 2:
                            times_wolves += 1
                        elif team.id == 3:
                            times_stallions += 1
    if total_games == 0:
        print(f"{colors.red}Player, '{i}', hasn't played any games!{colors.default}")
        input("\nPress Enter to Exit...")
        quit()
    win_rate = (total_wins / total_games) * 100

    #Find payment stats.
    total_payed = 0
    number_of_payments = 0
    max_payment = 0
    min_payment = 1000000 #Need to set it to an obsured number so the min function works.
    average_payment = 0
    payed_locations = {}
    most_payed_location = ""
    often_locations = {}
    most_often_location = ""
    
    for payment in players_payments:
        number_of_payments += 1
        total_payed += payment.amount
        max_payment = max(max_payment, payment.amount)
        min_payment = min(min_payment, payment.amount)
        if payment.location in payed_locations:
            payed_locations[payment.location] += payment.amount
        else:
            payed_locations[payment.location] =  payment.amount
        if payment.location in often_locations:
            often_locations[payment.location] += 1
        else:
            often_locations[payment.location] =  1
    average_payment = int(total_payed / number_of_payments)
    most_payed_location = max(payed_locations, key=payed_locations.get)
    most_often_location = max(often_locations, key=often_locations.get)

    #Find sabotage stats.
    total_sabotaged = 0
    number_of_sabotages = 0
    max_sabotage = 0
    min_sabotage = 100000 #Need to set it to an absurd number so the min function works.
    average_payment = 0
    sabotaged_locations = {}
    most_sabotaged_location = ""
    highest_locations = {}
    highest_sabotaged_location = ""
    
    for sabotage in players_sabotages:
        number_of_sabotages += 1
        total_sabotaged += sabotage.amount
        max_sabotage = max(max_sabotage, sabotage.amount)
        min_sabotage = min(min_sabotage, sabotage.amount)
        if sabotage.location in highest_locations:
            highest_locations[sabotage.location] += sabotage.amount
        else:
            highest_locations[sabotage.location] =  sabotage.amount
        if sabotage.location in sabotaged_locations:
            sabotaged_locations[sabotage.location] += 1
        else:
            sabotaged_locations[sabotage.location] =  1
    average_payment = int(total_sabotaged / number_of_sabotages)
    most_sabotaged_location = max(sabotaged_locations, key=sabotaged_locations.get)
    highest_sabotaged_location = max(sabotaged_locations, key=sabotaged_locations.get)

    #Print way too many statistics!
    print(f"""{colors.purple}
Statistics for "{player_name}" with id of {player_id}:

{colors.dark_green}
Payment stats:
{colors.green}{total_payed} lifetime coin{s(total_payed)} payed.
{number_of_payments} indivival payment{s(number_of_payments)}.
Biggest payment: {max_payment} coin{s(max_payment)}.
Smallest payment: {min_payment} coin{s(min_payment)}.
Average payment: {average_payment} coin{s(average_payment)}.
Lifetime highest payed for location: {most_payed_location} with {payed_locations[most_payed_location]} coin{s(payed_locations[most_payed_location])} payed!
Lifetime most often payed for location: {most_often_location} traveled to {often_locations[most_often_location]} time{s(often_locations[most_often_location])}!

{colors.dark_red}
Sabotages stats:
{colors.red}{total_sabotaged} lifetime coin{s(total_sabotaged)} sabotaged.
{number_of_sabotages} indivival sabotages{s(number_of_sabotages)}.
Biggest sabotage: {max_sabotage} coin{s(max_sabotage)}.
Smallest sabotage: {min_sabotage} coin{s(min_sabotage)}.
Average sabotage: {average_payment} coin{s(average_payment)}.
Lifetime highest total sabotaged location: {highest_sabotaged_location} with {highest_locations[highest_sabotaged_location]} coin{s(highest_locations[highest_sabotaged_location])} sabotaged!
Lifetime most often sabotaged location: {most_sabotaged_location} sabotaged {sabotaged_locations[most_sabotaged_location]} time{s(sabotaged_locations[most_sabotaged_location])}!

{colors.dark_yellow}
Win stats:
{colors.yellow}{total_wins} total win{s(total_wins)}.
{total_games} total game{s(total_games)}.
{round(win_rate, 2)}% win rate.

{colors.dark_blue}
Team stats:
{colors.blue}Player was on the {colors.default}Argent Boars{colors.blue} {times_boars} time{s(times_boars)}!
Player was on the {colors.cyan}Azure Wolves{colors.blue} {times_wolves} time{s(times_wolves)}!
Player was on the {colors.red}Crimson Stallions{colors.blue} {times_stallions} time{s(times_stallions)}!
{colors.default}""")

################################################################
################################################################
################################################################

elif i == "2":
    print("This feature is not yet implemented.")

################################################################
################################################################
################################################################

elif i == "3":
    #Get highest sabotage and payment
    all_sabotages = []
    all_payments = []
    highest_payment = Payment(None, None, 0, None, None)
    highest_sabotage = Sabotage(None, None, 0, None, None)
    for game in data:
        for team in game.teams:
            for payment in team.payments:
                player_in_list = False
                for a_payment in all_payments:
                    if a_payment.player_id == payment.player_id: #If we can find the player in already found payments, then increase the amount.
                        player_in_list = True
                        index = all_payments.index(a_payment)
                        all_payments[index].amount += payment.amount
                if not player_in_list:
                    all_payments.append(payment.copy())

                if payment.amount > highest_payment.amount:
                    highest_payment = payment
            for sabotage in team.sabotages:
                player_in_list = False
                for a_sabotage in all_sabotages:
                    if a_sabotage.player_id == sabotage.player_id: #If we can find the player in already found sabotages, then increase the amount.
                        player_in_list = True
                        index = all_sabotages.index(a_sabotage)
                        all_sabotages[index].amount += sabotage.amount
                if not player_in_list:
                    all_sabotages.append(sabotage.copy())

                if sabotage.amount > highest_sabotage.amount:
                    highest_sabotage = sabotage

    highest_lifetime_payment = Payment(None, None, 0, None, None)
    for payment in all_payments:
        if max(highest_lifetime_payment.amount, payment.amount) == payment.amount:
            highest_lifetime_payment = payment

    highest_lifetime_sabotage = Sabotage(None, None, 0, None, None)
    for sabotage in all_sabotages:
        if max(highest_lifetime_sabotage.amount, sabotage.amount) == sabotage.amount:
            highest_lifetime_sabotage = sabotage
    
    #Get win stats.
    players_wins = {}
    most_winningest_player = {"id": None, "wins": 0}
    most_winningest_player_by_percentage = {"id": None, "win_rate": 0}
    for game in data:
        for team in game.teams:
            for player in team.players:
                if player.id in players_wins:
                    if team.place == 1:
                        players_wins[player.id]["wins"] += 1
                    players_wins[player.id]["games"] += 1
                else:
                    if team.place == 1:
                        players_wins[player.id] = {"wins": 1, "games": 1}
                    else:
                        players_wins[player.id] = {"wins": 0, "games": 1}
                players_wins[player.id]["id"] = player.id
    for player in players_wins:
        if max(most_winningest_player["wins"], players_wins[player]["wins"]) == players_wins[player]["wins"]:
            most_winningest_player = players_wins[player]
        player_win_rate = players_wins[player]["wins"] / players_wins[player]["games"]
        if players_wins[player]["wins"] >= 3:
            if max(most_winningest_player_by_percentage["win_rate"], player_win_rate) == player_win_rate:
                most_winningest_player_by_percentage["id"] = players_wins[player]["id"]
                most_winningest_player_by_percentage["win_rate"] = player_win_rate
                

    print(f"""{colors.dark_green}
Payment Hall of Fame:
{colors.green}Largest payment: {highest_payment.amount} coin{s(highest_payment.amount)} by "{p(highest_payment.player_id)}" toward {highest_payment.location} at {highest_payment.time.strftime("%H:%M %b %d %Y")}!{colors.default}
{colors.green}Highest lifetime coins payed: "{p(highest_lifetime_payment.player_id)}" with {highest_lifetime_payment.amount} lifetime coin{s(highest_lifetime_payment.amount)} payed!{colors.default}

{colors.dark_red}
Sabotage Hall of Fame:
{colors.red}Largest sabotage: {highest_sabotage.amount} coin{s(highest_sabotage.amount)} by "{p(highest_sabotage.player_id)}" at {highest_sabotage.time.strftime("%H:%M %b %d %Y")} against {t(highest_sabotage.against)} trying to travel to {highest_sabotage.location}!{colors.default}
{colors.red}Highest lifetime coins sabotaged: "{p(highest_lifetime_payment.player_id)}" with {highest_lifetime_sabotage.amount} lifetime coin{s(highest_lifetime_sabotage.amount)} sabotaged!{colors.default}

{colors.dark_yellow}
{colors.yellow}Most wins: "{p(most_winningest_player["id"])}" with {most_winningest_player["wins"]} win{s(most_winningest_player["wins"])}!{colors.default}
{colors.yellow}Highest win percentage by player with more that three wins: "{p(most_winningest_player_by_percentage["id"])}" with a {round(most_winningest_player_by_percentage["win_rate"] * 100, 2)}% win rate!{colors.default}
""")