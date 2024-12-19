#Bataille navale

def suiv(joueur):
    if joueur != 0 or joueur != 1:
        joueur = int(input("Choisis un nombre entre 0 et 1"))
    if joueur == 0:
        print("Vous êtes le joueur 0 et l'autre est le 1")
        return 1
    else:
        print("Vous êtes le joueur 1 et l'autre est le 0")
        return 0

def grille_vide():
    grille = [3*[3*[" "]], 3*[3*[" "]], 3*[3*[" "]]]
    return grille

def affiche_grille(grille,message):
