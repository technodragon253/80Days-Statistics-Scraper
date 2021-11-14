import json
import message_handler
from constants import *
mh = message_handler.main()
from datetime import datetime

import loading_animation
l = loading_animation.loading_animation()
l.start()  

output = []
print("Retriving game endpoints.")
endpoints = mh.retrive_game_endpoints()
print("Game endpoints retrieved.")

final_endpoints = endpoints.copy()
try:
    with open("../output.json", "r") as f:
        data = json.loads(f.read())
        game_dates_to_skip = []
        for game in data:
            game_dates_to_skip.append({"start_time": datetime.fromisoformat(game["start_time"]), "end_time": datetime.fromisoformat(game["end_time"])})
            output.append(game)
        i = 0
        for endpoint in endpoints:
            for date in game_dates_to_skip:
                if endpoint["start_time"].date() == date["start_time"].date(): #Round to the nearest day then check the dates.
                    final_endpoints.pop(i)
                    i -= 1 #Take away one from i because the list is now shorter.
                    break
            i += 1
    #Having "games found" when there was only one game found annoyed me.
    s = "s"
    if len(final_endpoints) == 1:
        s = ""
    print(f"Existing downloaded data found. Found {len(final_endpoints)} addional game{s} to be downloaded.")   
except:
    print("No existing data found.")

for i, final_endpoint in enumerate(final_endpoints):
    output.append(mh.retrive_game(final_endpoint["start_time"], final_endpoint["end_time"]).to_dict())

    #Having "games to download" when there was only one game to download annoyed me.
    if len(final_endpoints) == 1:
        print(f"Last game to download has been downloaded.")
    else:
        print(f"{i + 1} out of {len(final_endpoints)} games to download have been downloaded.")

    with open("../output.json", "w") as f:
        json.dump(output, f, indent=4)
    print("output.json updated.")

l.stop()
