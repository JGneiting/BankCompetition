from gamestate import GameState
from entry import Entry


class TestEntry(Entry):
    def __init__(self, name: str) -> None:
        super().__init__(name)
        self.current_round = 0
        self.curr_turn = 0
        self.threshold = 17

    def bank(self, state: GameState) -> bool:
        if state.current_round != self.current_round:
            self.current_round = state.current_round
            self.curr_turn = 0
        self.curr_turn += 1
        if self.current_round == state.num_rounds - 2:
            if self.am_winning(state):
                if any(player.is_banked for player in state.players):
                    return True
                else:
                    return False
            else:
                if self.curr_turn == self.threshold:
                    return True
        elif self.current_round == state.num_rounds - 1:
            if self.am_winning(state):
                if any(player.is_banked for player in state.players):
                    return True
                else:
                    return False
            else:
                if self.curr_turn >= self.threshold and state.bank >= 300:
                    return True
        elif self.curr_turn == self.threshold:
            return True
        else:
            return False

        return True

    def am_winning(self, state: GameState) -> bool:
        my_index = self.get_my_index(state)
        if self.is_highest_score(state.players, my_index):
            return True
        return False

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


def main(name: str) -> TestEntry:
    return TestEntry(name)
