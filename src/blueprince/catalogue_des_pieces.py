from room import Piece
N_A = 100
COMMONPLACE = 0
STANDART = 1
UNUSUAL = 2
RARE = 3

#piece 0 a 46
EntranceHall = Piece(
    nom = "EntranceHall",
    image="assets/rooms/Entrancehall.png",  
    portes={"haut": True,"droite": True,"bas": False,"gauche": True},
    type_de_piece= "normal",
    cout_gemmes = 0,
    objets=[],
    effet = None,
    rarete = N_A,
    niveaux_portes = {"haut": 0,"droite": 0,"bas": None,"gauche": 0}
)

Antechamber = Piece(
    nom = "Antechamber",
    image = "assets/rooms/Antechamber.png",  
    portes={"haut": True,"droite": True,"bas": True,"gauche": True},
    type_de_piece= "normal",
    cout_gemmes = 0,
    objets = [],
    effet = None,
    rarete = N_A,
    niveaux_portes = {"haut": None,"droite": 2,"bas": 2,"gauche": 2}
)

TheFondation = Piece(
    nom = "TheFondation",
    image = "assets/rooms/The_Foundation.png",  
    portes={"haut": False,"droite": True,"bas": True,"gauche": True},
    type_de_piece= "normal",
    cout_gemmes = 0,
    objets = [],
    effet = None,
    rarete = RARE,
    condition = "impossible_dans_les_coins"
)

SpareRoom = Piece(
    nom = "SpareRoom",
    image = "assets/rooms/SpareRoom.png",  
    portes={"haut": True,"droite": False,"bas": True,"gauche": False},
    type_de_piece= "normal",
    cout_gemmes = 0,
    effet = None,
    rarete = N_A,
)

Rotunda = Piece(
    nom = "Rotunda",
    image = "assets/rooms/Rotunda.png",  
    portes={"haut": False,"droite": False,"bas": True,"gauche": True},
    type_de_piece= "normal",
    cout_gemmes = 3,
    objets = [],
    effet = None,
    rarete = RARE,
)

Parlor = Piece(
    nom = "Parlor",
    image = "assets/rooms/Parlor.png",  
    portes={"haut": False,"droite": False,"bas": True,"gauche": True},
    type_de_piece= "normal",
    cout_gemmes = 0,
    objets = ["puzzle"] + ["aleatoire"] * 2,
    effet = None,
    rarete = COMMONPLACE,
)

BilliardRoom = Piece(
    nom = "BilliardRoom",
    image = "assets/rooms/Billiard_Room.png",  
    portes={"haut": False,"droite": False,"bas": True,"gauche": True},
    type_de_piece= "normal",
    cout_gemmes = 0,
    objets = ["puzzle"],
    effet = None,
    rarete = COMMONPLACE,
)

Gallery = Piece(
    nom = "Gallery",
    image = "assets/rooms/Gallery.png",  
    portes={"haut": True,"droite": False,"bas": True,"gauche": False},
    type_de_piece= "normal",
    cout_gemmes = 0,
    objets = ["puzzle"],
    effet = None,
    rarete = RARE,
    condition = "debloquer_la_room_46"
)

Room8= Piece(
    nom = "Room8",
    image = "assets/rooms/Room_8.png",  
    portes={"haut": False,"droite": False,"bas": True,"gauche": True},
    type_de_piece= "normal",
    cout_gemmes = 0,
    objets = [],
    effet = None,
    rarete = RARE,
)

Closet = Piece(
    nom = "Closet",
    image = "assets/rooms/Closet.png",  
    portes={"haut": False,"droite": False,"bas": True,"gauche": False},
    type_de_piece= "normal",
    cout_gemmes = 0,
    objets = ["aleatoire","aleatoire"],
    effet = None,
    rarete = COMMONPLACE,
    interactions = [{"type": "casier", "quantite": 2}]
)

WalkInCloset = Piece(
    nom = "Walk-InCloset",
    image = "assets/rooms/Walk-in_Closet.png",  
    portes={"haut": False,"droite": False,"bas": True,"gauche": False},
    type_de_piece= "normal",
    cout_gemmes = 1,
    objets = ["aleatoire","aleatoire","aleatoire","aleatoire"],
    effet = None,
    rarete = STANDART,
    interactions = [{"type": "casier", "quantite": 4}]
)

Attic = Piece(
    nom = "Attic",
    image = "assets/rooms/Attic.png",  
    portes={"haut": False,"droite": False,"bas": True,"gauche": False},
    type_de_piece= "normal",
    cout_gemmes = 3,
    objets = ["aleatoire","aleatoire","aleatoire","aleatoire"],
    effet = None,
    rarete = RARE,
    interactions = [{"type": "coffre", "niveau": 1, "quantite": 2}]
)

