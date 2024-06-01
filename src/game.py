import random
import logging
import copy

from entry import Entry
from player import Player
from gamestate import GameState


log = logging.getLogger(__name__)


class Game:
    def __init__(self, num_rounds: int, *entries: Entry) -> None:
        """Initialize the game state."""
        self.__entries: list[Entry] = [].clear()
        self.state: GameState = None
        players = []
        for entry in entries:
            try:
                entry.is_valid()
                self.__entries.append(entry)
                players.append(Player(entry.name))
                log.info("Entry passed validation: %s", entry)
                log.info("Player added: %s", entry.name)
            except Exception as e:
                log.warning("Entry failed validation: %s", entry, exc_info=e)
        try:
            self.state = GameState(num_rounds, players)
        except Exception as e:
            log.warning("Failed to initialize game state", exc_info=e)

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
        if all(self.state.players):
            self.state.next_round()
            return
        poll_again = False
        for i, player in enumerate(self.state.players):
            if not player.is_banked:
                if self.__entries[i].func(copy.deepcopy(self.state)):
                    self.state.players[i].bank(self.state.bank)
                    poll_again = True
        if poll_again:
            self.poll()

    def run(self) -> None:
        while self.state.current_round < self.state.num_rounds:
            self.roll()
            self.poll()

        results = self.state.get_results()
        print(f"{results[0].name} wins with {results[0].score} points!")
        print("Scores:")
        for player in results:
            print(f"{player.name}: {player.score}")
        # TODO: export results to a file