from gamestate import GameState
from entry import Entry


class TestEntry(Entry):
    def __init__(self, name: str) -> None:
        super().__init__(name)

    def bank(self, state: GameState) -> bool:
        return False


def main(name: str) -> TestEntry:
    return TestEntry(name)
