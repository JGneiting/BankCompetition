import random
from src.player import Player
import json

from typing import Union


class GameState:
    def __init__(self, num_rounds: int = 0, players: list[Player] = [],
                 gamestate_json: Union[str, dict] = None) -> None:
        """Initialize the game state.

        Args:
            num_rounds (int): number of rounds
            players (list[Player]): list of players
            gamestate_json (Union[str, dict], optional): game state json. Defaults to None.
        """
        if gamestate_json is not None and isinstance(gamestate_json, str):
            self.from_json(gamestate_json)
        elif gamestate_json is not None and isinstance(gamestate_json, dict):
            self.from_dict(gamestate_json)
        else:
            self.current_round = 0
            self.num_rounds = num_rounds
            self.players: list[Player] = []
            for player in players:
                self.players.append(player)
            self.__current_player_index = 0
            if not self.players:
                raise ValueError("No players")
            if len(self.players) < 2:
                raise ValueError("Not enough players")
            self.current_player = self.players[self.__current_player_index]
            self.bank: int = 0
            self.current_roll: tuple = (0, 0)
            self.current_turn = 0

    def __str__(self) -> str:
        ret_str = f"Round: {self.current_round} of {self.num_rounds}\n"
        ret_str += "Bank: " + str(self.bank) + "\n"
        ret_str += "Current player: " + self.current_player.name + "\n"
        for player in self.players:
            ret_str += player.__str__() + "\n"
        return ret_str

    def __repr__(self) -> str:
        return self.__str__()

    def next_round(self) -> None:
        self.bank = 0
        self.current_round += 1
        self.current_turn = 0
        if self.current_round >= self.num_rounds:
            return
        for player in self.players:
            player.unbank()
        self.advance_player()

    def next_turn(self) -> None:
        self.advance_player()

    def advance_player(self) -> None:
        if all(self.players):
            return
        self.__current_player_index = (
            self.__current_player_index + 1
        ) % len(self.players)
        self.current_player = self.players[self.__current_player_index]
        if self.current_player.is_banked:
            self.advance_player()

    def update_bank(self, amount: int) -> None:
        self.bank += amount

    def get_results(self) -> list[Player]:
        results = sorted(self.players, key=lambda player: player.score, reverse=True)
        return results

    def roll(self) -> tuple[int, int]:
        dice1 = random.randint(1, 6)
        dice2 = random.randint(1, 6)
        self.current_roll = (dice1, dice2)
        self.current_turn += 1
        return self.current_roll

    def from_json(json_str: str) -> "GameState":
        return GameState.from_dict(json.loads(json_str))

    def from_dict(self, gamestate_dict: dict) -> "GameState":
        self.current_round = gamestate_dict.get("current_round", 0)
        self.num_rounds = gamestate_dict.get("num_rounds", 0)
        self.__current_player_index = gamestate_dict.get("current_player_index", 0)

        players = gamestate_dict.get("players", [])
        for player in players:
            self.players.append(Player(player))
        if not self.players:
            raise ValueError("No players")
        if len(self.players) < 2:
            raise ValueError("Not enough players")
        self.current_player = gamestate_dict.get("current_player", None)
        self.bank: int = gamestate_dict.get("bank", 0)
        self.current_roll: tuple = tuple(gamestate_dict.get("current_roll", (0, 0)))
        self.current_turn = gamestate_dict.get("current_turn", 0)


class GameStateENCODER(json.JSONEncoder):
    def default(self, obj):
        if hasattr(obj, "__dict__"):
            return obj.__dict__
        return super().default(self, obj)
