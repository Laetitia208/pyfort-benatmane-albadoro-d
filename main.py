#Fort Boyard Simulator
#Laetitia BENATMANE, Nicolas ALBADORO
#Ce fichier lance le jeu Fort Boyard Simulator
import time

from fonctions_utiles import*
from epreuve_finale import*

def jeu():
    introduction()
    time.sleep(1.5)
    equipe = composer_equipe()
    nombre_cles = 0
    while nombre_cles < 3:
        print("\nVous avez :",nombre_cles,"clés.\n")
        time.sleep(1)
        type_epreuve = menu_epreuves() #cette variable va prendre le résultat renvoyé par la fonction menu_epreuve()
        choix_joueur = choisir_joueur(equipe) #Cette variable récupère le dictionnaire du joueur sélectionné pour l'épreuve
        resultat = type_epreuve() #cette variable va permettre de savoir si on a gagné ou perdu l'épreuve
        time.sleep(1.5)
        if resultat == True:
            choix_joueur["cles_gagnees"] += 1 #On rajoute une clé au joueur qui a gagné l'épreuve
            nombre_cles += 1 #On rajoute une clé au compteur
    print("\nVous avez obtenus 3 clés !") #Une fois que la variable nombre_cles est égale à 3, le jeu lance l'épreuve finale
    print("\nVous passez à l'épreuve finale")
    time.sleep(1.5)
    salle_De_Tresor() #lance l'épreuve finale




jeux = jeu()
