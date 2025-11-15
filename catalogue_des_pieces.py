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
    portes={
        "haut": True,       
        "droite": True,   
        "bas": False,
        "gauche": True},
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
    portes={
        "haut": False,       
        "droite": True,   
        "bas": True,
        "gauche": True},
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
    portes={
        "haut": False,       
        "droite": True,   
        "bas": True,
        "gauche": True},
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
    portes={
        "haut": True,       
        "droite": False,   
        "bas": True,
        "gauche": False},
    type_de_piece= "normal",
    cout_gemmes = 0,
    effet = None,
    rarete = N_A,
)

Rotunda = Piece(
    nom = "Rotunda",
    image = "assets/rooms/Rotunda.png",  
    portes={
        "haut": False,       
        "droite": False,   
        "bas": True,
        "gauche": True},
    type_de_piece= "normal",
    cout_gemmes = 3,
    objets = [],
    effet = None,
    rarete = RARE,
)

Parlor = Piece(
    nom = "Parlor",
    image = "assets/rooms/Parlor.png",  
    portes={
        "haut": False,       
        "droite": False,   
        "bas": True,
        "gauche": True},
    type_de_piece= "normal",
    cout_gemmes = 0,
    objets = [["puzzle", 1]],
    effet = None,
    rarete = COMMONPLACE,
)

BilliardRoom = Piece(
    nom = "BilliardRoom",
    image = "assets/rooms/Billiard_Room.png",  
    portes={
        "haut": False,       
        "droite": False,   
        "bas": True,
        "gauche": True},
    type_de_piece= "normal",
    cout_gemmes = 0,
    objets = [["puzzle", 1]],
    effet = None,
    rarete = COMMONPLACE,
)

Gallery = Piece(
    nom = "Gallery",
    image = "assets/rooms/Gallery.png",  
    portes={"haut": True,"droite": False,"bas": True,"gauche": False},
    type_de_piece= "normal",
    cout_gemmes = 0,
    objets = [["puzzle", 1]],
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
    objets = [["aleatoire", 2]],
    effet = None,
    rarete = COMMONPLACE,
)

WalkInCloset = Piece(
    nom = "Walk-InCloset",
    image = "assets/rooms/Walk-in_Closet.png",  
    portes={"haut": False,"droite": False,"bas": True,"gauche": False},
    type_de_piece= "normal",
    cout_gemmes = 1,
    objets = [["aleatoire", 4]],
    effet = None,
    rarete = STANDART,
)

Attic = Piece(
    nom = "Attic",
    image = "assets/rooms/Attic.png",  
    portes={"haut": False,"droite": False,"bas": True,"gauche": False},
    type_de_piece= "normal",
    cout_gemmes = 3,
    objets = [["aleatoire", 4]],
    effet = None,
    rarete = RARE,
)

StoreRoom = Piece(
    nom = "StoreRoom",
    image = "assets/rooms/StoreRoom.png",  
    portes={"haut": False,"droite": False,"bas": True,"gauche": False},
    type_de_piece= "normal",
    cout_gemmes = 0,
    objets = [["cle", 1], ["gemme", 1], ["or", 1]],
    effet = None,
    rarete = COMMONPLACE,
)

Nook = Piece(
    nom = "Nook",
    image = "assets/rooms/Nook_icon.png",  
    portes={"haut": False,"droite": False,"bas": True,"gauche": True},
    type_de_piece= "normal",
    cout_gemmes = 0,
    objets = [["cle", 1]],
    effet = None,
    rarete = COMMONPLACE,
)

Garage = Piece(
    nom = "Garage",
    image = "assets/rooms/Garage.png",  
    portes={"haut": False,"droite": False,"bas": True,"gauche": False},
    type_de_piece= "normal",
    cout_gemmes = 1,
    objets = [["cle", 3]],
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
    objets = [["cle", 1]],
    effet = None,
    rarete = UNUSUAL,
    
)

LockerRoom = Piece(
    nom = "Locker Room",
    image = "assets/rooms/Locker_Room_Icon.png",  
    portes={"haut": True,"droite": False,"bas": True,"gauche": False},
    type_de_piece= "normal",
    cout_gemmes = 1,
    objets = [["cle", 1]],
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
    objets = [["gemme", 1]],
    effet = None,
    rarete = COMMONPLACE,
    
)

WineCellar = Piece(
    nom = "Wine Cellar",
    image = "assets/rooms/Wine_Cellar_Icon.png",  
    portes={"haut": False,"droite": False,"bas": True,"gauche": False},
    type_de_piece= "normal",
    cout_gemmes = 0,
    objets = [["gemme", 1]],
    effet = None,
    rarete = UNUSUAL,
    
)

