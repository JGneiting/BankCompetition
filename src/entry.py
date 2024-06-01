class Entry:
    def __init__(self, name: str) -> None:
        self.name = name
        self.should_bank
        pass

    def __validate__(self) -> bool:
        return True

    def __str__(self) -> str:
        return ""

    def __repr__(self) -> str:
        return self.__str__()

    def is_valid(self) -> bool:
        return self.__validate__()
