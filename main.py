import requests
import json
import time
from dataclasses import dataclass

import loading_animation
l = loading_animation.loading_animation()
l.start()  

@dataclass
class Payment:
    team: str
    time: str
    player_id: str
    amount: int
    location: str

    def to_dict(self):
        return {"team": self.team, "time": self.time, "player_id": self.player_id, "amount": self.amount, "location": self.location}

@dataclass
class Sabotage:
    team:str
    time: str
    player_id: str
    amount: int
    against: str
    location: str

    def to_dict(self):
        return {"team": self.team, "time": self.time, "player_id": self.player_id, "amount": self.amount, "against": self.against, "location": self.location}

payments = []
sabotages = []

progress_anouncements_id = "614336214786375682"
wolves_general_id = "614345822477352974"
wolves_commands_id = "614350640264511508"
stallions_general_id = "614345873463443457"
stallions_commands_id = "614503418299547661"
boars_general_id = "614345791133188096"
boars_commands_id = "614350341344985098"


def retrieve_payments(channel_id, channel_name, team_name):
    with open('auth_key.txt') as f: #Get the auth key from "auth_key.txt".
        key = f.readline()

    headers = { #Add the auth key to the headers. Kinda important.
        'authorization': key 
    }

    end_reached = False
    total_payments = 0 #The total number of payments.
    total_sabotages = 0 #The total number of sabotages.

    i = 0
    while end_reached == False:
        time.sleep(0.1) #StopRateLimitingMe
        if i == 0:  
            r = requests.get( #If it is the first iteration, then we need to load the initial messages.
                f"https://discord.com/api/v9/channels/{channel_id}/messages?limit=100", headers=headers)
        else:
            r = requests.get( #In subsequent iterations we have been able to get a "last_message" and use that to search for more messages. 
                f"https://discord.com/api/v9/channels/{channel_id}/messages?before={last_message}&limit=100", headers=headers)
        i += 1

        if (r.status_code == 401): #401 status code means invald authorization.
            raise Exception("Invalid Auth Key!")

        content = json.loads(r.text)
        if (content == []):
            end_reached = True
            break
        for value in content:
            last_message = value["id"]
        for value in content:
            if value["author"]["username"] == "80Days":
                if (value["content"].find("has paid") != -1):
                    if value["content"].find("sabotage") != -1:
                        total_sabotages += 1
                        
                        v = value["content"].split("**")

                        amount = int(v[1]) 
                        sabo = Sabotage(team_name, value["timestamp"], value["content"].split()[0], amount, v[3], v[5])
                        sabotages.append(sabo)
                    else:
                        total_payments += 1
                        
                        v = value["content"].split("**")

                        amount = int(v[1]) 
                        payment = Payment(team_name, value["timestamp"], value["content"].split()[0], amount, v[3])
                        payments.append(payment)

    print(f"\rNumber of Sabotages in {channel_name}: {total_sabotages}") #Uses \r to get rid of the slash from the loading animation.
    print(f"Number of Payments in {channel_name}: {total_payments}")

                    


retrieve_payments(wolves_commands_id, "Wolves Commands", "Azure Wolves")
retrieve_payments(wolves_general_id, "Wolves General", "Azure Wolves")
retrieve_payments(stallions_commands_id, "Stallions Commands", "Crimson Stallions")
retrieve_payments(stallions_general_id, "Stallions General", "Crimson Stallions")
retrieve_payments(boars_commands_id, "Boars Commands", "Argent Boars")
retrieve_payments(boars_general_id, "Boars General", "Argent Boars")
with open("sabotages.json", "w") as f:
    results = [obj.to_dict() for obj in sabotages]
    results.sort(key=lambda obj: obj["time"])
    json.dump(results, f, indent=4)
with open("payments.json", "w") as f:
    results = [obj.to_dict() for obj in payments]
    results.sort(key=lambda obj: obj["time"])
    json.dump(results, f, indent=4)
