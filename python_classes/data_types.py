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


@dataclass
class Sabotage:
    time: datetime
    player_id: int
    amount: int
    against: str
    location: str
    
    def to_dict(self):
        return {"time": self.time.isoformat(), "player_id": self.player_id, "amount": self.amount, "against": self.against, "location": self.location}


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
        return {"id": self.id, "players": players, "payments": payments, "sabotages": sabotages}


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

