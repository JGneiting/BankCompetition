from gamestate import GameState
from entry import Entry


class Klink(Entry):
    def __init__(self, name: str) -> None:
        super().__init__(name)
        self.number_of_nines = 0
        self.current_round = 0
        self.nine_threshold = 5

    def bank(self, state: GameState) -> bool:
        if state.current_round != self.current_round:
            self.current_round = state.current_round
            self.number_of_nines = 0
        if sum(state.current_roll) == 9:
            self.number_of_nines += 1
        if self.number_of_nines >= self.nine_threshold:
            return True
        return False


def main(name: str) -> Klink:
    return Klink(name)
