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
        self.board = Board()
        self.assets = Assets()
        self.direction_ui = None

        self.tirage_en_cours = []
        self.selection_tirage = 0
        #fusion 
        self.joueur=Joueur()
        
 


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
    
        if self.board.mode == "exploration":
            nom_piece_actuelle = pygame.font.Font(None, 30)
            nom_piece_actuelle = nom_piece_actuelle.render(self.board.grille[self.board.ligne_joueur][self.board.colonne_joueur].nom, True, (0, 0, 0))
            self.screen.blit(nom_piece_actuelle, (450, 375))
        
        texte_inventaire = pygame.font.Font(None, 30)
        texte_inventaire = texte_inventaire.render("Inventaire :", True, (0, 0, 0))
        self.screen.blit(texte_inventaire, (450, 50))
        
        img_pas = pygame.image.load("assets/Inventaire/Steps1.png").convert()
        img_pas = pygame.transform.scale(img_pas, (25,25))
        self.screen.blit(img_pas, ( 1200, 80))

        texte_pas = pygame.font.Font(None, 30)
        texte_pas = texte_pas.render(f"{self.joueur.inventaire["Pas"]["nombre"]}", True, (0, 0, 0))
        self.screen.blit(texte_pas, (1240, 80))
        
        img_gold = pygame.image.load("assets/Inventaire/Gold.png")
        img_gold = pygame.transform.scale(img_gold, (25,25))
        self.screen.blit(img_gold, ( 1200, 120))

        texte_gold = pygame.font.Font(None, 30)
        texte_gold = texte_gold.render(f"{self.joueur.inventaire["or"]["nombre"]}", True, (0, 0, 0))
        self.screen.blit(texte_gold, (1240, 120))
        
        img_gem = pygame.image.load("assets/Inventaire/Gem.png")
        img_gem = pygame.transform.scale(img_gem, (25,25))
        self.screen.blit(img_gem, ( 1200, 160))

        texte_gem = pygame.font.Font(None, 30)
        texte_gem = texte_gem.render(f"{self.joueur.inventaire["gemme"]["nombre"]}", True, (0, 0, 0))
        self.screen.blit(texte_gem, (1240, 160))
        
        img_key = pygame.image.load("assets/Inventaire/Key.png")
        img_key = pygame.transform.scale(img_key, (25,25))
        self.screen.blit(img_key, ( 1200, 200))

        texte_key = pygame.font.Font(None, 30)
        texte_key = texte_key.render(f"{self.joueur.inventaire["cle"]["nombre"]}", True, (0, 0, 0))
        self.screen.blit(texte_key, (1240, 200))
        
        img_dice = pygame.image.load("assets/Inventaire/Ivory_dice.png").convert()
        img_dice = pygame.transform.scale(img_dice, (25,25))
        self.screen.blit(img_dice, ( 1200, 240))

        texte_dice = pygame.font.Font(None, 30)
        texte_dice = texte_dice.render(f"{self.joueur.inventaire["des"]["nombre"]}", True, (0, 0, 0))
        self.screen.blit(texte_dice, (1240, 240))
 
        if self.board.message:
            font_message = pygame.font.Font(None, 30)  
            texte_message = font_message.render(self.board.message, True, (0, 0, 0))  
            self.screen.blit(texte_message, (450, 680))  
                
        
        #tirage du bas affichage
        if self.board.tirage_en_cours:
            font_choix = pygame.font.Font(None, 30)  
            texte_choix = font_choix.render("Choisie une pièce à placer", True, (0, 0, 0))  
            self.screen.blit(texte_choix, (450, 375))  
            
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
                    

        
                
    

    def run(self):
        """"
        Cette méthode gere le lancement de la fenetre de eu et des évenements.
        C'est ici que l'on regarde dans quelle mode on est. 
        """
        running = True
        
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
        
                
                if self.board.mode == "exploration":
                    if event.type == pygame.KEYDOWN:
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
        
                        # elif event.key == pygame.K_SPACE:
                        #     self.board.ouvrir_porte()
                            #en commentaire pour l'instant j'utilise pas se deplacer
                            #self.board.se_deplacer(self.joueur)
                        elif event.key == pygame.K_SPACE:
                            self.board.se_deplacer(self.joueur)
                            
        
                
                elif self.board.mode == "choix_piece":
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_LEFT:
                            self.board.changer_selection_tirage("gauche")
                        elif event.key == pygame.K_RIGHT:
                            self.board.changer_selection_tirage("droite")
                        elif event.key == pygame.K_RETURN:  
                            self.board.placer_piece_choisie(self.joueur)
                              
                    




            self.Partie_Salle()
            self.Partie_Inventaire()
            pygame.display.flip()
            if self.joueur.inventaire["Pas"]==0:
                running = False
            self.clock.tick(30)

        pygame.quit()
