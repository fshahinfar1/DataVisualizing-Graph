#! python3
from enum import Enum, auto


class MouseState(Enum):
    clicked = auto()
    release = auto()
    drag = auto()