StoreRoom = Piece(
    nom = "StoreRoom",
    image = "assets/rooms/StoreRoom.png",  
    portes={"haut": False,"droite": False,"bas": True,"gauche": False},
    type_de_piece= "Shop",
    cout_gemmes = 0,
    objets = [],
    effet = None,
    rarete = COMMONPLACE,
    commerce = [
        {"nom": "Gemme de réserve (+1)", "cout": 3, "gain": {"ressource": "Gemmes", "quantite": 1}},
        {"nom": "Dé poussiéreux (+1)", "cout": 4, "gain": {"ressource": "Des", "quantite": 1}},
        {"nom": "Pelle robuste", "cout": 8, "gain": {"ressource": "Pelle", "quantite": 1}},
    ]
)

Nook = Piece(
    nom = "Nook",
    image = "assets/rooms/Nook_icon.png",  
    portes={"haut": False,"droite": False,"bas": True,"gauche": True},
    type_de_piece= "normal",
    cout_gemmes = 0,
    objets = ['cle'],
    effet = None,
    rarete = COMMONPLACE,
)

Garage = Piece(
    nom = "Garage",
    image = "assets/rooms/Garage.png",  
    portes={"haut": False,"droite": False,"bas": True,"gauche": False},
    type_de_piece= "normal",
    cout_gemmes = 1,
    objets = ["cle","cle", "cle"],
    effet = None,
    rarete = UNUSUAL,
    condition = "uniquement entre la ligne 4 et 8, colonne 0 et 1 via une porte gauche ou haut"
)

MusicRoom = Piece(
    nom = "Music Room",
    image = "assets/rooms/Music_Room_Icon.png",  
    portes={"haut": False,"droite": False,"bas": True,"gauche": True},
    type_de_piece= "normal",
    cout_gemmes = 2,
    objets = ["cle"],
    effet = None,
    rarete = UNUSUAL,
    
)

LockerRoom = Piece(
    nom = "Locker Room",
    image = "assets/rooms/Locker_Room_Icon.png",  
    portes={"haut": True,"droite": False,"bas": True,"gauche": False},
    type_de_piece= "normal",
    cout_gemmes = 1,
    objets = ["cle"],
    effet = None, #eparpille des cle dans le manoir?
    rarete = RARE,
    condition = "avoir placer pool"
    
)

Den = Piece(
    nom = "Den",
    image = "assets/rooms/Den_Icon.png",  
    portes={"haut": False,"droite": True,"bas": True,"gauche": True},
    type_de_piece= "normal",
    cout_gemmes = 0,
    objets = ["gemme"],
    effet = None,
    rarete = COMMONPLACE,
    interactions = [{"type": "coffre", "niveau": 1}]
    
)

WineCellar = Piece(
    nom = "Wine Cellar",
    image = "assets/rooms/Wine_Cellar_Icon.png",  
    portes={"haut": False,"droite": False,"bas": True,"gauche": False},
    type_de_piece= "normal",
    cout_gemmes = 0,
    objets = ["gemme","gemme","gemme"],
    effet = None,
    rarete = UNUSUAL,
    interactions = [{"type": "coffre", "niveau": 2}]
    
)

TrophyRoom = Piece(
    nom = "Tropy Room",
    image = "assets/rooms/Trophy_Room_Icon.png",  
    portes={"haut": False,"droite": False,"bas": True,"gauche": True},
    type_de_piece= "normal",
    cout_gemmes = 5,
    objets = ["gemme","gemme","gemme",], #8 gemmes
    effet = None,
    rarete = RARE,
    
)

BallRoom = Piece(
    nom = "BallRoom",
    image = "assets/rooms/Ballroom_Icon.png",  
    portes={"haut": True,"droite": False,"bas": True,"gauche": False},
    type_de_piece= "normal",
    cout_gemmes = 2,
    objets = ["gemme","gemme","gemme"],
    effet = "chaque fois qu'on rentre dans cette piece sa met nos gemmes a 2 gemmes",
    rarete = UNUSUAL,
    
)

Pantry = Piece(
    nom = "Pantry",
    image = "assets/rooms/Pantry.png",  
    portes={"haut": False,"droite": False,"bas": True,"gauche": True},
    type_de_piece= "normal",
    cout_gemmes = 0,
    objets = ["fruit"] + ["or"] * 4,#4 piece or et 1 fruit
    effet = None,
    rarete = COMMONPLACE,
    #or_total = 4
    
)

RumpusRoom = Piece(
    nom = "Rumpus Room",
    image = "assets/rooms/Rumpus_Room_Icon.png",  
    portes={"haut": True,"droite": False,"bas": True,"gauche": False},
    type_de_piece= "normal",
    cout_gemmes = 1,
    objets = ["or"] * 8,
    effet = None,
    rarete = STANDART,
    #or_total = 8
    
)

