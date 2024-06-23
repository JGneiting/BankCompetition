import inspect
import logging
from abc import ABC, abstractmethod
from bankcompetition.src.bankcompetition.gamestate import GameState


log = logging.getLogger(__name__)


class Entry(ABC):
    def __init__(self, name: str) -> None:
        self.name = name
        if not self.is_valid():
            raise ValueError(f"The function for {self.name} is not valid")

    @abstractmethod
    def bank(self, gamestate: GameState) -> bool:
        pass

    def __validate__(self) -> bool:
        # Get the function signature of the overridden func method
        func_impl = self.__class__.__dict__.get('bank')
        if func_impl is None:
            raise TypeError("Derived class must implement the 'bank' method.")

        sig = inspect.signature(func_impl)

        if len(sig.parameters) != 2:  # self and gamestate
            raise ValueError("Function must accept exactly one parameter besides 'self'.")

        params = list(sig.parameters.values())
        if type(params[1].annotation) is not type(GameState):
            raise TypeError("Function parameter must be of type 'GameState'.")

        if sig.return_annotation is not bool:
            raise TypeError("Function must return a boolean.")

        return True

    def __str__(self) -> str:
        return ""

    def __repr__(self) -> str:
        return self.__str__()

    def is_valid(self) -> bool:
        return self.__validate__()
