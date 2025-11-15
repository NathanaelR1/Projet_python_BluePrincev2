import random
from Inventaire import Objets, Nourriture, Joueur

def genere_obj(joueur):
    """tire aléatoirement un objet"""
    obj_possibles = [
        Objets("cle"),
        Objets("gemme"),
        Nourriture("pomme"),
        Nourriture("banane"),
        Nourriture("gateau"),
        Nourriture("sandwich"),
        Nourriture("repas"),
        Objets("lockpick")
    ]

    probabilites = [
        0.3,   # Cle
        0.2,   # Gemmes
        0.25,  # pomme
        0.12,   # banane
        0.07,  # gateau
        0.05,  # sandwich
        0.01,  # repas
        0.002  #lockpick kit
    ]

    obj_genere= random.choices(obj_possibles, weights=probabilites, k=1)[0]
    if "lockpick" in joueur.inventaire and obj_genere.nom == "lockpick":
        obj_genere = Nourriture("repas")
    return obj_genere
    

def tirer_pieces(grille,ligne,colonne):
    """temporaire pour tester la génération de pièce"""
    pieces=["Pantry","SpareRoom"]
    i=random.randint(0,1)
    grille[ligne][colonne] = pieces[i]
    return grille
    