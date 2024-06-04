from gamestate import GameState
from entry import Entry

# Scrooge - never wants to risk losing any points at all. Always banks on the third roll.


class Scrooge(Entry):
    def __init__(self, name: str) -> None:
        super().__init__(name)
        self.current_round = 0
        self.roll_count = 0
        self.print_debug_info = True  # Set this to True if you want to see debug information

    def bank(self, state: GameState) -> bool:
        if state.current_round != self.current_round:
            self.current_round = state.current_round
            if self.print_debug_info:
                print(f"Starting new round, resetting roll count")
            self.roll_count = 0
        if self.current_round == 0 and self.roll_count == 0:
            if self.print_debug_info:
                print(f"Start of game info:")
            my_index = self.get_my_index(state)
            if self.print_debug_info:
                print(f"   My index: {my_index}")
        my_score = self.get_my_score(state)
        if self.print_debug_info:
            print(f"Round #: {self.current_round}, Roll #: {self.roll_count}, Current score: {my_score}, Dice : ({state.current_roll[0]}, {state.current_roll[1]})")
        self.roll_count += 1  #FIXME: Use state.current_roll to get the current roll.
        if self.roll_count <= 2:
            if self.print_debug_info:
                print(f"Banking False")
            return False
        if self.print_debug_info:
            print(f"Banking True")
        return True

    def get_my_score(self, state: GameState) -> int:
        my_index = self.get_my_index(state)
        my_score = state.players[my_index].score
        return my_score

    def get_my_index(self, state: GameState) -> int:
        my_index = 0
        for player in state.players:
            if player.name == self.name:
                break
            my_index += 1
        return my_index


def main(name: str) -> Scrooge:
    return Scrooge(name)