Vault = Piece(
    nom = "Vault",
    image = "assets/rooms/Vault_Icon.png",  
    portes={"haut": False,"droite": False,"bas": True,"gauche": False},
    type_de_piece= "normal",
    cout_gemmes = 3,
    objets = ["or"] * 40,
    effet = None,
    rarete = RARE,
    #or_total = 40
    
)

Office = Piece(
    nom = "Office",
    image = "assets/rooms/Office_Icon.png",  
    portes={"haut": False,"droite": False,"bas": True,"gauche": True},
    type_de_piece= "normal",
    cout_gemmes = 2,
    objets = ["or"],#aleatoirement gagne des pieces
    effet = {"type": "disperse", "ressource": "or", "quantite": 3},
    rarete = STANDART,
    
)

DrawingRoom = Piece(
    nom = "Drawing Room",
    image = "assets/rooms/Drawing_Room_Icon.png",  
    portes={"haut": False,"droite": True,"bas": True,"gauche": True},
    type_de_piece= "normal",
    cout_gemmes = 1,
    objets = [],
    effet = None,#?
    rarete = COMMONPLACE,
    
)

Study = Piece(
    nom = "Study",
    image = "assets/rooms/Study_Icon.png",  
    portes={"haut": False,"droite": False,"bas": True,"gauche": False},
    type_de_piece= "normal",
    cout_gemmes = 0,
    objets = [],
    effet = ["pour 8 tirage permet d'utiliser des gemmes pour relancer un tirage"],
    rarete = UNUSUAL,
    
)

Library = Piece(
    nom = "Library",
    image = "assets/rooms/Library_Icon.png",  
    portes={"haut": False,"droite": False,"bas": True,"gauche": True},
    type_de_piece= "normal",
    cout_gemmes = 0,
    objets = [],
    effet = None,#reduit les chanche de tirer des pieces commons si on effectue un tirage a partir de cette piece
    rarete = UNUSUAL,
    
)

ChamberOfMirrors = Piece(
    nom = "Chamber of Mirrors",
    image = "assets/rooms/Chamber_of_Mirrors_Icon.png",  
    portes={"haut": False,"droite": False,"bas": True,"gauche": False},
    type_de_piece= "normal",
    cout_gemmes = 0,
    objets = [],
    effet = {"type": "ajout_pioche", "pieces": ["Mirror Room"]},
    rarete = RARE,
    
)

MirrorRoom = Piece(
    nom = "Mirror Room",
    image = "assets/rooms/Chamber_of_Mirrors_Icon.png",
    portes={"haut": True,"droite": True,"bas": True,"gauche": True},
    type_de_piece= "Special",
    cout_gemmes = 0,
    objets = [],
    effet = {"type": "custom_message", "message": "Les reflets brouillent vos sens."},
    rarete = RARE,
    
)

ThePool = Piece(
    nom = "The Pool",
    image = "assets/rooms/The_Pool_Icon.png",  
    portes={"haut": False,"droite": True,"bas": True,"gauche": True},
    type_de_piece= "normal",
    cout_gemmes = 1,
    objets = [],
    effet = {"type": "ajout_pioche", "pieces": ["Locker Room", "Sauna", "Pump Room"]},
    rarete = STANDART,
    
)

DraftingStudio = Piece(
    nom = "Drafting Studio",
    image = "assets/rooms/Drafting_Studio_Icon.png",  
    portes={"haut": True,"droite": False,"bas": True,"gauche": False},
    type_de_piece= "normal",
    cout_gemmes = 2,
    objets = [],
    effet = None,
    rarete = RARE,
    
)

UtilityCloset = Piece(
    nom = "Utility Closet",
    image = "assets/rooms/Utility_Closet_Icon.png",  
    portes={"haut": False,"droite": False,"bas": True,"gauche": False},
    type_de_piece= "normal",
    cout_gemmes = 0,
    objets = [],
    effet = None,
    rarete = STANDART,
    
)

BoilerRoom = Piece(
    nom = "Boiler Room",
    image = "assets/rooms/Boiler_Room_Icon.png",  
    portes={"haut": True,"droite": False,"bas": True,"gauche": True},
    type_de_piece= "normal",
    cout_gemmes = 1,
    objets = [],#chance de trouver le detecteur de metal et la shovel
    effet = None,
    rarete = UNUSUAL,
    
)

PumpRoom = Piece(
    nom = "Pump Room",
    image = "assets/rooms/Pump_Room_Icon.png",  
    portes={"haut": False,"droite": False,"bas": True,"gauche": True},
    type_de_piece= "normal",
    cout_gemmes = 0,
    objets = [],
    effet = None,
    rarete = UNUSUAL,
    condition = "avoir placer the pool"
    
)

