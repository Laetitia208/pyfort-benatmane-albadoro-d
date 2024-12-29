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

def demande_position():
    print("Saisissez une position (ligne,colonne) entre 1 et 3 :")
    pos = str(input())
    nombres = pos.split(",")
    entiers = [int(nombre) for nombre in nombres]       #Faut peut-être changer ça car ca marche pas avec des str
    correct = False
    while correct == False:
        if len(entiers) == 2:
            if entiers[0] >= 1 and entiers[0] <= 3 and entiers[1] >=1 and entiers[1] <=3 :
                correct = True
                return (entiers[0],entiers[1])
            else:
                print("Saisissez une position (ligne,colonne) entre 1 et 3 :")
                pos = str(input())
                nombres = pos.split(",")
                entiers = [int(nombre) for nombre in nombres]
        else:
            print("Saisissez une position (ligne,colonne) entre 1 et 3 :")
            pos = str(input())
            nombres = pos.split(",")
            entiers = [int(nombre) for nombre in nombres]

def init():
    grille = grille_vide()
    for i in range(2):
        libre = False
        while libre == False:
            position = demande_position()
            if grille[position[0]-1][position[1]-1] == " ":
                grille[position[0]-1][position[1]-1] = "B"
                print(position)
                libre = True
    return affiche_grille(grille,"Rappel de l'historique des tirs que vous avez effectués :")





