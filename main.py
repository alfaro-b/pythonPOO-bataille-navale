from boat import Boat
from grid import Grid

boats = [
    Boat("Aircraft carrier", ("B2", "C2", "D2", "E2", "F2")),
    Boat("Cruiser", ("A4", "A5", "A6", "A7")),
    Boat("Destroyer", ("C5", "C6", "C7")),
    Boat("Submarine", ("H5", "I5", "J5")),
    Boat("Torpedo boat", ("E9", "F9"))
]
for boat in boats:
    print(f"{boat.name} : {boat.positions}")

grid_game = Grid()
print(grid_game.grid)