Security = Piece(
    nom = "Security",
    image = "assets/rooms/Security_Icon.png",  
    portes={"haut": False,"droite": True,"bas": True,"gauche": True},
    type_de_piece= "normal",
    cout_gemmes = 1,
    objets = [],#aleatoirement des objets
    effet = None,
    rarete = STANDART,
    
)

Workshop = Piece(
    nom = "Workshop",
    image = "assets/rooms/Workshop_Icon.png",  
    portes={"haut": True,"droite": False,"bas": True,"gauche": False},
    type_de_piece= "normal",
    cout_gemmes = 0,
    objets = [],#un objet, 0-2 trou a creuser
    effet = None,
    rarete = UNUSUAL,
    
)

ClockworkRoom = Piece(
    nom = "Clockwork Room",
    image = "assets/rooms/Workshop_Icon.png",
    portes={"haut": True,"droite": False,"bas": True,"gauche": False},
    type_de_piece= "Special",
    cout_gemmes = 0,
    objets = [],
    effet = {"type": "double_cost", "cout": 1},
    rarete = UNUSUAL,
    
)

Laboratory = Piece(
    nom = "Laboratory",
    image = "assets/rooms/Laboratory_Icon.png",  
    portes={"haut": False,"droite": False,"bas": True,"gauche": True},
    type_de_piece= "normal",
    cout_gemmes = 1,
    objets = [],#objet aleatoire
    effet = None,
    rarete = STANDART,
    
)

Sauna = Piece(
    nom = "Sauna",
    image = "assets/rooms/Sauna_Icon.png",  
    portes={"haut": False,"droite": False,"bas": True,"gauche": False},
    type_de_piece= "normal",
    cout_gemmes = 0,
    objets = [],#objet aleatoire
    effet = None,
    rarete = UNUSUAL,
    
)

Coatcheck = Piece(
    nom = "Coatcheck",
    image = "assets/rooms/Coat_Check_Icon.png",  
    portes={"haut": False,"droite": False,"bas": True,"gauche": False},
    type_de_piece= "normal",
    cout_gemmes = 0,
    objets = ["aleatoire"],
    effet = None,
    rarete = STANDART,
    
)

MailRoom = Piece(
    nom = "Mail Room",
    image = "assets/rooms/Mail_Room_Icon.png",  
    portes={"haut": False,"droite": False,"bas": True,"gauche": False},
    type_de_piece= "normal",
    cout_gemmes = 0,
    objets = [],
    effet = None,
    rarete = UNUSUAL,
    
)

Freezer = Piece(
    nom = "Freezer",
    image = "assets/rooms/Freezer_Icon.png",  
    portes={"haut": False,"droite": False,"bas": True,"gauche": False},
    type_de_piece= "normal",
    cout_gemmes = 0,
    objets = ["gemme","gemme","cle"],
    effet = None,
    rarete = RARE,
    
)

DiningRoom = Piece(
    nom = "Dining Room",
    image = "assets/rooms/Dining_Room_Icon.png",  
    portes={"haut": False,"droite": True,"bas": True,"gauche": True},
    type_de_piece= "normal",
    cout_gemmes = 0,
    objets = ["aleatoire"],
    effet = None,
    rarete = STANDART,
    
)

Observatory = Piece(
    nom = "Observatory",
    image = "assets/rooms/Observatory_Icon.png",  
    portes={"haut": False,"droite": False,"bas": True,"gauche": True},
    type_de_piece= "normal",
    cout_gemmes = 1,
    objets = [],
    effet = None,
    rarete = STANDART,
    
)

ConferenceRoom = Piece(
    nom = "Conference Room",
    image = "assets/rooms/Conference_Room_Icon.png",  
    portes={"haut": False,"droite": True,"bas": True,"gauche": True},
    type_de_piece= "normal",
    cout_gemmes = 0,
    objets = [],
    effet = None,#recupere tout les objets eparpiller et les places dans cette pieces
    rarete = UNUSUAL,
    
)

Aquarium = Piece(
    nom = "Aquarium",
    image = "assets/rooms/Aquarim_Icon.png",  
    portes={"haut": False,"droite": True,"bas": True,"gauche": True},
    type_de_piece= "normal",
    cout_gemmes = 1,
    objets = ["aleatoire"],
    effet = None,
    rarete = UNUSUAL,
    
)

#Bedroom

Bedroom = Piece(
    nom = "Bedroom",
    image = "assets/rooms/Bedroom_Icon.png",  
    portes={"haut": False,"droite": False,"bas": True,"gauche": True},
    type_de_piece= "Bedroom",
    cout_gemmes = 0,
    objets = [],
    effet = {"type": "enter_resource", "ressource": "Pas", "quantite": 2, "message": "+2 pas dans la chambre"},
    rarete = COMMONPLACE,
    
)

