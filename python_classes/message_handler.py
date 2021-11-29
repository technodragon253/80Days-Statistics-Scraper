import time
import requests
from requests.models import Response
from python_classes.data_types import *
from python_classes.constants import *
import json
from typing import List
from datetime import datetime
import python_classes.ratelimit_handler as ratelimit_handler
rh = ratelimit_handler.main()


class main:
    def datetime_to_snowflake(self, time):
        return (int(time.timestamp() * 1000) - discord_epoch) << 22

    def handle_response_errors(self, response: Response):
        # 401 status code means invald authorization.
        if (response.status_code == 401):
            raise Exception("Invalid Auth Key!")
        elif (response.status_code == 429):  # 429 means rate limiting
            # Get the rate limit time
            limit = json.loads(response.text)["retry_after"]
            print(colors.red +
                  f"Rate limited. Sleeping {limit} seconds." + colors.default)
            time.sleep(limit)
            rh.increase_ratelimit()
            return False
        elif response.status_code != 200:
            print(response.text)
            return False
        else:
            return True

    def message_request(self, channel_id, args):
        # Get the auth key from "auth_key.txt".
        with open('auth_key.txt') as f:
            key = f.readline()

        headers = {  # Add the auth key to the headers. Kinda important.
            'authorization': key
        }
        valid_response = False
        iterations = 0
        while valid_response != True:
            rh.ratelimit()  # StopRateLimitingMe
            r = requests.get(
                f"https://discord.com/api/v9/channels/{channel_id}/messages{args}", headers=headers)
            valid_response = self.handle_response_errors(r)
            iterations += 1
            if iterations > max_retries:
                raise Exception("Max Retries Reached!")
        return r

    def message_request_between(self, server_id, start_time, end_time, channel_id, args=""):
        # Get the auth key from "auth_key.txt".
        with open('auth_key.txt') as f:
            key = f.readline()

        headers = {  # Add the auth key to the headers. Kinda important.
            'authorization': key
        }
        valid_response = False
        iterations = 0
        while valid_response != True:
            rh.ratelimit()  # StopRateLimitingMe
            r = requests.get(
                f"https://discord.com/api/v9/guilds/{server_id}/messages/search?min_id={start_time}&max_id={end_time}&channel_id={channel_id}{args}", headers=headers)
            valid_response = self.handle_response_errors(r)
            iterations += 1
            if iterations > max_retries:
                raise Exception("Max Retries Reached!")
        return r

    def account_request(self, account_id):
        # Get the auth key from "auth_key.txt".
        with open('auth_key.txt') as f:
            key = f.readline()

        headers = {  # Add the auth key to the headers. Kinda important.
            'authorization': key
        }
        valid_response = False
        iterations = 0
        while valid_response != True:
            rh.ratelimit()  # StopRateLimitingMe
            r = requests.get(
                f"https://discord.com/api/v9/users/{account_id}/profile?with_mutual_guilds=false", headers=headers)
            valid_response = self.handle_response_errors(r)
            iterations += 1
            if iterations > max_retries:
                raise Exception("Max Retries Reached!")
        return r

    def parse_payment(self, message, team):
        if message["author"]["username"] == "80Days":
            if (message["content"].find("has paid") != -1):
                if message["content"].find("sabotage") != -1:
                    pass
                else:
                    v = message["content"].split("**")

                    amount = int(v[1])
                    # Remove the random other characters from the player id. Thanks StackOverFlow: https://stackoverflow.com/questions/3939361/remove-specific-characters-from-a-string-in-python#3939381
                    id = (message["content"].split()[0]).translate(
                        str.maketrans('', '', '<@!>'))
                    payment = Payment(datetime.fromisoformat(
                        message["timestamp"]), id, amount, team, v[3])
                    return payment

    def parse_sabotage(self, message):
        if message["author"]["username"] == "80Days":
            if (message["content"].find("has paid") != -1):
                if message["content"].find("sabotage") != -1:
                    v = message["content"].split("**")

                    amount = int(v[1])
                    # Remove the random other characters from the player id. Thanks StackOverFlow: https://stackoverflow.com/questions/3939361/remove-specific-characters-from-a-string-in-python#3939381
                    id = (message["content"].split()[0]).translate(
                        str.maketrans('', '', '<@!>'))
                    sabo = Sabotage(datetime.fromisoformat(
                        message["timestamp"]), id, amount, v[3][:-1], v[5])
                    return sabo

    def retrive_game_endpoints(self):
        out = []
        end = None

        i = 0
        end_reached = False
        while not end_reached:
            if i == 0:
                content = json.loads(self.message_request(
                    progress_anouncements.id, "?limit=100").text)
            else:
                content = json.loads(self.message_request(
                    progress_anouncements.id, f"?before={last_message}&limit=100").text)
            i += 1

            if (content == []):
                end_reached = True
            for value in content:
                if value["author"]["username"] == "80Days":
                    if (value["content"].find("Welcome to day **1**") != -1):
                        if end != None:
                            out.append({"start_time": datetime.fromisoformat(
                                value["timestamp"]), "end_time": end})
                            end = None
                        else:
                            print("Found game in progress.")
                    elif (value["content"].find("Thank you all for playing!") != -1):
                        end = datetime.fromisoformat(value["timestamp"])

                # Set the last message to be able to find the next block of messsages.
                last_message = value["id"]
                if (int(last_message) < cut_off_id):
                    end_reached = True

        return out

    def retrive_game(self, start_date: datetime, end_date: datetime):
        game = Game(None, start_date, end_date, [])

        end = self.datetime_to_snowflake(end_date)
        start = self.datetime_to_snowflake(start_date)

        boars_place = 0
        wolves_place = 0
        stallions_place = 0

        # Get the places for all teams. 1 for first, 2 for secound, etc.

        # Need to initize this variable before it is asigned a value.
        total = 0
        offset = 0
        i = 0
        while total >= 0:
            if i == 0:  # First iteration doesn't need an offset.
                r = json.loads(self.message_request_between(
                    server_id, start, end, progress_anouncements.id).text)
                total = r["total_results"]
            else:  # Second iteration does, however.
                r = json.loads(self.message_request_between(
                    server_id, start, end, progress_anouncements.id, f"&offset={offset}").text)

            for messages in r["messages"]:
                for message in messages:
                    place = 0
                    if message["content"].find("In third place,") != -1:
                        place = 3
                        if message["content"].split()[7] == "Argent":
                            boars_place = place
                        elif message["content"].split()[7] == "Azure":
                            wolves_place = place
                        elif message["content"].split()[7] == "Crimson":
                            stallions_place = place
                    elif(message["content"].find("In second place,") != -1):
                        place = 2
                        if message["content"].split()[7] == "Argent":
                            boars_place = place
                        elif message["content"].split()[7] == "Azure":
                            wolves_place = place
                        elif message["content"].split()[7] == "Crimson":
                            stallions_place = place
                    elif(message["content"].find("Finally, in first place,") != -1):
                        place = 1
                        if message["content"].split()[5] == "Argent":
                            boars_place = place
                        elif message["content"].split()[5] == "Azure":
                            wolves_place = place
                        elif message["content"].split()[5] == "Crimson":
                            stallions_place = place
            total -= 25
            offset += 25
            i += 1

        # Get all player messages.
        for idx, (key, team) in enumerate(all_player_channels.items()):
            game.teams.append(Team(idx + 1, None, [], [], []))

            # Depending on which team we are interating over, we set the place. 1 for first, 2 for secound, etc.
            if key == 1:
                game.teams[idx].place = boars_place
            elif key == 2:
                game.teams[idx].place = wolves_place
            elif key == 3:
                game.teams[idx].place = stallions_place

            # Iterating over each channel belonging to a team.
            for channel in team:

                # Need to initize this variable before it is asigned a value.
                total = 0
                offset = 0
                i = 0
                while total >= 0:
                    if i == 0:  # First iteration doesn't need an offset.
                        r = json.loads(self.message_request_between(
                            server_id, start, end, channel.id).text)
                        total = r["total_results"]
                    else:  # Second iteration does, however.
                        r = json.loads(self.message_request_between(
                            server_id, start, end, channel.id, f"&offset={offset}").text)
                    for messages in r["messages"]:
                        for message in messages:
                            payment = self.parse_payment(message, idx + 1)
                            sabotage = self.parse_sabotage(message)
                            if (payment != None):
                                game.teams[idx].payments.append(payment)
                                if not game.teams[idx].players.__contains__(Player(payment.player_id, message["mentions"][0]["username"])):
                                    game.teams[idx].players.append(
                                        Player(payment.player_id, message["mentions"][0]["username"]))
                            if (sabotage != None):
                                game.teams[idx].sabotages.append(sabotage)
                                if not game.teams[idx].players.__contains__(Player(sabotage.player_id, message["mentions"][0]["username"])):
                                    game.teams[idx].players.append(
                                        Player(sabotage.player_id, message["mentions"][0]["username"]))
                    total -= 25
                    offset += 25
                    i += 1

        return game
