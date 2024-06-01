import inspect
import logging
from typing import Callable

from gamestate import GameState


log = logging.getLogger(__name__)


class Entry:
    def __init__(self, name: str, func: Callable[[GameState], bool]) -> None:
        self.name = name
        self.func = func

    def __validate__(self) -> bool:
        # Check if it's callable
        if not callable(self.func):
            raise TypeError("The submitted object is not a function.")

        # Get function signature
        sig = inspect.signature(self.func)

        # Check the number of parameters
        if len(sig.parameters) != 1:
            raise ValueError("Function must accept exactly one parameter.")

        # Check parameter type annotation
        params = list(sig.parameters.values())
        if params[0].annotation is not GameState:
            raise TypeError("Function parameter must be of type 'GameState'.")

        # Optionally check return type
        if sig.return_annotation is not bool:
            raise TypeError("Function must return a boolean.")

        return True

    def __str__(self) -> str:
        return ""

    def __repr__(self) -> str:
        return self.__str__()

    def is_valid(self) -> bool:
        return self.__validate__()
