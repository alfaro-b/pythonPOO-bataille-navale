from boat import Boat


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

    def show_grid(self) -> None:
        """
        Affiche la grille de jeu avec en-têtes des colonnes et lignes.
        """
        print("   A B C D E F G H I J")
        for index, row in enumerate(self.cells):  # permet d'avoir le numéro de la ligne index+1 et ligne elle-même
            print(f"{index + 1:2} {' '.join(row)}")
            # dans les f string :2 permet de réserver deux caractères pour aligner

    def mark_sunk(self, boat: Boat) -> None:
        """
        Met à jour la grille lorsqu'un bateau est coulé, marque les cases du bateau coulé en C.
        :param boat: Le bateau qui vient d'être coulé.
        """
        for position in boat.positions:
            column = position[0]
            row = int(position[1:])
            column_index = ord(column) - ord('A')
            row_index = row - 1
            self.cells[row_index][column_index] = "C"
