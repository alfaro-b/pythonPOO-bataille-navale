class Grid:

    def __init__(self) -> None:
        """
        Initialise une grille de jeu vide de 10 lignes et 10 colonnes.
        """
        self.cells: list[list[str]] = []
        for _ in range(10):
            row: list[str] = []
            for _ in range(10):
                row.append(".")
            self.cells.append(row)
