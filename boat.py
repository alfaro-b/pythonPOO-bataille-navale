class Boat:
    def __init__(self, name: str, positions: tuple[str, ...]) -> None:
        """
        Initialise un bateau.
        :param name: Nom du bateau
        :param positions: Coordonnées occupées par le bateau.
        """
        self.name: str = name
        self.positions: tuple[str, ...] = positions
        self.hits: list[str] = []

    def contains(self, shot: str) -> bool:
        """
        Vérifie si une coordonnée appartient au bateau.
        :param shot: Coordonnée du tir.
        :return: True si le bateau occupe la case, False sinon.
        """
        return shot in self.positions

    def hit(self, shot: str) -> None:
        """
        Enregistre un tir sur le bateau si la coordonnée lui appartient et n'a pas déjà été touchée.
        :param shot: Coordonnées du tir.
        """
        if self.contains(shot) and shot not in self.hits:
            self.hits.append(shot)

    def is_sunk(self) -> bool:
        """
        Indique si toutes les cases du bateau ont été touchées.
        :return: True si le bateau est coulé, False sinon.
        """
        return len(self.hits) == len(self.positions)
