#Bataille navale

def suiv(indice):                                #Cette fonction indique le numéro du joueur suivant
    if indice == 0:
        return 1
    if indice == 1:
        return 0

def grille_vide():                               #Cette fonction crée un tableau 2D 3x3 remplie avec des espaces " "
    grille = [[" "," "," "],[" "," "," "],[" "," "," "]]
    return grille

def affiche_grille(grille,message):              #Cette fonction affiche un message et un tableau 2D ligne par ligne
    print(message)
    for ligne in grille:                         #Le tableau 2D est parcouru
        nvl_ligne = ""                           # Les cases sont séparées par des batons "|"
        for case in ligne:
            nvl_ligne = nvl_ligne+" | "+case     #On ajoute ensuite toutes les cases du tableau et les batons pour les ajouter à la ligne
        nvl_ligne = nvl_ligne+" |"
        print(nvl_ligne)                         #Et ensuite les afficher
    print(" -------------")

import re

def demande_position():
    print("Saisissez une position (ligne,colonne) entre 1 et 3 :")
    pos = str(input())
    nombres = re.findall(r'\d+', pos)
    entiers = [int(nombre) for nombre in nombres]       #Faut peut-être changer ça car ca marche pas avec des str
    correct = False
    while correct == False:
        if len(entiers) == 2:
            if entiers[0] >= 1 and entiers[0] <= 3 and entiers[1] >=1 and entiers[1] <=3 :
                correct = True
                print("Bateau choisi :",(entiers[0],entiers[1]))
                return (entiers[0],entiers[1])
            else:
                print("Saisissez une position (ligne,colonne) entre 1 et 3 :")
                pos = str(input())
                nombres = re.findall(r'\d+', pos)
                entiers = [int(nombre) for nombre in nombres]
        else:
            print("Saisissez une position (ligne,colonne) entre 1 et 3 :")
            pos = str(input())
            nombres = re.findall(r'\d+', pos)
            entiers = [int(nombre) for nombre in nombres]

def init():
    grille = grille_vide()
    print("Positionnez vos bateaux :")
    for i in range(2):
        libre = False
        while libre == False:
            print("Bateau",i+1)
            position = demande_position()
            if grille[position[0]-1][position[1]-1] == " ":
                grille[position[0]-1][position[1]-1] = "B"
                libre = True
    return grille

import random
import time

def tour(joueur, grille_tirs_joueur, grille_adversaire):
    if joueur == 1 :
        time.sleep(1.5)
        print("C'est le tour du maître du jeu :")
        l = random.randint(1,3)
        c = random.randint(1,3)
        time.sleep(1.5)
        print("Le maître du jeu tire en position",l,",",c)
        if grille_adversaire[l - 1][c - 1] == "-":
            print("Le maître du jeu a touché le même bateau")
        if grille_adversaire[l-1][c-1] == " ":
            grille_tirs_joueur[l-1][c-1] = "."
            time.sleep(1)
            print("Dans l'eau...")
        if grille_adversaire[l-1][c-1] == "B":
            grille_tirs_joueur[l-1][c-1] = "x"
            grille_adversaire[l-1][c-1] = "-"
            time.sleep(1)
            print("Touché coulé !")
    if joueur == 0 :
        time.sleep(1.5)
        print("C'est à votre tour de faire feu ! :")
        time.sleep(1.5)
        print("Rappel de l'historique des tirs que vous avez effectués :")
        affiche_grille(grille_tirs_joueur,"")
        pos = demande_position()
        if grille_adversaire[pos[0]-1][pos[1]-1] == "-":
            print("Oups, vous avez encore touché ce bateau...")
        if grille_adversaire[pos[0]-1][pos[1]-1] == " ":
            grille_tirs_joueur[pos[0]-1][pos[1]-1] = "."
            print("Dans l'eau...")
        if grille_adversaire[pos[0]-1][pos[1]-1] == "B":
            grille_tirs_joueur[pos[0]-1][pos[1]-1] = "x"
            grille_adversaire[pos[0]-1][pos[1]-1] = "-"
            time.sleep(1)
            print("Touché coulé !")

def gagne(grille_tirs_joueur):
    bateaux_touches = 0
    tous_touches = False
    for ligne in grille_tirs_joueur:
        for case in ligne:
            if case == "x":
                bateaux_touches += 1
    if bateaux_touches == 2:
        tous_touches = True
    return tous_touches

def init_grille_maitre():
    grille_maitre = grille_vide()
    for i in range(2):
        libre = False
        while libre == False:
            l = random.randint(1,3)
            c = random.randint(1,3)
            if grille_maitre[l-1][c-1] == " ":
                grille_maitre[l-1][c-1] = "B"
                libre = True
    return grille_maitre

def jeu_bataille_navale():
    print("Ce jeu se nomme 'La Bataille Navale'. Pour jouer, chaque joueur doit placer 2 bateaux sur une grille 3x3.")
    print("Les bateaux sont représentés par 'B' et les tirs manqués par '.'. Les bateaux coulés sont marqués par 'x'.")
    print("")
    grille_joueur = init()
    affiche_grille(grille_joueur,"Découvrez votre grille de jeu avec vos bateaux :")
    grille_maitre = init_grille_maitre()
    grille_tirs_joueur = grille_vide()
    grille_tirs_maitre = grille_vide()
    fini = False
    j = 1
    while fini == False:
        j = suiv(j)
        if j == 0:
            tour(j,grille_tirs_joueur,grille_maitre)
            print("")
        if j == 1:
            tour(j,grille_tirs_maitre,grille_joueur)
            print("")
        if gagne(grille_tirs_joueur) == True:
            print("Vous avez gagné !")
            fini = True
            return True
        if gagne(grille_tirs_maitre) == True:
            print("Dommage, le maître a gagné !")
            fini = True
            return False


"""jeu_bataille_navale()"""