Boudoir = Piece(
    nom = "Boudoir",
    image = "assets/rooms/Boudoir_Icon.png",  
    portes={"haut": False,"droite": False,"bas": True,"gauche": True},
    type_de_piece= "Bedroom",
    cout_gemmes = 0,
    objets = [],
    effet = "pas",#nb pas aleatoire en plus
    rarete = STANDART,
    
)

GuestBedroom = Piece(
    nom = "Guest Bedroom",
    image = "assets/rooms/Guest_Bedroom_Icon.png",  
    portes={"haut": False,"droite": False,"bas": True,"gauche": False},
    type_de_piece= "Bedroom",
    cout_gemmes = 0,
    objets = [],
    effet = {"type": "enter_resource", "ressource": "Pas", "quantite": 5, "message": "Repos dans la chambre d'amis"},
    rarete = COMMONPLACE,
    
)

Nursery = Piece(
    nom = "Nursery",
    image = "assets/rooms/Nursery_Icon.png",  
    portes={"haut": False,"droite": False,"bas": True,"gauche": False},
    type_de_piece= "Bedroom",
    cout_gemmes = 1,
    objets = ["aleatoire"],
    effet = "pas",# 5 pas pour chaque bedroom placer
    rarete = COMMONPLACE,
    
)

ServantsQuarters = Piece(
    nom = "Servant's Quarters",
    image = "assets/rooms/Servants_Quarters_Icon.png",  
    portes={"haut": False,"droite": False,"bas": True,"gauche": False},
    type_de_piece= "Bedroom",
    cout_gemmes = 1,
    objets = [],
    effet = {"type": "enter_resource", "ressource": "Cle", "quantite": 1, "message": "Les serviteurs partagent une clé"},
    rarete = UNUSUAL,
    
)

BunkRoom = Piece(
    nom = "Bunk Room",
    image = "assets/rooms/Bunk_Room_Icon.png",  
    portes={"haut": False,"droite": False,"bas": True,"gauche": False},
    type_de_piece= "Bedroom",
    cout_gemmes = 0,
    objets = [],
    effet = None,
    rarete = UNUSUAL,
    
)

HerLadyshipChamber = Piece(
    nom = "Her Ladyships Chamber",
    image = "assets/rooms/Her_Ladyships_Chamber_Icon.png",  
    portes={"haut": False,"droite": False,"bas": True,"gauche": False},
    type_de_piece= "Bedroom",
    cout_gemmes = 0,
    objets = [],
    effet = None, # 10 pas quand on rentre dans le boudoir, 3 gemme dans le walkin closet, 1 seul fois
    rarete = RARE
    
)

MasterBedroom = Piece(
    nom = "Master Bedroom",
    image = "assets/rooms/Master_Bedroom_Icon.png",  
    portes={"haut": False,"droite": False,"bas": True,"gauche": False},
    type_de_piece= "Bedroom",
    cout_gemmes = 2,
    objets = ["gemme"],
    effet = {"type": "draw_resource", "ressource": "Pas", "quantite": 3},
    rarete = RARE,
    
)

#Hallways

Hallway = Piece(
    nom = "Hallway",
    image = "assets/rooms/Hallway_Icon.png",  
    portes={"haut": False,"droite": True,"bas": True,"gauche": True},
    type_de_piece= "Hallway",
    cout_gemmes = 0,
    objets = [],
    effet = None,
    rarete = COMMONPLACE,
    
)

WestWingHall = Piece(
    nom = "West Wing Hall",
    image = "assets/rooms/West_Wing_Hall_Icon.png",  
    portes={"haut": False,"droite": True,"bas": True,"gauche": True},
    type_de_piece= "Hallway",
    cout_gemmes = 0,
    objets = [],
    effet = None,
    rarete = STANDART,
    condition = "colonne 0 a 1"
    
)

EastWingHall = Piece(
    nom = "East Wing Hall",
    image = "assets/rooms/East_Wing_Hall_Icon.png",  
    portes={"haut": False,"droite": True,"bas": True,"gauche": True},
    type_de_piece= "Hallway",
    cout_gemmes = 0,
    objets = [],
    effet = None,
    rarete = UNUSUAL,
    condition = "colonne 3 a 5"
    
)

Corridor = Piece(
    nom = "Corridor",
    image = "assets/rooms/Corridor_Icon.png",  
    portes={"haut": True,"droite": False,"bas": True,"gauche": False},
    type_de_piece= "Hallway",
    cout_gemmes = 0,
    objets = [],
    effet = None,# deuxieme porte toujour ouverte
    rarete = COMMONPLACE,
    
)

Passageway = Piece(
    nom = "Hallway",
    image = "assets/rooms/Passageway_Icon.png",  
    portes={"haut": True,"droite": True,"bas": True,"gauche": True},
    type_de_piece= "Hallway",
    cout_gemmes = 2,
    objets = [],
    effet = None,
    rarete = COMMONPLACE,
    
)

