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

    def update(self, shot: str, is_hit: bool) -> None:
        """
        Met à jour la grille après un tir.
        :param shot: Coordonnées du tir
        :param is_hit: True si le tir touche un bateau, False sinon.
        :return:
        """
        column = shot[0]
        row = int(shot[1:])
        column_index = ord(column) - ord('A')
        row_index = row - 1
        if is_hit:
            self.cells[row_index][column_index] = "O"
        else:
            self.cells[row_index][column_index] = "X"
