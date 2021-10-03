import requests
import json
import time

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

    r = requests.get(
        f"https://discord.com/api/v9/channels/{channel_id}/messages?limit=100", headers=headers)
    content = json.loads(r.text)
    last_message = ""
    for value in content:
        last_message = value["id"]
        break
    for value in content:
        if value["author"]["username"] == "80Days":
            if (value["content"].find("has paid") != -1):
                if value["content"].find("sabotage") != -1:
                    #Add to sabo lists
                    print("sabo")
                else:
                    #Add to payment lists
                    print("payment")

    while end_reached == False:
        time.sleep(0.1)
        r = requests.get(
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
                        print("sabo")
                    else:
                        #Add to payment lists
                        print("payment")
                


retrieve_payments(wolves_commands_id)
