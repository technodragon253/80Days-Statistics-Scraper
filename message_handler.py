import time
import requests
from dataclasses import dataclass
import json

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

@dataclass
class Channel:
    id: str
    name: str
    team: str

def message_request(headers, channel_id, args):
    r = requests.get(
                f"https://discord.com/api/v9/channels/{channel_id}/messages{args}", headers=headers)
    if (r.status_code == 401): #401 status code means invald authorization.
        raise Exception("Invalid Auth Key!")
    return r

def retrieve_payments(channel: Channel):
    out = []
    
    with open('auth_key.txt') as f: #Get the auth key from "auth_key.txt".
        key = f.readline()

    headers = { #Add the auth key to the headers. Kinda important.
        'authorization': key 
    }

    end_reached = False
    total_payments = 0 #The total number of payments.

    i = 0
    while end_reached == False:
        time.sleep(0.1) #StopRateLimitingMe
        if i == 0:  
            content = json.loads(message_request(headers,channel.id,"?limit=100").text)
        else:
            content = json.loads(message_request(headers,channel.id, f"?before={last_message}&limit=100").text)
        i += 1

        if (content == []):
            end_reached = True
            break
        for value in content:
            last_message = value["id"]
        for value in content:
            if value["author"]["username"] == "80Days":
                if (value["content"].find("has paid") != -1):
                    if value["content"].find("sabotage") != -1:
                        pass
                    else:
                        total_payments += 1
                        
                        v = value["content"].split("**")

                        amount = int(v[1]) 
                        payment = Payment(channel.team, value["timestamp"], value["content"].split()[0], amount, v[3])
                        out.append(payment)

    print(f"\rNumber of Payments in {channel.name}: {total_payments}") #Uses \r to get rid of the slash from the loading animation.

    return out

def retrieve_sabotages(channel: Channel):
    out = []

    with open('auth_key.txt') as f: #Get the auth key from "auth_key.txt".
        key = f.readline()

    headers = { #Add the auth key to the headers. Kinda important.
        'authorization': key 
    }

    end_reached = False
    total_sabotages = 0 #The total number of sabotages.

    i = 0
    while end_reached == False:
        time.sleep(0.1) #StopRateLimitingMe
        if i == 0:  
            content = json.loads(message_request(headers,channel.id,"?limit=100").text)
        else:
            content = json.loads(message_request(headers,channel.id, f"?before={last_message}&limit=100").text)
        i += 1

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
                        sabo = Sabotage(channel.team, value["timestamp"], value["content"].split()[0], amount, v[3], v[5])
                        out.append(sabo)


    print(f"\rNumber of Sabotages in {channel.name}: {total_sabotages}") #Uses \r to get rid of the slash from the loading animation.

    return out

def retrieve_game_dates(channel: Channel):
    out = []

    with open('auth_key.txt') as f: #Get the auth key from "auth_key.txt".
        key = f.readline()

    headers = { #Add the auth key to the headers. Kinda important.
        'authorization': key 
    }

    end_reached = False
    total_games = 0

    i = 0
    while end_reached == False:
        time.sleep(0.1) #StopRateLimitingMe
        if i == 0:  
            content = json.loads(message_request(headers,channel.id,"?limit=100").text)
        else:
            content = json.loads(message_request(headers,channel.id, f"?before={last_message}&limit=100").text)
        i += 1

        if (content == []):
            end_reached = True
            break
        for value in content:
            if value["author"]["username"] == "80Days":
                if (value["content"].find("Welcome to day **1**") != -1):
                    total_games += 1
                    out.append(value["timestamp"])
            last_message = value["id"] #Set the last message to be able to find the next block of messsages.


    print(f"\rNumber of Games: {total_games}") #Uses \r to get rid of the slash from the loading animation.

    return out

def parse_game_data(data, timestamps):
    out = {}
    i = 0
    n = 0
    for d in data:
        if (max(d.time, timestamps[i]) != timestamps[i]): #If d is newer than the timestamp.
            if (i > 0): #Make sure there is an older value.
                if (max(d.time, timestamps[i - 1]) == timestamps[i - 1]): #If d is older than the timestamp before.
                    out[timestamps[i]][n] = d
            else: #If not, we can just add it to the section of the dictionary.
                out[str(timestamps[i])][str(n)] = d
            n += 1
        else:
            i += 1
            print("i++")
