class Player:
    def __init__(self, name: str) -> None:
        self.name = name
        self.score = 0
        self.is_banked = False

    def __repr__(self) -> str:
        return self.__str__()

    def __str__(self) -> str:
        return f"{self.name}: {self.score} - {self.is_banked}"

    def __bool__(self) -> bool:
        return self.is_banked

    def bank(self, amount: int) -> None:
        self.is_banked = True
        self.score += amount

    def unbank(self) -> None:
        self.is_banked = False
