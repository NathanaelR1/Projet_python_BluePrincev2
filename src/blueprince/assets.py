import pygame
import os

class Assets:
    """
    Gère le chargement et la mise en cache des images pour l'affichage.
    """

    def __init__(self):
        self.pieces = {}

        # Chemin ABSOLU vers le dossier "assets"
        self.assets_path = os.path.abspath(
            os.path.join(os.path.dirname(__file__), "..", "..", "assets")
        )

    def charger_image_piece(self, piece, taille):
        """
        Charge l'image d'une pièce, la redimensionne selon le contexte,
        et applique la rotation actuelle de la pièce si nécessaire.
        - taille = 1 → affichage dans la grille (80x80)
        - taille = 2 → affichage du tirage (128x128)
        """
        tailles = {1: (80, 80), 2: (128, 128)}
        target_size = tailles.get(taille, (80, 80))

        angle = getattr(piece, "angle", 0)
        chemin_image = getattr(piece, "image", "")

        # Support des anciens chemins qui commencent par "assets/"
        if chemin_image.startswith("assets/"):
            chemin_image = chemin_image[len("assets/"):]

        # Construction du chemin absolu
        full_path = os.path.join(self.assets_path, chemin_image)

        # Debug si image manquante (ne plante pas le jeu)
        if not os.path.exists(full_path):
            print(f"Image introuvable : {full_path}")

        cle = (full_path, taille, angle)
        if cle in self.pieces:
            return self.pieces[cle]

        img = pygame.image.load(full_path).convert_alpha()
        img = pygame.transform.smoothscale(img, target_size)

        if angle != 0:
            img = pygame.transform.rotate(img, angle)

        self.pieces[cle] = img
        return img