SecretPassage = Piece(
    nom = "Secret Passage",
    image = "assets/rooms/Secret_Passage_Icon.png",  
    portes={"haut": False,"droite": False,"bas": True,"gauche": False},
    type_de_piece= "Hallway",
    cout_gemmes = 1,
    objets = [],
    effet = None,
    rarete = UNUSUAL,
    
)

Foyer = Piece(
    nom = "Foyer",
    image = "assets/rooms/Foyer_Icon.png",  
    portes={"haut": True,"droite": False,"bas": True,"gauche": False},
    type_de_piece= "Hallway",
    cout_gemmes = 2,
    objets = [],
    effet = None,#porte du haut toujour ouverte
    rarete = UNUSUAL,
    
)

GreatHall = Piece(
    nom = "Great Hall",
    image = "assets/rooms/Great_Hall_Icon.png",  
    portes={"haut": True,"droite": False,"bas": True,"gauche": False},
    type_de_piece= "Hallway",
    cout_gemmes = 0,
    objets = [],
    effet = None,
    rarete = UNUSUAL,
    
)

#green room

Terrace = Piece(
    nom = "Terrace",
    image = "assets/rooms/Terrace_Icon.png",  
    portes={"haut": False,"droite": False,"bas": True,"gauche": False},
    type_de_piece= "Greenroom",
    cout_gemmes = 0,
    objets = ["aleatoire"],
    effet = None,#une fois poser toute les green rooms coutent 0 gemme a poser
    rarete =  STANDART,
    
)

Patio = Piece(
    nom = "Patio",
    image = "assets/rooms/Patio_Icon.png",  
    portes={"haut": False,"droite": False,"bas": True,"gauche": True},
    type_de_piece= "Greenroom",
    cout_gemmes = 1,
    objets = [],
    effet = {"type": "disperse", "ressource": "gemme", "quantite": 3},
    rarete = COMMONPLACE,
    
)

Courtyard = Piece(
    nom = "Courtyard",
    image = "assets/rooms/Courtyard_Icon.png",  
    portes={"haut": False,"droite": True,"bas": True,"gauche": True},
    type_de_piece= "Greenroom",
    cout_gemmes = 1,
    objets = [],
    effet = None,
    rarete = STANDART,
    
)

Cloister = Piece(
    nom = "Cloister",
    image = "assets/rooms/Cloister_Icon.png",  
    portes={"haut": True,"droite": True,"bas": True,"gauche": True},
    type_de_piece= "Greenroom",
    cout_gemmes = 3,
    objets = [],#2-4 dig spot
    effet = None,
    rarete = UNUSUAL,
    
)

Veranda = Piece(
    nom = "Veranda",
    image = "assets/rooms/Veranda_Icon.png",  
    portes={"haut": True,"droite": False,"bas": True,"gauche": False},
    type_de_piece= "Greenroom",
    cout_gemmes = 2,
    objets = ["aleatoire"],
    effet = {"type": "object_probability", "bonus": 0.1},
    rarete = UNUSUAL,
    
)

GreenHouse = Piece(
    nom = "Greenhouse",
    image = "assets/rooms/Greenhouse_Icon.png",  
    portes={"haut": False,"droite": False,"bas": True,"gauche": False},
    type_de_piece= "Greenroom",
    cout_gemmes = 1,
    objets = ["aleatoire"],
    effet = {"type": "room_probability", "cible": "Greenroom", "delta": 0.5},
    rarete = STANDART,
    
)

MorningRoom = Piece(
    nom = "Morning Room",
    image = "assets/rooms/Morning_Room_Icon.png",  
    portes={"haut": False,"droite": False,"bas": True,"gauche": True},
    type_de_piece= "Greenroom",
    cout_gemmes = 0,
    objets = [],
    effet = None,
    rarete = RARE,
    
)

SecretGaden = Piece(
    nom = "Secret Garden",
    image = "assets/rooms/Secret_Garden_Icon.png",  
    portes={"haut": False,"droite": True,"bas": True,"gauche": True},
    type_de_piece= "Greenroom",
    cout_gemmes = 0,
    objets = [],
    effet = None,#eparpille des fruits dans le manoir
    rarete = RARE,
    interactions = [{"type": "trou", "quantite": 2}]
    
)

#Shop
Commissary = Piece(
    nom = "Commissary",
    image = "assets/rooms/Commissary_Icon.png",  
    portes={"haut": False,"droite": False,"bas": True,"gauche": True},
    type_de_piece= "Shop",
    cout_gemmes = 1,
    objets = [],
    effet = None,
    rarete = STANDART,
    commerce = [
        {"nom": "Ration (+5 pas)", "cout": 2, "gain": {"ressource": "Pas", "quantite": 5}},
        {"nom": "Gemmes de poche", "cout": 5, "gain": {"ressource": "Gemmes", "quantite": 1}}
    ]
    
)

