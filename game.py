from boat import Boat
from grid import Grid


class Game:
    def __init__(self) -> None:
        """
        Initialise une partie de bataille navale.
        """
        self.boats: list[Boat] = [
            Boat("Aircraft carrier", ("B2", "C2", "D2", "E2", "F2")),
            Boat("Cruiser", ("A4", "A5", "A6", "A7")),
            Boat("Destroyer", ("C5", "C6", "C7")),
            Boat("Submarine", ("H5", "I5", "J5")),
            Boat("Torpedo boat", ("E9", "F9"))
        ]
        self.grid: Grid = Grid()
        self.misses: list[str] = []
