#Module pour gérer les potions
def ajouter_potion(inventaire: list[str], potion: str) -> None:
    """
    Fonction pour ajouter une potion dans l'inventaire
    :param inventaire: Liste de potions
    :param potion: Nouvelle potion
    """
    inventaire.append(potion)
    print(f"La potion {potion} a été ajoutée dans l'inventaire.")

def copier_inventaire(inventaire: list[str]) -> list[str]:
    """
    Fonction pour copier dans l'inventaire
    :param inventaire: Liste de potions
    :return: Une copie de la liste de potions
    """
    copie = inventaire.copy()
    return copie

def additionner_potions(total: int, nb: int) -> int:
    """
    Fonction pour additionner les potions de l'inventaire
    :param total: Total précédent
    :param nb: nb à ajouter
    :return: nouveau total
    """
    total += nb
    return total