import random
from Inventaire import cle, gemme, Nourriture, Gold, creer_objet_depuis_nom, KitCrochetage, des

def _copie_obj(obj):
    """Crée une copie simple d'un objet pour les loots."""
    if isinstance(obj, Nourriture):
        return Nourriture(obj.nom)
    if obj.nom in ["Cle", "Gemmes", "Gold", "Des", "Pelle", "Marteau", "Detecteur", "Patte", "Kit de crochetage"]:
        return creer_objet_depuis_nom(obj.nom if obj.nom != "Gemmes" else "Gemmes")
    return obj


def genere_objet_aleatoire(chance_bonus=0.0, joueur=None):
    """Tire un objet pour les pièces avec tag 'aleatoire'."""
    table = [
        ([cle("Cle")], 0.25),
        ([gemme("Gemmes")], 0.2),
        ([Nourriture("pomme")], 0.15),
        ([Nourriture("banane")], 0.1),
        ([Nourriture("sandwich")], 0.08),
        ([Gold()], 0.15),
        ([], 0.07),
        ([KitCrochetage()], 0),
        ([des("des")], 0.5)
    ]
    return _tirer_lot(table, chance_bonus, joueur)


def tirer_loot(source, chance_bonus=0.0, joueur=None):
    """Retourne un lot d'objets ou ressources selon la source."""
    tables = {
        "coffre": [
            ([gemme("Gemmes"), gemme("Gemmes")], 0.25),
            ([cle("Cle")], 0.2),
            ([Nourriture("repas")], 0.1),
            ([Gold(), Gold(), Gold()], 0.25),
            ([creer_objet_depuis_nom("Marteau")], 0.05),
            ([], 0.15)
        ],
        "casier": [
            ([cle("Cle")], 0.35),
            ([Nourriture("sandwich")], 0.2),
            ([gemme("Gemmes")], 0.15),
            ([], 0.3)
        ],
        "trou": [
            ([Nourriture("pomme")], 0.3),
            ([Nourriture("gateau")], 0.1),
            ([Gold(), Gold()], 0.25),
            ([creer_objet_depuis_nom("Detecteur")], 0.05),
            ([], 0.3)
        ],
        "piece": [
            ([cle("Cle")], 0.2),
            ([gemme("Gemmes")], 0.2),
            ([Gold()], 0.2),
            ([Nourriture("banane")], 0.2),
            ([], 0.2)
        ]
    }
    table = tables.get(source, tables["piece"])
    return _tirer_lot(table, chance_bonus, joueur)


def _tirer_lot(table, chance_bonus, joueur):
    """Tire un lot en appliquant bonus et objets permanents."""
    bonus = chance_bonus
    if joueur:
        if joueur.possede("Patte", 1):
            bonus += 0.05
        if joueur.possede("Detecteur", 1):
            bonus += 0.05
    total = sum(p for _, p in table)
    rand = random.random() * (total + bonus)
    cumul = 0
    for lot, proba in table:
        cumul += proba
        if rand <= cumul:
            return [_copie_obj(obj) for obj in lot if obj]
    return []
