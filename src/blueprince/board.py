import random
import catalogue_des_pieces
from Inventaire import Gold, creer_objet_depuis_nom, Nourriture
from Aleatoire import tirer_loot, genere_objet_aleatoire
import copy

class Board:
    """" 
    Gere la grille du jeu soit tout ce qui est en lien avec le joueur son déplacement,
    l'ouverture d'une porte, le tirage des pièces, la séléctions des pièces, la rotation
    des pièces et le placement des pieces.
    
    
    """
    def __init__(self, joueur):

        self.joueur = joueur
        self.grille = [[None for _ in range(5)] for _ in range(9)]
        self.ligne_joueur = 8  
        self.colonne_joueur = 2  
        self.ligne_antechambert = 0
        self.colonne_antechambert = 2
        self.grille[self.ligne_joueur][self.colonne_joueur] = catalogue_des_pieces.EntranceHall
        self.grille[self.ligne_antechambert][self.colonne_antechambert] = catalogue_des_pieces.Antechamber
        self.direction = None 
        self.tirage_en_cours = []
        self.case_cible = None
        self.pioche_initial = copy.deepcopy(catalogue_des_pieces.pioche)
        self.mode = "exploration"
        self.direction_pour_placement = None
        self.direction_opposee = None
        self.message = ""
        self.magasin_ouvert = False
        self.selection_magasin = 0
        self.bonus_type_piece = {}
        self.bonus_objets = 0.0
        self.cout_pas_supplementaire = 0
        self.pieces_placees = {}
        self.enregistrer_piece(self.ligne_joueur, self.colonne_joueur)
        self.enregistrer_piece(self.ligne_antechambert, self.colonne_antechambert)
        self.chance_crochetage = 0.75
        
       
        

    def selectionner_direction(self, direction):
        """Met à jour la direction choisie par le joueur via ZQSD."""
        self.direction = direction
        
    
    def se_deplacer(self):
        """Déplace le joueur si la salle en face existe déjà.
        Gere les cas d'un mur, d'une porte fermer, d'une porte bloquer.
        Appelle la methode du tirage des pièces dans le cas ou on veut se déplacer dans
        une case vide.
        C'est la méthodes qui va appeller les autres indirectement pour l'avancer dans le jeu.
        Cette méthode est appeller dans le fichier game lors d'un évenement (appui sur espace).
        """
        piece_actuelle = self.grille[self.ligne_joueur][self.colonne_joueur]
        if self.direction is None:
            return
        
        ligne = self.ligne_joueur
        colonne = self.colonne_joueur
    
        direction_opposee = self.direction_opposee
    
        if self.direction == "haut":
            ligne -= 1
            direction_opposee = "bas"
            
        elif self.direction == "bas":
            ligne += 1
            direction_opposee = "haut"
            
        elif self.direction == "gauche":
            colonne -= 1
            direction_opposee = "droite"
            
        elif self.direction == "droite":
            colonne += 1
            direction_opposee = "gauche"
    
        # Vérification des bornes de la grille
        if not (0 <= ligne < 9 and 0 <= colonne < 5):
            print("Mur du manoir, impossible de bouger.")
            return
        
        if piece_actuelle.portes[self.direction] == False:
            self.message = "Pas de porte ici"
            return
       

        if self.grille[ligne][colonne] is not None:
            if self.grille[ligne][colonne].portes[direction_opposee] == False:
                self.message = "La porte est bloquée"
                return
            
            if not self.consommer_pas():
                return
            self.ligne_joueur = ligne
            self.colonne_joueur = colonne
            self.message = ""
            self.magasin_ouvert = False
            piece = self.grille[ligne][colonne]
            self.collecter_contenu_piece(piece)
            self.appliquer_effet_piece(piece, "enter")
            print(f"Le joueur s’est déplacé en ({ligne}, {colonne})")
            return
        
        niveau = piece_actuelle.niveaux_portes[self.direction]
        
        if niveau == 1:
            self.mode = "porte"
            self.message = "Porte verouillée. Appuyer sur Entrée pour utiliser une clé ou un kit"
            
        elif niveau == 2:
            self.mode = "porte"
            self.message = "Porte verouillée. Appuyer sur Entrée pour utiliser une clé"
        

        else:
            print("Aucune salle ici, ouverture d’une nouvelle porte.")
            self.direction_pour_placement = self.direction
            self.tirer_pieces_possibles()
            self.case_cible = (ligne, colonne)
            

        
    def tirer_pieces_possibles(self):
        """
        Effectue le tirage aléatoire des pieces selon leur rareté et gere la rotation lors
        du tirage.

        """
        poids_par_rarete = {
            catalogue_des_pieces.COMMONPLACE: 100,
            catalogue_des_pieces.STANDART: 100/3,
            catalogue_des_pieces.UNUSUAL: (100/3)/3,
            catalogue_des_pieces.RARE: ((100/3)/3)/3
            }
    
        
        poids = []  

        for piece in self.pioche_initial:  
            rarete = piece.rarete          
            if rarete in poids_par_rarete: 
                valeur = poids_par_rarete[rarete]  
            else:
                valeur = 0  
            bonus = self.bonus_type_piece.get(piece.type_de_piece, 0)
            valeur *= max(0.1, (1 + bonus))
            poids.append(valeur)  
    
        
        pieces_tirees = []
        selection_valide = False
        while not selection_valide:
            pieces_tirees = []
            while len(pieces_tirees) < 3:
                tirage = random.choices(self.pioche_initial, weights=poids, k=1)[0]
                if tirage not in pieces_tirees:
                    pieces_tirees.append(tirage)
                    
            if any(piece.cout_gemmes == 0 for piece in pieces_tirees):
                selection_valide = True
    
                
        for piece in pieces_tirees:
            self.orienter_piece_selon_direction(piece)
            self.appliquer_effet_piece(piece, "draw")
                
    
        # Sauvegarde le tirage actuel           
        self.tirage_en_cours = pieces_tirees
        self.selection_tirage = 0  # index du choix par défaut
        self.mode = "choix_piece"
    
        return pieces_tirees

        

    def changer_selection_tirage(self, direction):
        """Permet de changer le choix dans les 3 propositions avec les flèches directionelles."""
        if not self.tirage_en_cours:
            return
        if direction == "gauche":
            self.selection_tirage = (self.selection_tirage - 1) % len(self.tirage_en_cours)
        elif direction == "droite":
            self.selection_tirage = (self.selection_tirage + 1) % len(self.tirage_en_cours)

    def appliquer_effet_piece(self, piece, evenement):
        if piece is None or not piece.effet:
            return
        effets = piece.effet if isinstance(piece.effet, list) else [piece.effet]
        for effet in effets:
            effet = self._normaliser_effet(effet)
            if not effet:
                continue
            type_effet = effet.get("type")
            if type_effet == "enter_resource" and evenement == "enter":
                quantite = effet.get("quantite", 0)
                ressource = effet.get("ressource")
                if quantite >= 0:
                    self.joueur.add_inv(creer_objet_depuis_nom(ressource), quantite)
                else:
                    if not self.joueur.depenser(ressource, abs(quantite)):
                        self.message = "Ressource insuffisante."
                self.message = effet.get("message", self.message)
            elif type_effet == "draw_resource" and evenement == "draw":
                quantite = effet.get("quantite", 0)
                ressource = effet.get("ressource")
                if quantite >= 0:
                    self.joueur.add_inv(creer_objet_depuis_nom(ressource), quantite)
                else:
                    self.joueur.depenser(ressource, abs(quantite))
            elif type_effet == "disperse" and evenement == "enter":
                self.disperser_ressource(effet.get("ressource"), effet.get("quantite", 1))
            elif type_effet == "room_probability":
                if evenement == effet.get("evenement", "enter"):
                    cible = effet.get("cible")
                    delta = effet.get("delta", 0)
                    self.bonus_type_piece[cible] = self.bonus_type_piece.get(cible, 0) + delta
            elif type_effet == "object_probability" and evenement == "enter":
                self.bonus_objets += effet.get("bonus", 0)
            elif type_effet == "ajout_pioche" and evenement == "enter":
                self.ajouter_pieces_pioche(effet.get("pieces", []))
            elif type_effet == "double_cost" and evenement == "enter":
                self.cout_pas_supplementaire = effet.get("cout", 1)
            elif type_effet == "custom_message" and evenement == "enter":
                self.message = effet.get("message", self.message)
            elif type_effet == "set_resource_min" and evenement == "enter":
                valeur = effet.get("valeur", 0)
                ressource = effet.get("ressource")
                actuel = self.joueur.get_quantite(ressource)
                if actuel < valeur:
                    self.joueur.add_inv(creer_objet_depuis_nom(ressource), valeur - actuel)

    def piece_actuelle(self):
        """Retourne la pièce où se trouve le joueur."""
        return self.grille[self.ligne_joueur][self.colonne_joueur]

    def enregistrer_piece(self, ligne, colonne):
        piece = self.grille[ligne][colonne]
        if piece is not None:
            self.pieces_placees[(ligne, colonne)] = piece

    def disperser_ressource(self, ressource, quantite):
        cibles = list(self.pieces_placees.values())
        if not cibles:
            return
        for _ in range(min(quantite, len(cibles))):
            piece = random.choice(cibles)
            piece.objets.append(ressource.lower())

    def ajouter_pieces_pioche(self, noms_pieces):
        for nom in noms_pieces:
            piece_modele = catalogue_des_pieces.obtenir_piece_par_nom(nom)
            if piece_modele:
                self.pioche_initial.append(copy.deepcopy(piece_modele))

    def consommer_pas(self):
        """Retire un pas de l'inventaire, retourne False si impossible."""
        cout = 1 + self.cout_pas_supplementaire
        if self.joueur.depenser("Pas", cout):
            self.cout_pas_supplementaire = 0
            return True
        self.message = "Plus de pas."
        return False

    def collecter_contenu_piece(self, piece):
        """Affiche le loot de la pièce sans rien ramasser automatiquement."""
        if piece is None:
            return
    
        # Réinitialise la liste
        self.objets_disponibles = []
    
        # Tous les objets sont listés
        if piece.objets and not piece.objets_ramasses:
            for tag in piece.objets:
                if tag == "aleatoire":
                    loot = genere_objet_aleatoire(self.bonus_objets, self.joueur)
                    self.objets_disponibles.extend(loot)
                else:
                    obj = self._creer_objet_depuis_tag(tag)
                    if obj:
                        self.objets_disponibles.append(obj)
    
        # Si la pièce contient quelque chose → mode sélection
        if self.objets_disponibles:
            self.selection_objet = 0
            self.mode = "choix_objet"
            self.message = "Choisis un objet"
            return
        
        # Si rien → retour normal
        piece.objets_ramasses = True
        
    def choisir_objet(self, direction):
        """Navigation dans la liste des objets au sol."""
        if not self.objets_disponibles:
            return
    
        if direction == "haut":
            self.selection_objet = (self.selection_objet - 1) % len(self.objets_disponibles)
        elif direction == "bas":
            self.selection_objet = (self.selection_objet + 1) % len(self.objets_disponibles)
    
    
    def ramasser_objet_selectionne(self):
        """Ramasse l'objet sélectionné et repasse en exploration si plus rien."""
        if self.mode != "choix_objet":
            return
    
        if not self.objets_disponibles:
            self.mode = "exploration"
            self.message = ""
            return
    
        obj = self.objets_disponibles[self.selection_objet]
    
        # Ramassage via Joueur
        self.joueur.ramasser_objet(obj)
        self.message = f"Vous avez ramasser {obj.nom}."
    
        # Retire de la liste des objets affichés
        self.objets_disponibles.pop(self.selection_objet)
    
        # Ajuste l'index pour ne pas sortir de la liste
        if self.selection_objet >= len(self.objets_disponibles):
            self.selection_objet = max(0, len(self.objets_disponibles) - 1)
    
        # Si il n’y a plus rien → mode normal
        if not self.objets_disponibles:
            piece = self.piece_actuelle()
            if piece:
                piece.objets_ramasses = True
            self.mode = "exploration"



    def _creer_objet_depuis_tag(self, tag):
        """Convertit un tag d'objet de pièce en véritable objet."""
        tag = tag.lower()
        if tag == "cle":
            return creer_objet_depuis_nom("Cle")
        if tag == "gemme":
            return creer_objet_depuis_nom("Gemmes")
        if tag == "or":
            return Gold()
        if tag == "fruit":
            return Nourriture("banane")
        if tag == "pelle":
            return creer_objet_depuis_nom("Pelle")
        if tag == "des":
            return creer_objet_depuis_nom("Des")
        if tag == "kit de crochetage":
            return creer_objet_depuis_nom("Kit de crochetage")
        if tag == "detecteur":
            return creer_objet_depuis_nom("Detecteur")
        # tags 'aleatoire' ou inconnus ne sont pas traités ici
        return None

    def ouvrir_magasin(self, automatique=False):
        piece = self.piece_actuelle()
        if piece is None or not piece.commerce:
            self.message = "Pas de magasin ici."
            self.magasin_ouvert = False
            return
    
        self.magasin_ouvert = True
        self.selection_magasin = 0
        
        # On garde une liste des offres visibles
        self.options_magasin_visibles = piece.commerce.copy()
    
        self.message = f"Magasin : {piece.nom}"

    def fermer_magasin(self):
        """Ferme l'interface magasin."""
        self.magasin_ouvert = False

    def changer_selection_magasin(self, direction):
        if not self.magasin_ouvert or not self.options_magasin_visibles:
            return
        if direction == "haut":
            self.selection_magasin = (self.selection_magasin - 1) % len(self.options_magasin_visibles)
        elif direction == "bas":
            self.selection_magasin = (self.selection_magasin + 1) % len(self.options_magasin_visibles)

    def acheter_selection_magasin(self):
        if not self.magasin_ouvert:
            return
    
        offre = self.options_magasin_visibles[self.selection_magasin]
        cout = offre.get("cout", 0)
    
        # Vérification de l'or
        if cout > 0 and not self.joueur.possede("Gold", cout):
            self.message = f"Il manque {cout} gold."
            return
    
        if cout > 0:
            self.joueur.depenser("Gold", cout)
    
        gain = offre.get("gain", {})
        if "ressource" in gain:
            obj = creer_objet_depuis_nom(gain["ressource"])
            quantite = gain.get("quantite", 1)
            self.joueur.add_inv(obj, quantite)
            self.message = f"Achat : +{quantite} {obj.nom}"
        else:
            self.message = "Aucun gain défini dans le magasin."
            
            
            
    def interagir(self):
        piece = self.piece_actuelle()
        if piece is None or not piece.interactions:
            self.message = "Rien à faire ici."
            return
        interaction = piece.interactions.pop(0)
        type_inter = interaction.get("type")
        if type_inter == "trou":
            if not self.joueur.possede("Pelle", 1):
                self.message = "Il faut une pelle."
                piece.interactions.insert(0, interaction)
                return
            butin = tirer_loot("trou", self.bonus_objets, self.joueur)
            self._appliquer_butin(butin)
        elif type_inter == "coffre":
            niveau = interaction.get("niveau", 1)
            cle_requise = 1 if niveau == 1 else 2
            if not self.joueur.possede("Marteau", 1):
                if not self.joueur.possede("Cle", cle_requise):
                    self.message = "Il manque des clefs."
                    piece.interactions.insert(0, interaction)
                    return
                for _ in range(cle_requise):
                    self.joueur.depenser("Cle", 1)
            butin = tirer_loot("coffre", self.bonus_objets, self.joueur)
            self._appliquer_butin(butin)
        elif type_inter == "casier":
            if not self.joueur.depenser("Cle", 1):
                self.message = "Besoin d'une clef."
                piece.interactions.insert(0, interaction)
                return
            butin = tirer_loot("casier", self.bonus_objets, self.joueur)
            self._appliquer_butin(butin)
        else:
            self.message = "Interaction inconnue."

    def _appliquer_butin(self, objets):
        if not objets:
            self.message = "Rien trouvé."
            return
        noms = []
        for obj in objets:
            self.joueur.ramasser_objet(obj)
            noms.append(obj.nom)
        self.message = f"Butin: {', '.join(noms)}"

    def placer_piece_choisie(self):
        """Place la pièce choisie sur la case cible et ré-initialise le tirage au moment
        du placement.
        Appeller dans game au moment de l'appui sur entrée.
         
        """

        # Récupération de la pièce choisie
        piece_choisie = self.tirage_en_cours[self.selection_tirage]
        ligne, colonne = self.case_cible
        
        if piece_choisie.cout_gemmes == 0:
            pass
        
        elif piece_choisie.cout_gemmes == 1:
            if not self.joueur.possede("Gemmes", 1):
                self.message = "Il manque 1 gemmes pour placer cette pièce."
                return
            self.joueur.depenser("Gemmes", 1)
            
        elif piece_choisie.cout_gemmes == 2:
            if not self.joueur.possede("Gemmes", 2):
                self.message = "Il manque 2 gemmes pour placer cette pièce."
                return
            self.joueur.depenser("Gemmes", 2)
            
        elif piece_choisie.cout_gemmes == 3:
            if not self.joueur.possede("Gemmes",3):
                self.message = "Il manque 2 gemmes pour placer cette pièce."
                return
            self.joueur.depenser("Gemmes", 3)
        
        
        #on eleve d'abord de la pioche la piece
        if piece_choisie in self.pioche_initial:
            self.pioche_initial.remove(piece_choisie)
        #puis on cree une copie qu'on va placer
        piece_choisie_a_placer = copy.deepcopy(piece_choisie)
        
            
        # Placement dans la grille
        self.grille[ligne][colonne] = piece_choisie_a_placer
        piece_choisie_a_placer.tirer_niveaux_portes(ligne)
        self.enregistrer_piece(ligne, colonne)
    
        # ré-initialistion du tirage de toute les pieces, utile plus tard quand la pioche
        #aura plusieur meme piece de base
        for piece in self.tirage_en_cours:
            piece.reinitialiser_rotation()
            
        self.tirage_en_cours = []
        self.selection_tirage = 0
        self.case_cible = None
        self.direction_pour_placement = None
        print(f" Pièce '{piece_choisie.nom}' placée en ({ligne}, {colonne})")
    
        # Retour au mode exploration
        self.mode = "exploration"
        self.magasin_ouvert = False

    def annuler_tirage(self):
        """Permet de revenir en mode exploration sans placer de pièce."""
        for piece in self.tirage_en_cours:
            piece.reinitialiser_rotation()
        self.tirage_en_cours = []
        self.selection_tirage = 0
        self.case_cible = None
        self.direction_pour_placement = None
        self.mode = "exploration"
        self.message = "Choix de pièce annulé."
        
    def _normaliser_effet(self, effet):
        if effet is None:
            return None
        if isinstance(effet, dict):
            return effet
        if isinstance(effet, str):
            if effet == "pas":
                return {"type": "enter_resource", "ressource": "Pas", "quantite": 3}
            if "gemmes" in effet:
                return {"type": "set_resource_min", "ressource": "Gemmes", "valeur": 2,
                        "message": "Les gemmes sont réinitialisées à 2"}
        return None

    def orienter_piece_selon_direction(self, piece):
        """
        Oriente les pièces de sorte a pouvoir continuer a progresser dans le manoir.
        Tout les cas possibles.
        Appeler dans le placement des pièces.
        Appelle la méthode de la class Pièce pour éffectuer la rotation.
        
        """
        
        portes = piece.portes
        #print(f"{piece.nom} | Portes : {piece.portes} | Direction placement : {self.direction_pour_placement}")
        if portes["bas"] and not (portes["haut"] or portes["gauche"] or portes["droite"] ):
            
            if self.direction_pour_placement == "haut":
                pass
                
            elif self.direction_pour_placement == "droite":
                piece.tourner_la_piece("horaire")
                
            elif self.direction_pour_placement == "gauche":
                piece.tourner_la_piece("antihoraire")
                
            elif self.direction_pour_placement == "bas":
                piece.tourner_la_piece("horaire")
                piece.tourner_la_piece("horaire")
                
        if portes["bas"] and portes["gauche"] and not (portes["haut"]  or portes["droite"] ):
            
            if self.direction_pour_placement == "haut":
                pass
                
            elif self.direction_pour_placement == "droite":
                piece.tourner_la_piece("horaire")
                
            elif self.direction_pour_placement == "gauche":
                piece.tourner_la_piece("horaire")
                piece.tourner_la_piece("horaire")
                
            elif self.direction_pour_placement == "bas":
                if self.grille[self.ligne_joueur-1][self.colonne_joueur -1] == None:
                    piece.tourner_la_piece("horaire")
                else: 
                    piece.tourner_la_piece("horaire")
            
        if portes["bas"] and portes["haut"] and not (portes["gauche"]  or portes["droite"] ):
            
            if self.direction_pour_placement == "haut":
                pass
                
            elif self.direction_pour_placement == "droite":
                piece.tourner_la_piece("horaire")
                
            elif self.direction_pour_placement == "gauche":
                piece.tourner_la_piece("antihoraire")
                
            elif self.direction_pour_placement == "bas":
                piece.tourner_la_piece("horaire")
                piece.tourner_la_piece("horaire")
        
        if portes["bas"] and portes["droite"] and portes["gauche"] and not (portes["haut"] ):
    
            if self.direction_pour_placement == "haut":
                pass
                
            elif self.direction_pour_placement == "droite":
                piece.tourner_la_piece("horaire")
                
            elif self.direction_pour_placement == "gauche":
                piece.tourner_la_piece("antihoraire")
                
            elif self.direction_pour_placement == "bas":
                piece.tourner_la_piece("horaire")
                #piece.tourner_la_piece("horaire")
            
                    
    def confirmer_ouverture_porte(self, accepter):
        if self.mode != "porte":
            return
        
        # Refus joueur
        if not accepter:
            self.message = "Porte laissée fermée."
            self.mode = "exploration"
            return
        
    
        piece = self.piece_actuelle()
        niveau = piece.niveaux_portes[self.direction]
    
    
        # Tentative de crochetage possible (uniquement N1)
        if niveau == 1 and self.joueur.possede("Kit de crochetage", 1):
            if random.random() <= self.chance_crochetage:
                piece.niveaux_portes[self.direction] = 0
                self.message = "Tu crochettes la porte avec succès !"
            else:
                self.message = "Échec du crochetage..."
            self.mode = "exploration"
            return
        
        
        elif niveau == 1 and  not self.joueur.possede("Kit de crochetage", 1):
    
            self.joueur.depenser("Cle", 1)
            piece.niveaux_portes[self.direction] = 0
        
            self.message = "Porte ouverte !"
            self.mode = "exploration"
            return
        elif niveau == 2 and self.joueur.possede("Kit de crochetage", 1) and not self.joueur.possede("Cle", 1):
        
            self.message = "Le kit de crochetage ne marche pas pour un porte verouillée à double tour"
            self.mode = "exploration"
            return
        

        elif not self.joueur.possede("Cle", 1):
            self.message = "Pas assez de clés."
            self.mode = "exploration"
            return
        
        else:
            self.joueur.depenser("Cle", 1)
            piece.niveaux_portes[self.direction] = 0
        
            self.message = "Porte ouverte !"
            self.mode = "exploration"
            return


    def relancer_tirage(self):
        """Ré-effectue un tirage si le joueur a au moins 1 dé."""
        
        # Vérifier si on est bien dans le mode tirage
        if self.mode != "choix_piece":
            self.message = "Tu ne peux pas relancer maintenant."
            return
    
        # Vérifier si le joueur a des dés
        if not self.joueur.possede("Des", 1):
            self.message = "Aucun dé disponible."
            return
        
        # Consommer un dé
        self.joueur.depenser("Des", 1)
        
        # Refaire un tirage de 3 nouvelles pièces
        self.tirer_pieces_possibles()
        self.message = "Relance du tirage "
        

        

    
