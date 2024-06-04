from gamestate import GameState
from entry import Entry


class EndGame(Entry):
    def __init__(self, name: str) -> None:
        super().__init__(name)
        self.current_round = 0
        self.winning_at_start = None
        self.minimum_threshold = 120

    def bank(self, state: GameState) -> bool:
        if state.current_round != self.current_round:
            self.current_round = state.current_round
            self.winning_at_start = None

        if self.winning_at_start is None:
            self.winning_at_start = self.am_winning(state)
        if state.current_turn < 3:
            return False
        if self.am_winning(state):
            return False
        elif self.winning_at_start:
            return self.can_bank(state)
        elif self.will_be_highest_score(state):
            return self.can_bank(state)
        else:
            return False

    def can_bank(self, state: GameState) -> bool:
        if self.minimum_threshold < state.bank:
            return True
        return False

    def is_last_round(self, state: GameState) -> bool:
        return state.current_round == state.num_rounds - 1

    def is_second_to_last_round(self, state: GameState) -> bool:
        return state.current_round == state.num_rounds - 2

    def am_winning(self, state: GameState) -> bool:
        my_index = self.get_my_index(state)
        if self.is_highest_score(state.players, my_index):
            return True
        return False

    def will_be_highest_score(self, state: GameState) -> bool:
        my_index = self.get_my_index(state)
        if self.is_highest_score(state.players, my_index):
            return True
        else:
            score = state.players[my_index].score + state.bank
            return all(score >= player.score for i, player in enumerate(state.players) if i != my_index)

    def is_highest_score(self, players: list, index):
        # Get the score of the player at the specified index
        player_score = players[index].score

        # Check if the score of the player at the specified index is greater than all other scores
        return all(player_score >= player.score for i, player in enumerate(players) if i != index)

    def get_my_index(self, state: GameState) -> int:
        my_index = 0
        for player in state.players:
            if player.name == self.name:
                break
            my_index += 1
        return my_index


def main(name: str) -> EndGame:
    return EndGame(name)
