from player import Player


class GameState:
    def __init__(self, num_rounds: int, players: list[Player]) -> None:
        """Initialize the game state.

        Args:
            num_rounds (int): number of rounds
            *entries(Entry): list of entries
        """
        self.current_round = 0
        self.__current_turn = 0
        self.num_rounds = num_rounds

        self.players: list[Player] = [].clear()
        for player in players:
            self.players.append(player)
        self.__current_player_index = 0

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

    def get_results(self) -> list[Player]:
        results = sorted(self.players, key=lambda player: player.score, reverse=True)
        return results