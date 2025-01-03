#Fort Boyard Simulator
#Laetitia BENATMANE, Nicolas ALBADORO
#Ce fichier comporte l'épreuve de logique, la Bataille Navale, et permet de la lancer


def suiv(indice):                                #Cette fonction permet de passer la main au joueur suivant, elle retourne 0 ou 1
    if indice == 0:                              #Si c'est le joueur 0 qui joue,
        return 1                                 #C'est au tour du joueur 1
    if indice == 1:                              #Si c'est le joueur 1 qui joue,
        return 0                                 #C'est au tour du joueur 0

def grille_vide():                               #Cette fonction crée un tableau 2D 3x3 remplie avec des espaces " " et le retourne
    grille = [[" "," "," "],[" "," "," "],[" "," "," "]]
    return grille

def affiche_grille(grille,message):              #Cette fonction prend en paramètre une grille et un message puis affiche le message et le tableau 2D ligne par ligne
    print(message)
    for ligne in grille:                         #Le tableau 2D est parcouru
        nvl_ligne = ""                           #À chaque ligne, remet une ligne vide "" pour ensuite la remplir
        for case in ligne:
            nvl_ligne = nvl_ligne+" | "+case     #On ajoute ensuite les cases de la ligne parcourue et une séparation " | " à la nouvelle ligne
        nvl_ligne = nvl_ligne+" |"               #On ajoute une dernière séparation " |" à la ligne
        print(nvl_ligne)                         #Et ensuite, elles s'affichent une par une
    print(" -------------")

import re

def demande_position():                          #Cette fonction demande une position valide dans la grille au joueur et retourne un tuple de deux entiers
    print("Saisissez une position (ligne,colonne) entre 1 et 3 :")
    pos = str(input())
    nombres = re.findall(r'\d+', pos)    #Le module re va permettre de trouver les nombres entiers présents dans la saisie du joueur
    entiers = [int(nombre) for nombre in nombres]#Ces nombres sont ensuite placés dans la liste entiers
    correct = False
    while correct == False:                      #Cette boucle permet d'effectuer une saisie sécurisée afin d'obtenir une saisie sous la forme de deux entiers compris entre 1 et 3
        if len(entiers) == 2:                    #On vérifie s'il y a bien deux entiers
            if entiers[0] >= 1 and entiers[0] <= 3 and entiers[1] >=1 and entiers[1] <=3 :
                correct = True
                print("Bateau choisi :",(entiers[0],entiers[1]))
                return (entiers[0],entiers[1])   #Si c'est correcte, la boucle s'arrête et les coordonnées sont retournées
            else:
                print("Saisissez une position (ligne,colonne) entre 1 et 3 :")
                pos = str(input())               #Sinon, une saisie est redemandée au joueur
                nombres = re.findall(r'\d+', pos)
                entiers = [int(nombre) for nombre in nombres]
        else:
            print("Saisissez une position (ligne,colonne) entre 1 et 3 :")
            pos = str(input())                   #S'il y a plus de deux entiers, une saisie est redemandée
            nombres = re.findall(r'\d+', pos)
            entiers = [int(nombre) for nombre in nombres]

def init():                                      #Cette fonction initialise la grille de jeu du joueur et retourne un tableau 2D
    grille = grille_vide()                       #Elle crée une grille vide
    print("Positionnez vos bateaux :")
    for i in range(2):                           #Elle va ensuite demander au joueur de placer deux bateaux
        libre = False
        while libre == False:
            print("Bateau",i+1)
            position = demande_position()        #Le joueur saisi une position
            if grille[position[0]-1][position[1]-1] == " ":  #Si la position est libre dans la grille
                grille[position[0]-1][position[1]-1] = "B"   #Alors un bateau "B" est placé
                libre = True                     #Et la boucle se ferme
    return grille

import random
import time

