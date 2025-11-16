class Objets:                       
    def __init__(self,nom):
        """classe de base des objets du jeu, classe parente de ces mêmes objets"""
        self.nom = nom

    def utiliser(self, joueur):
        print(f"le joueur utilise {self.nom}")
    
class Nourriture(Objets): 
    """hérite de Objet, gère la régénération de pas avec la nourriture"""          
    def __init__( self, nom):
        super().__init__(nom)
        self.nb_pas_nourriture={"pomme":2,
                           "banane":3,
                           "gateau":10,
                           "sandwich":15,
                           "repas":25
                           }
        self.nb_pas_recup= self.nb_pas_nourriture.get(nom)

    def utiliser(self, joueur):                   
        joueur.add_inv(Objets("Pas"), self.nb_pas_recup)
        print(f"le joueur mange {self.nom} et récupère {self.nb_pas_recup} pas.")
        
class cle(Objets):                                  
    """hérite de Objet, gère l'utilisation des clés"""
    def __init__( self, nom):
        super().__init__(nom)

    def utiliser(self , joueur):
        #partie.ouvrir_porte                remplacer par la fonction qui ouvre une porte
        print(f"le joueur utilise une {self.nom} pour ouvrir la porte")

class gemme(Objets):                                
    """hérite de Objet, gère l'utilisation des gemmes"""
    def __init__( self, nom):
        super().__init__(nom)

    def utiliser(self, joueur):
        #partie.choisir_piece()             remplacer par la fonction qui choisit une pièce
        print(f"le joueur utilise une {self.nom} pour choisir une pièce")

class des(Objets):
    """hérite de Objet, gère l'utilisation des dés"""
    def __init__( self, nom):
        super().__init__(nom)

    def utiliser(self, joueur):
        #partie.tirer_piece()             remplacer par la fonction qui tire une pièce
        print(f"le joueur utilise un {self.nom} et tire de nouvelles pièces")


class Gold(Objets):
    """Représente les pièces d'or de l'inventaire."""
    def __init__(self):
        super().__init__("Gold")


class Marteau(Objets):
    """Permet d'ouvrir certains coffres sans consommer de clé."""
    def __init__(self):
        super().__init__("Marteau")

    def utiliser(self, joueur):
        print("Le marteau permet de forcer des coffres.")


class MetalDetector(Objets):
    """Augmente les chances de trouver des clefs et pièces."""
    def __init__(self):
        super().__init__("Detecteur")

    def utiliser(self, joueur):
        print("Le détecteur augmente la chance de trouver du métal.")


class PatteLapin(Objets):
    """Augmente les chances de loot rares."""
    def __init__(self):
        super().__init__("Patte")

    def utiliser(self, joueur):
        print("La patte de lapin porte chance.")


class Pelle(Objets):
    """Objet permanent permettant de creuser."""
    def __init__(self):
        super().__init__("Pelle")

    def utiliser(self, joueur):
        print("La pelle permet de creuser dans certaines salles.")

class KitCrochetage(Objets):
    """Permet d'ouvrir portes sans consommer de clé."""
    def __init__(self):
        super().__init__("Kit de crochetage")

    def utiliser(self, joueur):
        print("")


def creer_objet_depuis_nom(nom):
    """Fabrique l'objet adéquat en fonction du nom utilisé dans l'inventaire."""
    mapping = {
        "Pas": Objets("Pas"),
        "Gemmes": gemme("Gemmes"),
        "Cle": cle("Cle"),
        "Gold": Gold(),
        "Des": des("Des"),
        "Pelle": Pelle(),
        "Marteau": Marteau(),
        "Detecteur": MetalDetector(),
        "Patte": PatteLapin(),
        "Kit de crochetage" : KitCrochetage()
    }
    return mapping.get(nom, Objets(nom))



class Joueur:
    """Cette classe représente l'inventaire du joueur et ses actions """
    def __init__(self):
        #self.nom= nom 
        self.__inventaire= {"Pas": {"objet": Objets("Pas"), "nombre": 70},  
            "Gemmes": {"objet": gemme("Gemmes"), "nombre": 2},
            "Cle": {"objet": cle("Cle"), "nombre": 0},
            "Gold": {"objet": Gold(), "nombre": 0},
            "Des": {"objet": des("Des"), "nombre": 0},
            "Pelle": {"objet": Pelle(), "nombre": 0},
            "Marteau": {"objet": Marteau(), "nombre": 0},
            "Detecteur": {"objet": MetalDetector(), "nombre": 0},
            "Patte": {"objet": PatteLapin(), "nombre": 0},
            "Kit de crochetage": {"objet": KitCrochetage(), "nombre": 0},
            }       # inventaire de départ 
                 
    @property   
    def inventaire(self):     
        """getter pour pouvoir consulter l'inventaire"""              
        return self.__inventaire


    def add_inv(self, obj, quantite):
        """ajoute une quantite d'un objet à l'inventaire (retire si négatif)"""
        
        if obj.nom not in self.__inventaire:
            self.__inventaire[obj.nom]= {"objet": obj , "nombre": 0}

        if quantite < 0 and self.__inventaire[obj.nom]["nombre"] + quantite < 0:
            print(f"pas assez de {obj.nom} dans l'inventaire")
        else:
            self.__inventaire[obj.nom]["nombre"]+= quantite  
            


    def ramasser_objet(self, obj): 
        """permet d'ajouter un objet à l'inventaire quand on le ramasse"""
        if isinstance(obj, Nourriture):
            obj.utiliser(self)

        elif obj.nom in self.__inventaire:
            self.__inventaire[obj.nom]["nombre"] += 1
            print(f"{obj.nom} ramassé")
            
        else:
            self.__inventaire[obj.nom] = {"objet": obj, "nombre": 1}
            print(f"{obj.nom} ramassé")



    def utiliser_objet(self, nom_objet):
        if nom_objet in self.__inventaire and self.__inventaire[nom_objet]["nombre"] >0 :

            objet = self.__inventaire[nom_objet]["objet"]
            objet.utiliser(self)
            
            self.__inventaire[nom_objet]["nombre"] -=1  
            if self.__inventaire[nom_objet]["nombre"]==0:
                del self.__inventaire[nom_objet]

            #print(f"le joueur utilise {nom_objet}.")
        else:
            print(f"pas de {nom_objet} dans l'inventaire.")

    def possede(self, nom_objet, quantite):
        """Vérifie si l'inventaire contient au moins une quantité donnée."""
        return self.__inventaire.get(nom_objet, {"nombre": 0})["nombre"] >= quantite

    def depenser(self, nom_objet, quantite):
        """Déduit une quantité sans déclencher l'effet `utiliser`."""
        if self.possede(nom_objet, quantite):
            self.__inventaire[nom_objet]["nombre"] -= quantite
            if self.__inventaire[nom_objet]["nombre"] == 0 and nom_objet not in ["Pas"]:
                del self.__inventaire[nom_objet]
            return True
        return False

    def get_quantite(self, nom_objet):
        """Retourne la quantité de la ressource demandée (0 par défaut)."""
        return self.__inventaire.get(nom_objet, {"nombre": 0})["nombre"]