Kitchen = Piece(
    nom = "Kitchen",
    image = "assets/rooms/Kitchen_Icon.png",  
    portes={"haut": False,"droite": False,"bas": True,"gauche": True},
    type_de_piece= "Shop",
    cout_gemmes = 1,
    objets = [],
    effet = None,
    rarete = COMMONPLACE,
    commerce = [
        {"nom": "Repas chaud (+10 pas)", "cout": 3, "gain": {"ressource": "Pas", "quantite": 10}},
        {"nom": "Fruit frais (+3 pas)", "cout": 1, "gain": {"ressource": "Pas", "quantite": 3}}
    ]
    
)

Locksmith = Piece(
    nom = "Locksmith",
    image = "assets/rooms/Locksmith_Icon.png",  
    portes={"haut": False,"droite": False,"bas": True,"gauche": False},
    type_de_piece= "Shop",
    cout_gemmes = 1,
    objets = [],
    effet = None,
    rarete = UNUSUAL,
    commerce = [
        {"nom": "Clé simple", "cout": 3, "gain": {"ressource": "Cle", "quantite": 1}}
    ]
    
)

Showroom = Piece(
    nom = "Showroom",
    image = "assets/rooms/Showroom_Icon.png",  
    portes={"haut": True,"droite": False,"bas": True,"gauche": False},
    type_de_piece= "Shop",
    cout_gemmes = 2,
    objets = [],
    effet = None,
    rarete = RARE,
    commerce = [
        {"nom": "Dé en ivoire", "cout": 4, "gain": {"ressource": "Des", "quantite": 1}},
        {"nom": "Gemmes polies", "cout": 6, "gain": {"ressource": "Gemmes", "quantite": 2}}
    ]
    
)

Laundryroom = Piece(
    nom = "Laundry Room",
    image = "assets/rooms/Laundr_Room_Icon.png",  
    portes={"haut": False,"droite": False,"bas": True,"gauche": False},
    type_de_piece= "Shop",
    cout_gemmes = 1,
    objets = [],
    effet = None,
    rarete = RARE,
    commerce = [
        {"nom": "Nettoyage express (+2 pas)", "cout": 1, "gain": {"ressource": "Pas", "quantite": 2}},
        {"nom": "Réparation d'équipement (+1 clé)", "cout": 4, "gain": {"ressource": "Cle", "quantite": 1}}
    ]
    
)

Bookshop = Piece(
    nom = "Bookshop",
    image = "assets/rooms/Bookshop_Icon.png",  
    portes={"haut": False,"droite": False,"bas": True,"gauche": True},
    type_de_piece= "Shop",
    cout_gemmes = 1,
    objets = [],
    effet = None,
    rarete = RARE,
    commerce = [
        {"nom": "Guide tactique (+1 dé)", "cout": 3, "gain": {"ressource": "Des", "quantite": 1}},
        {"nom": "Atlas secret (+1 gemme)", "cout": 4, "gain": {"ressource": "Gemmes", "quantite": 1}}
    ]
    
)

TheArmory = Piece(
    nom = "The Armory",
    image = "assets/rooms/The_Armory_Icon.png",  
    portes={"haut": False,"droite": False,"bas": True,"gauche": True},
    type_de_piece= "Shop",
    cout_gemmes = 0,
    objets = [],
    effet = None,
    rarete = STANDART,
    commerce = [
        {"nom": "Renforcer l'équipement (+1 clé)", "cout": 3, "gain": {"ressource": "Cle", "quantite": 1}},
        {"nom": "Bouclier improvisé (+5 pas)", "cout": 2, "gain": {"ressource": "Pas", "quantite": 5}}
    ]
    
)

MountHollyGiftShop = Piece(
    nom = "Mount Holly Gift Shop",
    image = "assets/rooms/Mount_Holly_Gift_Shop_Icon.png",  
    portes={"haut": False,"droite": True,"bas": True,"gauche": True},
    type_de_piece= "Shop",
    cout_gemmes = 0,
    objets = [],
    effet = None,
    rarete = RARE,
    commerce = [
        {"nom": "Souvenir (+1 gemme)", "cout": 3, "gain": {"ressource": "Gemmes", "quantite": 1}},
        {"nom": "Porte-bonheur (+1 dé)", "cout": 4, "gain": {"ressource": "Des", "quantite": 1}}
    ]
    
)

#red room
Lavatory = Piece(
    nom = "Lavatory",
    image = "assets/rooms/Lavatory_Icon.png",  
    portes={"haut": False,"droite": False,"bas": True,"gauche": False},
    type_de_piece= "Redroom",
    cout_gemmes = 0,
    objets = [],
    effet = None,
    rarete = STANDART,
    
)

