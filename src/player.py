import json
from typing import Union


class Player:
    def __init__(self, name: str, player_json: Union[str, dict] = None) -> None:
        if player_json is not None and isinstance(player_json, str):
            player_json = json.loads(player_json)
        elif player_json is not None and isinstance(player_json, dict):
            player_json = json.dumps(player_json)
        else:
            self.name = name
            self.score = 0
            self.is_banked = False

    def __repr__(self) -> str:
        return self.__str__()

    def __str__(self) -> str:
        return f"{self.name}: {self.score} - {self.is_banked}"

    def __bool__(self) -> bool:
        return self.is_banked

    def bank(self, amount: int) -> None:
        self.is_banked = True
        self.score += amount

    def unbank(self) -> None:
        self.is_banked = False

    def from_json(self, player_json: str) -> None:
        self.from_dict(json.loads(player_json))

    def from_dict(self, player_dict: dict) -> None:
        self.name = player_dict.get("name", "")
        self.score = player_dict.get("score", 0)
        self.is_banked = player_dict.get("is_banked", False)
