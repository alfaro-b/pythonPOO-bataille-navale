class Grid:
    """
    Initialise une grille de jeu vide de 10 lignes et 10 colonnes.
    """
    def __init__(self) -> None:
        self.grid: list[list[str]] = []
        for _ in range(10):
            row = []
            for _ in range(10):
                row.append(".")
            self.grid.append(row)
