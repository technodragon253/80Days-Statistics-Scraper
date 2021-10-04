import requests
import json
import time
from dataclasses import dataclass

import loading_animation
l = loading_animation.loading_animation()
l.start()  

@dataclass
class Payment:
    time: str
    player_id: str
    amount: int
    location: str

    def to_dict(self):
        return {"time": self.time, "player_id": self.player_id, "amount": self.amount, "location": self.location}

@dataclass
class Sabotage:
    time: str
    player_id: str
    amount: int
    against: str
    location: str

    def to_dict(self):
        return {"time": self.time, "player_id": self.player_id, "amount": self.amount, "against": self.against, "location": self.location}

payments = []
sabotages = []

key = ""
with open('auth_key') as f:
    key = f.readline()

progress_anouncements_id = "614336214786375682"
wolves_general_id = "614345822477352974"
wolves_commands_id = "614350640264511508"


def retrieve_payments(channel_id):
    headers = {
        'authorization': key
    }

    end_reached = False

    i = 0
    while end_reached == False:
        time.sleep(0.1)
        if i == 0:  
            r = requests.get( #If it is the first iteration, then we need to load the initial messages.
                f"https://discord.com/api/v9/channels/{channel_id}/messages?limit=100", headers=headers)
        else:
            r = requests.get( #In subsequent iterations we have been able to get a "last_message" and use that to search for more messages. 
                f"https://discord.com/api/v9/channels/{channel_id}/messages?before={last_message}&limit=100", headers=headers)
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
                        #Add to sabo lists
                        i = value["content"].split("**")

                        amount = int(i[1]) 
                        sabo = Sabotage(value["timestamp"], value["content"].split()[0], amount, i[3], i[5])
                        sabotages.append(sabo)
                    else:
                        #Add to payment lists
                        i = value["content"].split("**")

                        amount = int(i[1]) 
                        payment = Payment(value["timestamp"], value["content"].split()[0], amount, i[3])
                        payments.append(payment)
                    


retrieve_payments(wolves_commands_id)
with open("sabotages.json", "w") as f:
    results = [obj.to_dict() for obj in sabotages]
    results.sort(key=lambda obj: obj["time"])
    json.dump(results, f, indent=4)
with open("payments.json", "w") as f:
    results = [obj.to_dict() for obj in payments]
    results.sort(key=lambda obj: obj["time"])
    json.dump(results, f, indent=4)
