import pygame
from board import Board
from assets import Assets
from Inventaire import Joueur


class Game:
    """"
    Cette class gère l'affichage et les évenements du jeu.
    On a deux mode : exploration et choix de pièces.
    C'est ici qu'on appelle les méthodes de board lier au évenement soit lorsqu'on appui
    sur uune touche.
    
    """
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((1920, 1080), pygame.FULLSCREEN)
        pygame.display.set_caption("Blue Prince Prototype")
        self.clock = pygame.time.Clock()
        self.joueur=Joueur()
        self.board = Board(self.joueur)
        self.assets = Assets()
        self.direction_ui = None

        self.tirage_en_cours = []
        self.selection_tirage = 0
        
 


    def Partie_Salle(self):
        """
        Cette méthode crée la grille visuelle, affiche les pièces et la directions
        lors des appuis sur les touches.
        """
        depart_x =  0
        depart_y = 0
        taille_case = 80
        
        lignes = 9
        colonnes = 5
        
        for l in range(lignes):
            for c in range(colonnes):
                    x = depart_x + c*taille_case
                    y = depart_y + l*taille_case
                    pygame.draw.rect(self.screen, (0,0,0),(x,y,taille_case,taille_case),1)
                    
                    
                    room = self.board.grille[l][c]
                    if room is not None:
                        img = self.assets.charger_image_piece(room,1)
                        if img:
                            self.screen.blit(img, (x, y))

                
        x_joueur = self.board.colonne_joueur * taille_case
        y_joueur = self.board.ligne_joueur * taille_case
        pygame.draw.rect(self.screen, (255, 255, 255), (x_joueur , y_joueur , taille_case, taille_case), 2)
        

        if self.direction_ui is not None:
            marge = 2  
            epaisseur = 3
        
            if self.direction_ui == "haut":
                pygame.draw.line(self.screen, (255,255,255),
                                 (x_joueur + marge, y_joueur + marge),
                                 (x_joueur + taille_case - marge, y_joueur + marge),
                                 epaisseur)
            elif self.direction_ui == "bas":
                pygame.draw.line(self.screen, (255,255,255),
                                 (x_joueur + marge, y_joueur + taille_case - marge - 1),
                                 (x_joueur + taille_case - marge, y_joueur + taille_case - marge - 1),
                                 epaisseur)
            elif self.direction_ui == "gauche":
                pygame.draw.line(self.screen, (255,255,255),
                                 (x_joueur + marge, y_joueur + marge),
                                 (x_joueur + marge, y_joueur + taille_case - marge),
                                 epaisseur)
            elif self.direction_ui == "droite":
                pygame.draw.line(self.screen, (255,255,255),
                                 (x_joueur + taille_case - marge - 1, y_joueur + marge),
                                 (x_joueur + taille_case - marge - 1, y_joueur + taille_case - marge),
                                 epaisseur)
            


    
    def Partie_Inventaire(self):
        """
        Cette méthode affiche la partie inventaire, le tirage des pièces et la sélection visible
        des pièces lors du tirage.
        
        
        """
        depart_x = 400
        depart_y = 0
        
        largeur = 1520
        hauteur = 1080
        
        pygame.draw.rect(self.screen, (255,255,255),(depart_x,depart_y,largeur,hauteur))
    
        piece_actuelle = self.board.piece_actuelle() if hasattr(self.board, "piece_actuelle") else None
        if self.board.mode == "exploration" and piece_actuelle:
            nom_piece_actuelle = pygame.font.Font(None, 30)
            nom_piece_actuelle = nom_piece_actuelle.render(piece_actuelle.nom, True, (0, 0, 0))
            self.screen.blit(nom_piece_actuelle, (450, 375))
        
        texte_inventaire = pygame.font.Font(None, 30)
        texte_inventaire = texte_inventaire.render("Inventaire :", True, (0, 0, 0))
        self.screen.blit(texte_inventaire, (450, 50))
        
        ressources = [
            ("../../assets/Inventaire/Steps1.png", "Pas", 80),
            ("../../assets/Inventaire/Gold.png", "Gold", 120),
            ("../../assets/Inventaire/Gem.png", "Gemmes", 160),
            ("../../assets/Inventaire/Key.png", "Cle", 200),
            ("../../assets/Inventaire/Ivory_dice.png", "Des", 240),
        ]
        font_valeur = pygame.font.Font(None, 28)
        for chemin, nom, pos_y in ressources:
            img = pygame.image.load(chemin).convert_alpha()
            img = pygame.transform.scale(img, (25, 25))
            self.screen.blit(img, (1240, pos_y))
            quantite = self.joueur.get_quantite(nom)
            texte_qte = font_valeur.render(str(quantite), True, (0, 0, 0))
            self.screen.blit(texte_qte, (1200, pos_y))
            
        objets_speciaux = ["Pelle", "Marteau", "Detecteur de métal", "Patte", "Kit de crochetage"]

        font_item = pygame.font.Font(None, 26)
        
        y_item = 80
        for nom in objets_speciaux:
            if self.joueur.get_quantite(nom) > 0:  # Le joueur possède cet objet
                texte_item = font_item.render(f"{nom}", True, (0, 0, 0))
                self.screen.blit(texte_item, (450, y_item))
                y_item += 35
 
        if self.board.message:
            font_message = pygame.font.Font(None, 30)  
            texte_message = font_message.render(self.board.message, True, (0, 0, 0))  
            self.screen.blit(texte_message, (450, 680))
        elif piece_actuelle and piece_actuelle.commerce:
            font_message = pygame.font.Font(None, 28)
            texte_message = font_message.render("Appuie sur M pour ouvrir ou fermer le magasin.", True, (0, 0, 0))
            self.screen.blit(texte_message, (450, 680))
                
        
        #tirage du bas affichage
        if self.board.tirage_en_cours:
            font_choix = pygame.font.Font(None, 30)  
            texte_choix = font_choix.render("Choisie une pièce à placer", True, (0, 0, 0))  
            self.screen.blit(texte_choix, (450, 375))
            
            lignes = [
                      "ENTER = Placer",
                      #"ESC = Annuler",
                      "R = Relancer" 
                      ]
            for i, ligne in enumerate(lignes):
                texte = font_choix.render(ligne, True, (0, 0, 0))
                self.screen.blit(texte, (1100, 375 + i * 30))
                
            
            y_img = 425
            for i, room in enumerate(self.board.tirage_en_cours):
                img = self.assets.charger_image_piece(room,2)
                if img:
                    #img_redim = pygame.transform.scale(img, (128, 128))
                    x_img = 500 + i * 170
                    #self.screen.blit(img_redim, (x_img, y_img))
                    self.screen.blit(img, (x_img, y_img))
        
                    # cadre autour de la pièce sélectionnée
                    if i == self.board.selection_tirage:
                        pygame.draw.rect(self.screen, (255, 255, 0), (x_img - 5, y_img - 5, 138, 138), 4)
        
                    # nom de la pièce en dessous
                    font = pygame.font.Font(None, 24)
                    text = font.render(room.nom, True, (0, 0, 0))
                    self.screen.blit(text, (x_img, y_img + 135))
                    
                    cout = room.cout_gemmes
                    if cout > 0:
                        img_gemme = pygame.image.load("../../assets/Inventaire/Gem.png").convert_alpha()
                        img_gemme = pygame.transform.scale(img_gemme, (25, 25))
                    
                        for j in range(cout):
                            self.screen.blit(img_gemme, (x_img  + j * 32, y_img + 160))
                    

        if self.board.magasin_ouvert:
            font_shop = pygame.font.Font(None, 26)
            piece = self.board.piece_actuelle()
            if piece and piece.commerce:
                instructions = font_shop.render("Magasin ouvert (←/→ pour naviguer, Entrée pour acheter, ESC pour quitter)", True, (0, 0, 0))
                self.screen.blit(instructions, (450, 720))
                y_magasin = 760
                for i, offre in enumerate(piece.commerce):
                    x = 450 + i * 220
                    rect = pygame.Rect(x, y_magasin, 200, 90)
                    couleur = (200, 200, 200) if i == self.board.selection_magasin else (220, 220, 220)
                    pygame.draw.rect(self.screen, couleur, rect)
                    pygame.draw.rect(self.screen, (0, 0, 0), rect, 2)
                    texte_nom = font_shop.render(offre["nom"], True, (0, 0, 0))
                    self.screen.blit(texte_nom, (x + 10, y_magasin + 10))
                    texte_cout = font_shop.render(f"Cout: {offre['cout']} or", True, (0, 0, 0))
                    self.screen.blit(texte_cout, (x + 10, y_magasin + 40))
            else:
                info = font_shop.render("Ce magasin n'a plus d'offres.", True, (0, 0, 0))
                self.screen.blit(info, (450, 760))
        elif piece_actuelle and piece_actuelle.interactions:
            font_inter = pygame.font.Font(None, 26)
            texte_inter = font_inter.render("Appuie sur E pour interagir avec la pièce.", True, (0, 0, 0))
            self.screen.blit(texte_inter, (450, 720))

         # Affichage des objets au sol si en mode choix_objet
        if self.board.mode == "choix_objet" and piece_actuelle:
            

            nom_piece_actuelle = pygame.font.Font(None, 30)
            nom_piece_actuelle = nom_piece_actuelle.render(piece_actuelle.nom, True, (0, 0, 0))
            self.screen.blit(nom_piece_actuelle, (450, 375))
             
            font = pygame.font.Font(None, 28)
            y = 400
            for i, obj in enumerate(self.board.objets_disponibles):
                couleur = (255, 0, 0) if i == self.board.selection_objet else (0, 0, 0)
                
                texte = font.render( f"Prendre {obj.nom}", True, couleur)
                self.screen.blit(texte, (450, y))
                y += 20
                
        if self.board.magasin_ouvert:
            piece = self.board.piece_actuelle()
            offres = self.board.options_magasin_visibles
            font = pygame.font.Font(None, 28)
        
            y = 420
            for i, offre in enumerate(offres):
                prix = offre.get("cout", 0)
                nom = offre.get("nom", "???")
                texte = f"{nom} - {prix} Gold"
        
                if i == self.board.selection_magasin:
                    texte = "> " + texte
        
                render = font.render(texte, True, (0,0,0))
                self.screen.blit(render, (475, y))
                y += 30
    

    def run(self):
        """"
        Cette méthode gere le lancement de la fenetre de eu et des évenements.
        C'est ici que l'on regarde dans quelle mode on est. 
        """
        running = True
        fin_de_partie = False
        
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    
                
  
                if self.board.magasin_ouvert:
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_UP:
                            self.board.changer_selection_magasin("haut")
                        elif event.key == pygame.K_DOWN:
                            self.board.changer_selection_magasin("bas")
                        elif event.key == pygame.K_RETURN:
                            self.board.acheter_selection_magasin()
                        elif event.key == pygame.K_m:
                            self.board.fermer_magasin()
                    continue
                
                if self.board.mode == "exploration":
                    if event.type == pygame.KEYDOWN:
                        if fin_de_partie:
                            if event.key == pygame.K_ESCAPE:
                                running = False  # permettre de quitter
                            continue  # bloquer tout le gameplay
                            

                        if event.key == pygame.K_z:
                            self.board.selectionner_direction("haut")
                            self.direction_ui = "haut"
                        elif event.key == pygame.K_s:
                            self.board.selectionner_direction("bas")
                            self.direction_ui = "bas"
                        elif event.key == pygame.K_q:
                            self.board.selectionner_direction("gauche")
                            self.direction_ui = "gauche"
                        elif event.key == pygame.K_d:
                            self.board.selectionner_direction("droite")
                            self.direction_ui = "droite"
        
                        elif event.key == pygame.K_SPACE:
                            self.board.se_deplacer()
                            
                        elif event.key == pygame.K_m:
                            self.board.ouvrir_magasin()
                            continue

                    

                        elif event.key == pygame.K_e:
                            self.board.interagir()
                            
        
                
                elif self.board.mode == "choix_piece":
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_LEFT:
                            self.board.changer_selection_tirage("gauche")
                        elif event.key == pygame.K_RIGHT:
                            self.board.changer_selection_tirage("droite")
                        elif event.key == pygame.K_RETURN:  
                            self.board.placer_piece_choisie()
                        elif event.key == pygame.K_r:  # R comme Relancer
                            self.board.relancer_tirage()
                        # elif event.key == pygame.K_ESCAPE:
                        #     self.board.annuler_tirage()
                        
                            
                            
                elif self.board.mode == "choix_objet":
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_UP:
                            self.board.choisir_objet("haut")
                        elif event.key == pygame.K_DOWN:
                            self.board.choisir_objet("bas")
                        elif event.key == pygame.K_RETURN:
                            self.board.ramasser_objet_selectionne()
                              
                    
                elif self.board.mode == "porte":
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_RETURN:
                            self.board.confirmer_ouverture_porte(True)
                        elif event.key == pygame.K_ESCAPE:
                            self.board.confirmer_ouverture_porte(False)
                        
                            
                        

            
            # 1) Plus de pas → Game Over
            if self.joueur.get_quantite("Pas") <= 0 and not fin_de_partie:
                fin_de_partie = True
                self.board.message = "Plus de pas va falloir dormir"
            
            # 2) Arrivée en Antechambre → Victoire
            if (self.board.ligne_joueur == self.board.ligne_antechambert and
                self.board.colonne_joueur == self.board.colonne_antechambert and
                not fin_de_partie):
                fin_de_partie = True
                self.board.message = "Objectif Antechamber atteint"

            self.Partie_Salle()
            self.Partie_Inventaire()
            pygame.display.flip()
            self.clock.tick(30)

        pygame.quit()
        