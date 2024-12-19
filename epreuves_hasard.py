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