TrophyRoom = Piece(
    nom = "Tropy Room",
    image = "assets/rooms/Trophy_Room_Icon.png",  
    portes={"haut": False,"droite": False,"bas": True,"gauche": True},
    type_de_piece= "normal",
    cout_gemmes = 5,
    objets = [["gemme", 8]], 
    effet = None,
    rarete = RARE,
    
)

BallRoom = Piece(
    nom = "BallRoom",
    image = "assets/rooms/Ballroom_Icon.png",  
    portes={"haut": True,"droite": False,"bas": True,"gauche": False},
    type_de_piece= "normal",
    cout_gemmes = 2,
    objets = [["gemme", 3]],
    effet = "chaque fois qu'on rentre dans cette piece sa met nos gemmes a 2 gemmes",
    rarete = UNUSUAL,
    
)

Pantry = Piece(
    nom = "Pantry",
    image = "assets/rooms/Pantry.png",  
    portes={"haut": False,"droite": False,"bas": True,"gauche": True},
    type_de_piece= "normal",
    cout_gemmes = 0,
    objets = [["or", 4], ["pomme", 1]],#4 piece or et 1 fruit
    effet = None,
    rarete = COMMONPLACE,
    
)

RumpusRoom = Piece(
    nom = "Rumpus Room",
    image = "assets/rooms/Rumpus_Room_Icon.png",  
    portes={"haut": True,"droite": False,"bas": True,"gauche": False},
    type_de_piece= "normal",
    cout_gemmes = 1,
    objets = [["or", 8]],#8 piece d'or
    effet = None,
    rarete = STANDART,
    
)

Vault = Piece(
    nom = "Vault",
    image = "assets/rooms/Vault_Icon.png",  
    portes={"haut": False,"droite": False,"bas": True,"gauche": False},
    type_de_piece= "normal",
    cout_gemmes = 3,
    objets = [["or", 40]],# 40 piece d'or
    effet = None,
    rarete = RARE,
    
)

Office = Piece(
    nom = "Office",
    image = "assets/rooms/Office_Icon.png",  
    portes={"haut": False,"droite": False,"bas": True,"gauche": True},
    type_de_piece= "normal",
    cout_gemmes = 2,
    objets = [["or", "rd" ]],#aleatoirement gagne des pieces
    effet = ["genere des pieces d'or dans le manoir dans les pieces deja placer"],
    rarete = STANDART,
    
)

DrawingRoom = Piece(
    nom = "Drawing Room",
    image = "assets/rooms/Drawing_Room_Icon.png",  
    portes={"haut": False,"droite": True,"bas": True,"gauche": False},
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
    effet = None,#ajoute une copie des pieces deja placer dans la pioche
    rarete = RARE,
    
)

ThePool = Piece(
    nom = "The Pool",
    image = "assets/rooms/The_Pool_Icon.png",  
    portes={"haut": False,"droite": True,"bas": True,"gauche": True},
    type_de_piece= "normal",
    cout_gemmes = 1,
    objets = [],
    effet = None,#ajoute Locker room, sauna et pump room dans la pioche
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
    portes={"haut": False,"droite": True,"bas": True,"gauche": True},
    type_de_piece= "normal",
    cout_gemmes = 1,
    objets = [],#chance de trouver le detecteur de metal et la shovel
    effet = None,
    rarete = UNUSUAL,
    
)

PumpRoom = Piece(
    nom = "Wine Cellar",
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
    portes={"haut": False,"droite": False,"bas": True,"gauche": False},
    type_de_piece= "normal",
    cout_gemmes = 1,
    objets = [["aleatoire", "rd" ]],#aleatoirement des objets
    effet = None,
    rarete = STANDART,
    
)

Workshop = Piece(
    nom = "Workshop",
    image = "assets/rooms/Workshop_Icon.png",  
    portes={"haut": True,"droite": False,"bas": True,"gauche": False},
    type_de_piece= "normal",
    cout_gemmes = 0,
    objets = [["aleatoire", 1 ]],#un objet, 0-2 trou a creuser
    effet = None,
    rarete = UNUSUAL,
    
)

Laboratory = Piece(
    nom = "Laboratory",
    image = "assets/rooms/Laboratory_Icon.png",  
    portes={"haut": False,"droite": False,"bas": True,"gauche": True},
    type_de_piece= "normal",
    cout_gemmes = 1,
    objets = [["aleatoire", 1 ]],
    effet = None,
    rarete = STANDART,
    
)

