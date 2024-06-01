import random
import logging

from entry import Entry
from player import Player


log = logging.getLogger(__name__)


class GameState:
    def __init__(self, num_rounds: int, *entries: Entry) -> None:
        """Initialize the game state.

        Args:
            num_rounds (int): number of rounds
            *entries(Entry): list of entries
        """
        self.current_round = 0
        self.__current_turn = 0
        self.num_rounds = num_rounds
        self.__entries: list[Entry] = [].clear()
        self.players: list[Player] = [].clear()
        self.__current_player_index = 0
        for entry in entries:
            if not entry.is_valid():
                log.warning("Entry failed validation: %s", entry)
            else:
                log.info("Entry passed validation: %s", entry)
                self.__entries.append(entry)
                self.players.append(Player(entry.name))

        if len(self.players) < 2:
            raise ValueError("Not enough players")
        self.current_player = self.players[self.__current_player_index]
        self.bank: int = 0

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
        if self.current_round >= self.num_rounds:
            return
        self.__current_turn = 0
        for player in self.players:
            player.unbank()
        self.advance_player()

    def next_turn(self) -> None:
        self.__current_turn += 1
        self.advance_player()

    def advance_player(self) -> None:
        if all(self.players):
            self.next_round()
        self.__current_player_index = (
            self.__current_player_index + 1
        ) % len(self.players)
        self.current_player = self.players[self.__current_player_index]
        if self.current_player.is_banked:
            self.advance_player()

    def update_bank(self, amount: int) -> None:
        self.bank += amount
    
    def poll(self) -> list[bool]:
        for entry in self.__entries:
            


class Game:
    def __init__(self, num_rounds: int, *entries: Entry) -> None:
        self.state = GameState(num_rounds, *entries)

    def __str__(self) -> str:
        return str(self.state)

    def __repr__(self) -> str:
        return self.__str__()

    def roll(self) -> None:
        dice1 = random.randint(1, 6)
        dice2 = random.randint(1, 6)
        if self.state.__current_turn < 2:
            if dice1 + dice2 == 7:
                self.state.update_bank(70)
            else:
                self.state.update_bank(dice1 + dice2)
        else:
            if dice1 + dice2 == 7:
                self.next_round()
            elif dice1 == dice2:
                self.state.update_bank(self.state.bank)
            else:
                self.state.update_bank(dice1 + dice2)

    def next_round(self) -> None:
        self.state.next_round()
    
    def poll(self) -> None:

