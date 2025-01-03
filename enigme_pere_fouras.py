#Fort Boyard Simulator
#Laetitia BENATMANE, Nicolas ALBADORO
#Ce fichier comporte l'épreuve de l'énigme du Père Fouras et permet de la lancer

import json

def charger_enigmes():                    #Cette fonction permet d'extraire toutes les énigmes ainsi que leur réponse du fichier enigmesPF.json et retourne un dictionnaire
    with open('./data/enigmesPF.json','r',encoding='utf-8') as f:
        enigmes = json.load(f)            #Le fichier est ouvert est chargé
    d = {}
    for enigme in enigmes:                #Tout le fichier enigmes est parcouru
        d[enigme['question']] = enigme['reponse']  #Et on en extrait les questions et les réponses et on les place dans le dico d
    return d

import random

def enigme_pere_fouras():                 #Cette fonction organise l'épreuve de l'énigme du père fouras et retourne un booléen
    nb_essais = 3                         #Le joueur a 3 essais
    liste_enigmes = (charger_enigmes())   #Toutes les énigmes sont placées dans liste_enigmes grâce à la fonction charger_enigmes()
    enigme_choisie,rep = random.choice(list(liste_enigmes.items())) #Une énigme et sa réponse sont choisies au hasard
    print("Bienvenue dans l'énigme du Père Fouras. Déchiffrez cette énigme pour gagner cette épreuve et obtenir une clé.")
    print("Vous avez le droit à 3 essais. Si vous ne trouvez pas la réponse au bout de ces 3 essais, vous perdez.")
    print("Bonne chance à vous !")
    print("")
    print(enigme_choisie)
    while nb_essais > 0:                  #Tant que le joueur a au moins 1 essai,
        print("")
        print("Saisissez une réponse :")
        reponse = input()                 #Le joueur saisi une réponse
        reponse_min = reponse.lower()     #La réponse du joueur est mise en minuscule
        rep_min = rep.lower()             #La bonne réponse est mise en minuscule
        if reponse_min == rep or reponse == rep or reponse_min == rep_min or reponse == rep_min:
            print("Félicitation, votre réponse est correcte ! Vous avez gagné une clé")
            return True                   #Si la réponse du joueur est correcte, alors il a gagné et la boucle s'arrête, la fonction retourne True
        else:
            nb_essais -= 1                #Si c'est faux, le joueur perd un essai
            if nb_essais > 1:
                print("Malheureusement, votre réponse est incorrecte. Il vous reste",nb_essais,"essais.")
            if nb_essais == 1:
                print("Malheureusement, votre réponse est incorrecte. Il vous reste", nb_essais, "essai.")
            if nb_essais == 0:            #S'il n'a plus d'essais,
                print("Dommage, vous avez échoué à cette épreuve. La réponse était :",rep)
                return False              #Il a perdu est la boucle se ferme, la fonction retourne False
def epreuve_pere_fouras():
    epreuve = enigme_pere_fouras
    return epreuve
"""enigme_pere_fouras()"""