Sauna = Piece(
    nom = "Sauna",
    image = "assets/rooms/Sauna_Icon.png",  
    portes={"haut": False,"droite": False,"bas": True,"gauche": False},
    type_de_piece= "normal",
    cout_gemmes = 0,
    objets = [["aleatoire", 1]],
    effet = None,
    rarete = UNUSUAL,
    
)

Coatcheck = Piece(
    nom = "Coatcheck",
    image = "assets/rooms/Coat_Check_Icon.png",  
    portes={"haut": False,"droite": False,"bas": True,"gauche": False},
    type_de_piece= "normal",
    cout_gemmes = 0,
    objets = [["aleatoire", 1]],
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
    objets = [["gemme", 2], ["cle", 1]],
    effet = None,
    rarete = RARE,
    
)

DiningRoom = Piece(
    nom = "Dining Room",
    image = "assets/rooms/Dining_Room_Icon.png",  
    portes={"haut": False,"droite": True,"bas": True,"gauche": True},
    type_de_piece= "normal",
    cout_gemmes = 0,
    objets = [["aleatoire", 1]],
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
    image = "assets/rooms/Aquarium_Icon.png",  
    portes={"haut": False,"droite": True,"bas": True,"gauche": True},
    type_de_piece= "normal",
    cout_gemmes = 1,
    objets = [["aleatoire", 1]],
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
    effet = "pas",# 2 pas a chaque fois qu'on rentre dans cette piece
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
    effet = "pas",#10 pas
    rarete = COMMONPLACE,
    
)

Nursery = Piece(
    nom = "Nursery",
    image = "assets/rooms/Nursery_Icon.png",  
    portes={"haut": False,"droite": False,"bas": True,"gauche": False},
    type_de_piece= "Bedroom",
    cout_gemmes = 1,
    objets = [["aleatoire", 1]],
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
    effet = "cle",#1 cle pour chaque bedroom placer
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
    objets = [["gemme", 1]],
    effet = "pas", #1 pas pour chaque piece poser
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
    image = "assets/rooms/Secrete_Passage_Icon.png",  
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
    portes={"haut": False,"droite": True,"bas": True,"gauche": False},
    type_de_piece= "Hallway",
    cout_gemmes = 2,
    objets = [],
    effet = None,#porte du haut toujour ouverte
    rarete = UNUSUAL,
    
)

GreatHall = Piece(
    nom = "Great Hall",
    image = "assets/rooms/Great_Hall_Icon.png",  
    portes={"haut": False,"droite": True,"bas": True,"gauche": False},
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
    objets = [["aleatoire", 1]],
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
    effet = None,#eparpille une gemme dans toute les green room
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
    portes={"haut": False,"droite": False,"bas": True,"gauche": True},
    type_de_piece= "Greenroom",
    cout_gemmes = 2,
    objets = [["aleatoire", 1]],
    effet = None,#augmente les chances de trouver des objets dans les green room
    rarete = UNUSUAL,
    
)

GreenHouse = Piece(
    nom = "Hallway",
    image = "assets/rooms/Greenhouse_Icon.png",  
    portes={"haut": False,"droite": False,"bas": True,"gauche": False},
    type_de_piece= "Greenroom",
    cout_gemmes = 1,
    objets = [["aleatoire", 1]],
    effet = None,#augmente les chances de tirer des green room
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
    image = "assets/rooms/Secret Garden_Icon.png",  
    portes={"haut": False,"droite": True,"bas": True,"gauche": True},
    type_de_piece= "Greenroom",
    cout_gemmes = 0,
    objets = [],
    effet = None,#eparpille des fruits dans le manoir
    rarete = RARE,
    
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
    effet = None,#perd une piece a chaque fois qu'on rentre dans cette piece
    rarete = COMMONPLACE,
    
)

MaidsChamber = Piece(
    nom = "Maid's Chamber",
    image = "assets/rooms/Maids_Chamber_Icon.png",  
    portes={"haut": False,"droite": False,"bas": True,"gauche": True},
    type_de_piece= "Redroom",
    cout_gemmes = 0,
    objets = [],
    effet = None,
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
    image = "assets/rooms/Darkroom_Icon.piece.png",  
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
    effet = None,#divise par deux notre nombre de pas
    rarete = RARE,
    
)

Furnace = Piece(
    nom = "Furnace",
    image = "assets/rooms/Furnace_Icon.png",  
    portes={"haut": False,"droite": False,"bas": True,"gauche": True},
    type_de_piece= "Redroom",
    cout_gemmes = 0,
    objets = [],
    effet = None,#augmente la chance de tirer des red rooms
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
    DarkRoom, Weightroom, Furnace
]