Chapel = Piece(
    nom = "Chapel",
    image = "assets/rooms/Chapel_Icon.png",  
    portes={"haut": False,"droite": True,"bas": True,"gauche": True},
    type_de_piece= "Redroom",
    cout_gemmes = 0,
    objets = [],
    effet = {"type": "enter_resource", "ressource": "Gold", "quantite": -1, "message": "Vous faites une offrande (-1 or)"},
    rarete = COMMONPLACE,
    
)

MaidsChamber = Piece(
    nom = "Maid's Chamber",
    image = "assets/rooms/Maids_Chamber_Icon.png",  
    portes={"haut": False,"droite": False,"bas": True,"gauche": True},
    type_de_piece= "Redroom",
    cout_gemmes = 0,
    objets = [],
    effet = {"type": "object_probability", "bonus": -0.05},
    rarete = UNUSUAL,
    
)

Archives = Piece(
    nom = "Archives",
    image = "assets/rooms/Archives_Icon.png",  
    portes={"haut": True,"droite": True,"bas": True,"gauche": True},
    type_de_piece= "Redroom",
    cout_gemmes = 0,
    objets = [],
    effet = None,
    rarete = UNUSUAL,
    
)

Gymnasium = Piece(
    nom = "Gymnasium",
    image = "assets/rooms/Gymnasium_Icon.png",  
    portes={"haut": False,"droite": True,"bas": True,"gauche": True},
    type_de_piece= "Redroom",
    cout_gemmes = 0,
    objets = [],
    effet = None,#perd 2 pas a chaque fois qu'on rentre dans cette piece
    rarete = STANDART, 
    
)

DarkRoom = Piece(
    nom = "Darkroom",
    image = "assets/rooms/Darkroom_Icon.png",  
    portes={"haut": False,"droite": True,"bas": True,"gauche": True},
    type_de_piece= "Redroom",
    cout_gemmes = 0,
    objets = [],
    effet = None,#cache la grille pendant le tirage
    rarete = STANDART,
    
)

Weightroom= Piece(
    nom = "Weight Room",
    image = "assets/rooms/Weight_Room_Icon.png",  
    portes={"haut": True,"droite": True,"bas": True,"gauche": True},
    type_de_piece= "Redroom",
    cout_gemmes = 0,
    objets = [],
    effet = {"type": "draw_resource", "ressource": "Pas", "quantite": -5},
    rarete = RARE,
    
)

Furnace = Piece(
    nom = "Furnace",
    image = "assets/rooms/Furnace_Icon.png",  
    portes={"haut": False,"droite": False,"bas": True,"gauche": False},
    type_de_piece= "Redroom",
    cout_gemmes = 0,
    objets = [],
    effet = {"type": "room_probability", "cible": "Redroom", "delta": 0.5},
    rarete = RARE,
    
)

catalogue = [
    EntranceHall, Antechamber, TheFondation, SpareRoom, Rotunda,
    Parlor, BilliardRoom, Gallery, Room8, Closet,
    WalkInCloset, Attic, StoreRoom
]

# pioche = [
#     TheFondation, SpareRoom, Rotunda,
#     Parlor, BilliardRoom, Gallery, Room8, Closet,
#     WalkInCloset, Attic, StoreRoom
# ]

pioche = [
    EntranceHall, Antechamber, TheFondation,
    SpareRoom, Rotunda, Parlor,
    BilliardRoom, Gallery, Room8,
    Closet, WalkInCloset, Attic,
    StoreRoom, Nook, Garage,
    MusicRoom, LockerRoom, Den,
    WineCellar, TrophyRoom, BallRoom,
    Pantry, RumpusRoom, Vault,
    Office, DrawingRoom, Study,
    Library, ChamberOfMirrors, ThePool,
    DraftingStudio, UtilityCloset, BoilerRoom,
    PumpRoom, Security, Workshop,
    Laboratory, Sauna, Coatcheck,
    MailRoom, Freezer, DiningRoom,
    Observatory, ConferenceRoom, Aquarium,
    Bedroom, Boudoir, GuestBedroom,
    Nursery, ServantsQuarters, BunkRoom,
    HerLadyshipChamber, MasterBedroom, Hallway,
    WestWingHall,EastWingHall, Corridor, Passageway,
    SecretPassage, Foyer, GreatHall,
    Terrace, Patio, Courtyard,
    Cloister, Veranda, GreenHouse,
    MorningRoom, SecretGaden, Commissary,
    Kitchen, Locksmith, Showroom,
    Laundryroom, Bookshop, TheArmory,
    MountHollyGiftShop, Lavatory, Chapel,
    MaidsChamber, Archives, Gymnasium,
    DarkRoom, Weightroom, Furnace, MirrorRoom, ClockworkRoom
]


def obtenir_piece_par_nom(nom):
    for piece in pioche:
        if piece.nom == nom:
            return piece
    return None
