from dataclasses import dataclass
from datetime import datetime
from typing import List

@dataclass
class Payment:
    time: datetime
    player_id: int
    amount: int
    team: int
    location: str
    
    def to_dict(self):
        return {"time": self.time.isoformat(), "player_id": self.player_id, "amount": self.amount, "team": self.team, "location": self.location}
    def copy(self):
        return Payment(self.time.isoformat(), self.player_id, self.amount, self.team, self.location)


@dataclass
class Sabotage:
    time: datetime
    player_id: int
    amount: int
    against: str
    location: str
    
    def to_dict(self):
        return {"time": self.time.isoformat(), "player_id": self.player_id, "amount": self.amount, "against": self.against, "location": self.location}
    def copy(self):
        return Sabotage(self.time.isoformat(), self.player_id, self.amount, self.against, self.location)


@dataclass
class Channel:
    id: int
    name: str
    team: str


@dataclass
class Player:
    id: int
    name: str

    def to_dict(self):
        return self.__dict__


@dataclass
class Team:
    id: int
    place: int #1 being first place, 2 being second, etc.
    players: List[Player]
    payments: List[Payment]
    sabotages: List[Sabotage]

    def to_dict(self):
        players = []
        for player in self.players:
            players.append(player.to_dict())
        payments = []
        for payment in self.payments:
            payments.append(payment.to_dict())
        sabotages = []
        for sabotage in self.sabotages:
            sabotages.append(sabotage.to_dict())
        return {"id": self.id, "place": self.place, "players": players, "payments": payments, "sabotages": sabotages}


@dataclass
class Game:
    id: int
    start_time: datetime
    end_time: datetime
    teams: List[Team]

    def to_dict(self):
        teams = []
        for team in self.teams:
            teams.append(team.to_dict())
        return {"start_time": self.start_time.isoformat(), "end_time": self.end_time.isoformat(), "teams": teams}

def from_json(json: dict) -> List[Game]:
    out = []
    for game in json:
        g = Game(None, datetime.fromisoformat(game["start_time"]), datetime.fromisoformat(game["end_time"]), [])
        for team in game["teams"]:
            t = Team(team["id"], team["place"], [], [], [])
            for player in team["players"]:
                p = Player(player["id"], player["name"])
                t.players.append(p)
            for payment in team["payments"]:
                p = Payment(datetime.fromisoformat(payment["time"]), payment["player_id"], payment["amount"], payment["team"], payment["location"])
                t.payments.append(p)
                del(p)
            for sabotage in team["sabotages"]:
                s = Sabotage(datetime.fromisoformat(sabotage["time"]), sabotage["player_id"], sabotage["amount"], sabotage["against"], sabotage["location"])
                t.sabotages.append(s)
                del(s)
            g.teams.append(t)
        out.append(g)
    return out

