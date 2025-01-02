from enigme_pere_fouras import*
from epreuves_hasard import*
from epreuves_logiques import*
from epreuves_mathematiques import*

def introduction():
    print('Bienvenue dans le jeu !')
    print("Les règles de base sont : \n   - Le joueur doit accomplir des épreuves pour gagner des clés et déverrouiller la salle du trésor\n   - L'objectif est de ramasser trois clés pour accéder à la salle du trésor ")

def composer_equipe():
    print("Il peut y avoir au maximum 3 joueurs dans l'équipe.")
    nombre_joueur = 4 #On initialise cette variable à 4 car 4 est plus grand que 3 et cela permettra d'utiliser la boucle while
    equipe = [] #On crée la liste équipe qui contiendra les profils des joueurs
    nombre_leader = 0 #cette variable comptera si il y a un leader ou non

    while nombre_joueur > 3:
        nombre_joueur = int(input("Combien de joueurs voulez vous inscrire dans l'équipe ? "))
        if nombre_joueur > 3:
            print("Il y a trop de joueur, l'équipe ne doit pas posséder plus de 3 joueurs.\nVeuillez ressaisir le nombre de joueur que vous souhaitez inscrire dans l'équipe !")
        else:
            print("Il y a",nombre_joueur,"joueurs inscrit dans l'équipe.")

    for i in range(nombre_joueur):
        print("Entrez le nom du joueur", i + 1, " : ")
        nom = str(input())
        print("Entrez la profession du joueur", i + 1, " : ")
        profession = str(input())
        print("Le joueur", i + 1, " est-il le leader de l'équipe ? (oui/non): ")
        leader = str(input()).strip().lower() #Pour la simplification, les fonctions strip et lower sont utilisées afin que dans le dictionnaire il y ait bien "oui" ou "non"
        joueur = {"nom": nom,"profession": profession,"leader": leader,"cles_gagnees": 0} #Grâce aux variables ci-dessus, on crée le dictionnaire du joueur qu'on intègre ensuite dans la liste equipe
        equipe.append(joueur)

    for elt in equipe:
        if elt['leader'] == "oui":
            nombre_leader = nombre_leader + 1 #On compte si il y a un leader
    if nombre_leader == 0:
        print("Il n'y a eu aucun leader choisi. Le joueur 1 est choisi comme leader de l'équipe ! ")
        equipe[0]['leader'] = "oui" #On attribue le rôle de leader au joueur 1

    return equipe

def menu_epreuves():
    print("Il y a 4 types d'épreuves,\n les voici :")
    print("1. Épreuve de Mathématiques\n2. Épreuve de Logique\n3. Épreuve du hasard\n4. Énigme du Père Fouras\n")
    print("Saisir votre choix en indiquant le numéro de l'épreuve : ")
    choix = int(input())
    if choix == 1:
        return epreuve_math()
    if choix == 2:
        return jeu_bataille_navale()
    if choix == 3:
        return epreuve_hasard()
    if choix == 4:
        return enigme_pere_fouras()

def choisir_joueur(equipe):
    for i in range(len(equipe)):
        if equipe[i]['leader'] == "oui":
            print(i+1,". ",equipe[i]['nom']," (",equipe[i]['profession'],") - Leader")
        else:
            print(i+1, ". ", equipe[i]['nom'], " (", equipe[i]['profession'], ") - Membre")
    numero_joueur = int(input("Entrez le numéro du joueur : ")) - 1 #On soustrait de 1 car les indices démarrent à 0 et non à 1
    return equipe[numero_joueur]