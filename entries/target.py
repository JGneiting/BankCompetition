from gamestate import GameState
from entry import Entry


class Target(Entry):
    def __init__(self, name: str) -> None:
        super().__init__(name)
        self.current_round = 0
        self.base_target = 1700
        self.target_score = None
        self.winning_at_start = None

    def bank(self, state: GameState) -> bool:
        if self.target_score is None:
            self.target_score = self.base_target + ((state.num_rounds - 3) * 70)
        if state.current_round != self.current_round:
            self.current_round = state.current_round
            self.winning_at_start = None

        if self.winning_at_start is None:
            self.winning_at_start = self.am_winning(state)
        if state.current_turn < 3:
            return False
        if self.is_last_round(state):
            if self.am_winning(state):
                return False
            elif self.winning_at_start:
                return True
            elif self.will_be_highest_score(state):
                return True
            else:
                return False
        elif self.is_second_to_last_round(state):
            if self.am_winning(state):
                return False
            elif self.will_be_highest_score(state):
                return True
        else:
            round_target = self.target_score / (state.num_rounds - 3) * self.current_round
            my_current_score = state.players[self.get_my_index(state)].score
            if my_current_score + state.bank >= round_target:
                return True
            else:
                return False
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


def main(name: str) -> Target:
    return Target(name)
