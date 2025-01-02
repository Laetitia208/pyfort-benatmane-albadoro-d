from random import*

def bonneteau():
    Liste = ['A','B','C'] #on définit une liste contenant les noms de chaque bonneteau
    nombre_tentative = 2 #on définit le nombre de tentative à 2 car il y a 2 tentatives
    BonneLettre = str()
    Choix = str()
    print("Bienvenue sur le jeu Bonneteau !\nLes règles de ce jeu sont : \nLe joueur doit deviner sous quel bonneteau (A, B ou C) se cache la clé. Il dispose de deux essais pour le trouver. À chaque essai, la clé est placée aléatoirement sous l'un des bonneteaux.")
    print("\nLes bonneteaux disponibles sont : le A, le B et le C")
    BonneLettre = choice(Liste) #la variable BonneLettre va prendre aléatoirement un des bonneteaux de la liste
    while nombre_tentative > 0: #On répète tant que le joueur n'a pas fait ses deux tentatives
        print("Il vous reste :",nombre_tentative,"tentatives !")
        print("Saisissez un bonneteau entre le A, le B et le C : ")
        Choix = str(input()) #La variable Choix prend la valeur que le joueur donne
        if Choix in 'abc':
            Choix = chr(ord(Choix)-32) #Si le choix donné par le joueur est en minuscule alors on le convertit en majuscule
        if Choix in 'ABC':
            if Choix == BonneLettre: #Si le choix donné par le joueur est le bon alors la fonction renvoie vrai
                print("Bravo ! Vous avez trouvé la clé !")
                return True
            else:
                print("Vous n'avez pas trouvé la clé !")
            nombre_tentative = nombre_tentative - 1 #On enlève 1 aux nombres de tentatives restantes
        else:
            print("Le choix n'est pas valide")
    print("Vous avez perdu ! \nLa clé se trouvait sous le bonneteau :",BonneLettre)
    return False

def jeu_lance_des():
    print("Bienvenue sur le jeu des lancés de dés !\nLe maître du jeu et vous devez lancer deux dés, le premier qui obtient un 6 gagne, cependant vous avez 3 essais.")
    nombre_essai = 3 #On initalise le nombre d'essai restant à 3
    while nombre_essai > 0: #On répète tant qu'il reste des essais
        print("Il vous reste :",nombre_essai,"essais !")
        input("Pour lancer les dés, veuillez appuyer sur la touche **Entrée** !")
        a = randint(1,6) #la variable "a" va prendre une valeur entre 1 et 6 de façon aléatoire
        b = randint(1,6) #la variable "b" va prendre une valeur entre 1 et 6 de façon aléatoire
        des_joueur = (a,b) #on remplit le tuple des_joueur avec les valeurs de "a" et "b"
        print("Vous avez obtenus les valeurs : ",des_joueur)
        if des_joueur[0] == 6 or des_joueur[1] == 6: #On vérifie si il y a un 6 dans le tuple des_joueur
            print("Vous avez gagné ! \nVous remportez la clé !")
            return True
        else:
            print("C'est au tour du maître du jeu !")
        c = randint(1,6) #la variable "c" va prendre une valeur entre 1 et 6 de façon aléatoire
        d = randint(1,6) #la variable "d" va prendre une valeur entre 1 et 6 de façon aléatoire
        des_maitre = (c,d)
        print("Les résultats des dés obtenus par le maître du jeu sont : ",des_maitre)
        if des_maitre[0] == 6 or des_maitre[1] == 6: #On vérifie si il y a un 6 dans le tuple des_maitre
            print("Vous avez perdu !\nLe maître du jeu a gagné")
            return False
        else:
            if nombre_essai > 1: #Si il reste un essai alors on annonce qu'il y a une nouvelle tentative après sinon on annonce que c'est la fin du jeu
                print("Aucun 6 n'a été obtenu, on passe au prochain essai")
            else:
                print("Personne n'a eu de 6 sur les 3 essais, c'est un match nul !")
                return False
        nombre_essai = nombre_essai - 1 #On enlève un essai au nombre d'essai restant

def epreuve_hasard():
    epreuves = (bonneteau,jeu_lance_des) #on crée un tuple contenant les fonctions des deux jeux
    epreuve = choice(epreuves) #la variable epreuve va prendre aléatoirement un des jeux
    return epreuve

"""jeu=epreuve_hasard()
jeu()"""