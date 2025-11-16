# Projet Blue Prince version simplifier

Dans cette version simplifier du jeu Blue Prince le but est d'atteindre l'Antechamber avant d'avoir épuiser son nombre de pas.

## Fonctionalités principales

- Déplacement dans le manoir en posant les pièces au fur et à mesure que l'on avance
- Tirage et placement aleatoire des pièces selon leur raretés
- Gestion des ressources : clés, gemmes, pas, objet permanant...
- Système de portes verouillées (clé ou crochetage)
- Interaction selon le type de pièce
- Ramassage des ressources dans les pièces du manoir

## Prérequis

- Python 3
- Pygame

## Installation

1. Cloner le dépôt
    ```sh
    git clone https://github.com/NathanaelR1/Projet_python_BluePrincev2.git
    ```

2. Créer un environnement virtuel dans le dossier blueprince
    ```sh
    virtualenv <nom_env>
    ```
3. Activer l'environnement virtuelle
    ```sh
    .\<nom_env>\Scripts\activate
    ```
4. Installer les dépendances
    ```sh
    pip install -r requirements.txt
    ```

## Utilisation

    python main.py

## Touche de Controle
1. Mode exploration/porte :
- Déplacement dans le manoir : ZQSD
- Ouvrir/tenter d'ouvrir une porte : ESPACE
- Utiliser clé ou kit de crochetage : ENTREE
- Interagir avec une pièce(creuser) : E

2. Mode choix de pièce:
- Selection des pièces : Flèche directionnelle gauche et droite
- Placer une pièce : ESPACE
- Interagir avec une pièce(creuser) : E
- Relancer un tirage : R

3. Mode choix d'objet :
- Selection des pièces : Flèche directionnelle haut et bas
- Ramasser un objet : ENTREE

4. Echange dans le magasin:
- Selection des pièces : Flèche directionnelle haut et bas
- Acheter : ENTREE
- Ouvrir/Fermer un magasin : M


## Contributeurs 

- NathanaelR1
- Thoms4
- abdelmalekdjelouah-coder