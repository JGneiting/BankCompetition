from gamestate import GameState
from entry import Entry

# TODO - edit this to be a full fledged scrooge agent.
class TestEntry(Entry):
    def __init__(self, name: str) -> None:
        super().__init__(name)

    def bank(self, state: GameState) -> bool:
        return True


def main(name: str) -> TestEntry:
    return TestEntry(name)
