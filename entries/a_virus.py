from gamestate import GameState
from entry import Entry


class VirusEntry(Entry):
    def __init__(self, name: str) -> None:
        super().__init__(name)
        self.current_round = 0
        self.wait_turns = 1
        self.start_wait_turn = None

    def bank(self, state: GameState) -> bool:
        if state.current_round != self.current_round:
            self.current_round = state.current_round
            self.turns_waited = 0
            self.start_wait_turn = None
        my_index = self.get_my_index(state)
        highest_index = self.get_highest_player_index(state.players)
        if my_index == highest_index:
            return False
        elif state.current_turn >= 3 and state.players[highest_index].is_banked:
            # return True
            if self.start_wait_turn is None:
                self.start_wait_turn = state.current_turn
            if state.current_turn >= self.start_wait_turn + self.wait_turns:
                return True
            else:
                return False
        return False

    def get_highest_player_index(self, players: list) -> int:
        highest_index = 0
        for i, player in enumerate(players):
            if player.score > players[highest_index].score:
                highest_index = i
        return highest_index

    def get_my_index(self, state: GameState) -> int:
        my_index = 0
        for player in state.players:
            if player.name == self.name:
                break
            my_index += 1
        return my_index


def main(name: str) -> VirusEntry:
    return VirusEntry(name)