def tour(joueur, grille_tirs_joueur, grille_adversaire): #Cette fonction permet d'organiser un tour de jeu et prend en paramètre le numéro du joueur, sa grille de tirs et la grille de l'adversaire
    if joueur == 1 :                             #Si c'est le tour du joueur 1, c'est-à-dire au maître du jeu,
        time.sleep(1.5)
        print("C'est le tour du maître du jeu :")
        l = random.randint(1,3)           #Deux nombres entiers (ligne et colonne) sont choisi au hasard entre 1 et 3
        c = random.randint(1,3)
        time.sleep(1.5)
        print("Le maître du jeu tire en position",l,",",c)
        if grille_adversaire[l - 1][c - 1] == "-": #Si la position l,c de la grille de l'adversaire est égale à "-", cela signifie que le joueur a déjà touché au moins une fois cette case
            print("Le maître du jeu a touché le même bateau")
        if grille_adversaire[l-1][c-1] == " ":   #Si la position l,c de la grille de l'adversaire est égale à " ",
            grille_tirs_joueur[l-1][c-1] = "."   #Alors il n'y a pas de bateau à cet emplacement et on place un point "." sur la grille de tirs du joueur
            time.sleep(1)
            print("Dans l'eau...")
        if grille_adversaire[l-1][c-1] == "B":   #Si la position l,c de la grille de l'adversaire est égale à "B",
            grille_tirs_joueur[l-1][c-1] = "x"   #Alors il y a bien un bateau à cet emplacement et on place une croix "x" sur la grille de tirs du joueur
            grille_adversaire[l-1][c-1] = "-"    #Et un moins "-" sur la grille de l'adversaire
            time.sleep(1)
            print("Touché coulé !")
    if joueur == 0 :                             #Si c'est le tour du joueur 2, c'est-à-dire à l'utilisateur,
        time.sleep(1.5)
        print("C'est à votre tour de faire feu ! :")
        time.sleep(1.5)
        print("Rappel de l'historique des tirs que vous avez effectués :")
        affiche_grille(grille_tirs_joueur,"") #La fonction affiche la grille de tirs déjà effectués du joueur
        pos = demande_position()                 #Le joueur entre ensuite une position avec la fonction demande_position()
        if grille_adversaire[pos[0]-1][pos[1]-1] == "-":   #Si la position dans la grille de l'adversaire entrée par le joueur est égale à "-", cela signifie que le joueur a déjà touché au moins une fois cette case
            print("Oups, vous avez encore touché ce bateau...")
        if grille_adversaire[pos[0]-1][pos[1]-1] == " ":   #Si la position dans la grille de l'adversaire entrée par le joueur est égale à " ",
            grille_tirs_joueur[pos[0]-1][pos[1]-1] = "."   #Alors il n'y a pas de bateau à cet emplacement et on place un point "." sur la grille de tirs du joueur
            print("Dans l'eau...")
        if grille_adversaire[pos[0]-1][pos[1]-1] == "B":   #Si la position dans la grille de l'adversaire entrée par le joueur est égale à "B",
            grille_tirs_joueur[pos[0]-1][pos[1]-1] = "x"   #Alors il y a bien un bateau à cet emplacement et on place une croix "x" sur la grille de tirs du joueur
            grille_adversaire[pos[0]-1][pos[1]-1] = "-"    #Et un moins "-" sur la grille de l'adversaire
            time.sleep(1)
            print("Touché coulé !")

def gagne(grille_tirs_joueur):                   #Cette fonction retourne un booléen en fonction de si la grille de tirs prise en paramètre est gagnante ou pas
    bateaux_touches = 0                          #Le nombre de bateaux touchés est initialisé à 0
    tous_touches = False
    for ligne in grille_tirs_joueur:             #La fonction parcours toutes les cases de la grille prise en paramètre
        for case in ligne:
            if case == "x":                      #Si la case est égale à "x", c'est à dire qu'un bateau a été touché à cette position,
                bateaux_touches += 1             #Alors on ajoute 1 au nombre de bateaux touchés
    if bateaux_touches == 2:                     #Chaque joueur possède 2 bateaux, donc si le nombre de bateaux touchés est égal à 2,
        tous_touches = True                      #Alors le joueur a gagné
    return tous_touches                          #Sinon il n'a pas encore gagné

def init_grille_maitre():                        #Cette fonction initialise la grille de jeu du maître du jeu et retourne un tableau 2D
    grille_maitre = grille_vide()                #Elle crée une grille vide
    for i in range(2):                           #Et va ensuite placer deux bateaux
        libre = False
        while libre == False:
            l = random.randint(1,3)        #Elle va ensuite prendre deux nombre aléatoirement l,c entre 1 et 3
            c = random.randint(1,3)
            if grille_maitre[l-1][c-1] == " ":   #Si l'emplacement dans la grille est libre
                grille_maitre[l-1][c-1] = "B"    #Alors un bateau "B" est placé
                libre = True                     #Et la boucle se ferme
    return grille_maitre

def jeu_bataille_navale():                       #Cette fonction effectue le déroulement du jeu de la bataille navale et retourne un booléen
    print("Ce jeu se nomme 'La Bataille Navale'. Pour jouer, chaque joueur doit placer 2 bateaux sur une grille 3x3.")
    print("Les bateaux sont représentés par 'B' et les tirs manqués par '.'. Les bateaux coulés sont marqués par 'x'.")
    print("")
    grille_joueur = init()                       #La grille du joueur est initialisée avec la fonction init()
    affiche_grille(grille_joueur,"Découvrez votre grille de jeu avec vos bateaux :") #Elle est ensuite affichée grace à la fonction affiche_grille()
    grille_maitre = init_grille_maitre()         #La grille du maître du jeu est initialisée avec la fonction init_grille_maitre()
    grille_tirs_joueur = grille_vide()           #La grille de tirs du joueur est initialisée avec une grille vide
    grille_tirs_maitre = grille_vide()           #La grille de tirs du maître du jeu est initialisée avec une grille vide
    fini = False
    j = 1
    while fini == False:                         #Tant qu'aucun des deux jours n'a gagné,
        j = suiv(j)                              #On passe au joueur suivant
        if j == 0:                               #Si c'est au tour du joueur,
            tour(j,grille_tirs_joueur,grille_maitre) #Le tour du joueur est lancé avec la fonction tour() avec en paramètres la grille de trirs du joueur et la grille du maître
            print("")
        if j == 1:                               #Si c'est au tour du maître du jeu,
            tour(j,grille_tirs_maitre,grille_joueur) #Le tour du maître est lancé avec la fonction tour() avec en paramètres la grille de trirs du maître et la grille du joueur
            print("")
        if gagne(grille_tirs_joueur) == True:    #Si la grille de tirs du joueur est gagnante,
            print("Vous avez gagné !")
            fini = True
            return True                          #Alors le joueur a gagné et on sort de la boucle while
        if gagne(grille_tirs_maitre) == True:    #Si la grille de tirs du maître du jeu est gagante,
            print("Dommage, le maître a gagné !")
            fini = True
            return False                         #Alors le maître du jeu a gagné et on sort de la boucle while


"""jeu_bataille_navale()"""