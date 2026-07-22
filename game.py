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
        self.shots: list[str] = []

    def ask_shot(self) -> str:
        """
        Demande au joueur de saisir les coordonnées d'un tir.
        :return: Les coordonnées valides saisies par le joueur.
        """
        while True:
            coordinate_shot: str = input("Quelle case jouez-vous? Réponse format A1, par ex. ").upper()

            # Vérifie validité
            if len(coordinate_shot) < 2 or len(coordinate_shot) > 3:
                print("Saisie invalide.")
                continue

            # Vérifie la colonne
            if coordinate_shot[0] not in "ABCDEFGHIJ":
                print("La colonne doit être comprise entre A et J.")
                continue

            # Vérifier la ligne
            if not coordinate_shot[1:].isdigit():
                print("Le numéro de ligne est invalide.")
                continue

            row = int(coordinate_shot[1:])
            if row < 1 or row > 10:
                print("La ligne doit être comprise entre 1 et 10.")
                continue

            # Vérifie si la case a déjà été jouée
            if coordinate_shot in self.shots:
                print("Cette case a déjà été jouée.")
                continue

            return coordinate_shot

    def check_shot(self, coordinate_shot: str) -> Boat | None:
        """
        Vérifie si un tir touche un bateau.
        :param coordinate_shot: Coordonnée du tir
        :return: Le bateau touché ou None si le tir est manqué.
        """
        for boat in self.boats:
            if boat.contains(coordinate_shot):
                boat.hit(coordinate_shot)
                print("Touché! ")
                return boat
        print("Manqué! ")
        self.misses.append(coordinate_shot)
        return None
