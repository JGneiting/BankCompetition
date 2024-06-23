from gamestate import GameState
from entry import Entry


class TestEntry(Entry):
    def __init__(self, name: str) -> None:
        super().__init__(name)

    def bank(self, state: GameState) -> bool:
        # print(state)
        user_input = input("Bank? 'y' or 'n': ")
        if user_input == "y":
            return True
        elif user_input == "n":
            return False
        return False


def main(name: str) -> TestEntry:
    return TestEntry(name)
