class Boat:
    def __init__(self, name: str, positions: tuple[str, ...]) -> None:
        """
        Initialise un bateau.
        :param name: Nom du bateau
        :param positions: Coordonnées occupées par le bateau.
        """
        self.name: str = name
        self.positions: tuple[str, ...] = positions

    def is_sunk(self, hit_shots) -> bool:
        """
        Indique si le bateau est coulé,
        c'est-à-dire lorsque toutes les cases qu'il occupe sont touchées.
        :param hit_shots: Liste des coordonnées touchées.
        :return: True si le bateau est coulé, False sinon.
        """
        if all(position in hit_shots for position in self.positions):
            return True
        return False
