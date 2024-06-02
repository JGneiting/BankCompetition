import logging
import copy
import os
from abc import ABC, abstractmethod

from src.entry import Entry
from src.player import Player
from src.gamestate import GameState


log = logging.getLogger(__name__)


class Game(ABC):
    def __init__(self, num_rounds: int, players: list[Player]) -> None:
        """Initialize the game state."""
        self.__current_turn = 0
        self.state: GameState = None

        try:
            self.state = GameState(num_rounds, players)
        except Exception as e:
            log.warning("Failed to initialize game state", exc_info=e)

    def __str__(self) -> str:
        return str(self.state)

    def __repr__(self) -> str:
        return self.__str__()

    def roll(self) -> None:
        self.__current_turn += 1
        dice1, dice2 = self.state.roll()
        if self.__current_turn < 4:
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
        self.state.advance_player()

    def next_round(self) -> None:
        self.__current_turn = 0
        self.state.next_round()

    @abstractmethod
    def poll(self) -> None:
        pass

    def end(self) -> None:
        pass

    def run(self) -> None:
        while self.state.current_round < self.state.num_rounds:
            self.roll()
            self.poll()

        self.end()
        # results = self.state.get_results()
        # print(f"{results[0].name} wins with {results[0].score} points!")
        # print("Scores:")
        # for player in results:
        #     print(f"{player.name}: {player.score}")
        # TODO: export results to a file

    def get_winner(self) -> list[Player]:
        winners = []
        highest_score = 0
        for player in self.state.players:
            if player.score > highest_score:
                highest_score = player.score
        for player in self.state.players:
            if player.score == highest_score:
                winners.append(player)
        return winners


def get_entries(path: str, exclude: list[str]) -> list[Entry]:
    entries = []
    for entry_file in os.listdir("src/entries"):
        if entry_file.endswith(".py") and entry_file not in exclude:
            try:
                # Import the module dynamically
                module_name = entry_file[:-3]  # Strip ".py" extension
                module = __import__(f"entries.{module_name}", globals(), locals(), ["main"])

                # Check if the module has a main function
                if hasattr(module, "main"):
                    # Call the main function with the name derived from the file path
                    entry_name = module_name.capitalize()  # or use any other naming convention
                    entry_instance = module.main(entry_name)
                    entries.append(entry_instance)
            except Exception as e:
                print(f"Failed to import entry {entry_file}:", e)

    return entries


class LocalGame(Game):
    def __init__(self, num_rounds: int, *entries: Entry) -> None:
        players = []
        self.__entries = []
        for entry in entries:
            try:
                entry.is_valid()
                self.__entries.append(entry)
                players.append(Player(entry.name))
                log.info("Entry passed validation: %s", entry)
                log.info("Player added: %s", entry.name)
            except Exception as e:
                log.warning("Entry failed validation: %s", entry, exc_info=e)
        super().__init__(num_rounds, players)

    def poll(self) -> None:
        if all(self.state.players):
            self.state.next_round()
            return
        poll_again = False
        for i, player in enumerate(self.state.players):
            if not player.is_banked:
                if self.__entries[i].bank(copy.deepcopy(self.state)):
                    self.state.players[i].bank(self.state.bank)
                    poll_again = True
        if poll_again:
            self.poll()
