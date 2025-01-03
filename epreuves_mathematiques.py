#Fort Boyard Simulator
#Laetitia BENATMANE, Nicolas ALBADORO
#Ce fichier comporte les épreuves mathématiques et permet d'en lancer une

def factorielle(n):                                                   #Cette fonction calcule la factorielle du nombre n et retourne le résultat
    f = 1
    if n == 0:
        return 1                                                      #0! = 1
    for i in range(1, n+1):                                           #On multiplie f par tous les termes de 1 à n+1
        f = f*i
    return f

import random

def epreuve_math_factorielle():                                       #Cette fonction est une épreuve pour trouver la factorielle d'un nombre entre 1 et 10 et retourne un booléen
    n = random.randint(1, 10)
    print("Epreuve de Mathématiques : calculer la factorielle de", n)
    joueur = int(input())                                             #Le joueur saisi sa réponse
    print("Votre réponse :", joueur)
    reponse = factorielle(n)                                          #Le programme utilise la fonction factorielle(n) pour calculer n!
    if reponse == joueur :
        print("Correct ! Vous gagnez une clé.")
        return True                                                   #Si c'est correcte, la fonction retourne True
    else:
        print("Dommage, mauvaise réponse.")
        return False                                                  #Sinon elle retourne False

def est_premier(n):                                                   #Cette fonction  vérifie si un nombre n est premier et retourne un booléen
    pr = True
    if n <= 1 :
        return False                                                  #Si n<=1, alors n n'est pas premier
    for i in range(2, n):                                             #On vérifie pour toutes les valeurs inférieures à n (2 à n-1) s'il y a des diviseurs de n
        if n % i == 0:
            pr = False
    return pr

def premier_plus_proche(n):                                           #Cette fonction trouve le nombre premier sépérieur ou égal à n le plus proche et retourne la réponse, un entier
    proche = False
    i = n
    while proche == False :
        if est_premier(i) == True:                                    #Si i est permier, la boucle se ferme et la fonction retourne i
            proche = True
            return i
        else:
            i = i + 1                                                 #Sinon on ajoute 1 à i tant que i n'est pas premier

def epreuve_math_premier():                                           #Cette fonction choisi un nombre n aléatoire et demande à l'utilisateur de trouver le nombre premier le plus proche, elle retourne un booléen
    n = random.randint(10, 20)
    print("Epreuve de Mathématiques : trouver le nombre premier supérieur ou égal le plus proche de", n)
    joueur = int(input())                                             #L'utilisateur saisi sa réponse
    print("Votre réponse :", joueur)
    reponse = premier_plus_proche(n)                                  #Cette fonction utilise la fonction premier_plus_proche() pour n
    if reponse == joueur :                                            #Ensuite, il compare la réponse du joueur à la bonne réponse
        print("Correct ! Vous gagnez une clé.")
        return True
    else:
        print("Dommage, mauvaise réponse.")
        return False

def epreuve_roulette_mathematique():                                  #Cette fonction génère un calcul aléatoire et demande au joueur de trouver le résultat, elle retourne un booléen
    nb1 = random.randint(1, 20)                                 #Cinq nombres sont choisis aléatoirement entre 1 et 20
    nb2 = random.randint(1, 20)
    nb3 = random.randint(1, 20)
    nb4 = random.randint(1, 20)
    nb5 = random.randint(1, 20)
    nombres = [nb1, nb2, nb3, nb4, nb5]                               #Ces nombres sont ensuite rangés dans une liste
    print("Nombres sur la roulette :", nombres)
    operation = ("addition", "soustraction", "multiplication")
    o = random.choice(operation)                                      #Une opération est choisie au hasard
    if o == "addition":
        print("Calculez le résultat en combinant ces nombres avec une addition")
        joueur = int(input())
        print("Votre réponse :", joueur)
        reponse = nb1 + nb2 + nb3 + nb4 + nb5                         #Ici, tous les nombres choisis précédemment sont additionnés
    if o == "soustraction":
        print("Calculez le résultat en combinant ces nombres avec une soustraction")
        joueur = int(input())
        print("Votre réponse :", joueur)
        reponse = nb1 - nb2 - nb3 - nb4 - nb5                         #Ici, tous les nombres choisis précédemment sont soustraits
    if o == "multiplication":
        print("Calculez le résultat en combinant ces nombres avec une multiplication")
        joueur = int(input())
        print("Votre réponse :", joueur)
        reponse = nb1 * nb2 * nb3 * nb4 * nb5                         #Ici, tous les nombres choisis précédemment sont multipliés
    if joueur == reponse :                                            #Enfin, la bonne réponse est comparée à celle du joueur
        print("Bonne réponse ! Vous avez gagné une clé.")
        return True                                                   #Si c'est correcte, la fonction retourne True
    else:
        print("Dommage, mauvaise réponse.")
        return False                                                  #Si c'est incorrecte, elle retourne False

def epreuve_math():                                                   #Cette fonction choisi une épreuve au hasard parmi les précédentes, elle retourne une fonction
    epreuves = (epreuve_math_factorielle, epreuve_math_premier, epreuve_roulette_mathematique)
    epreuve = random.choice(epreuves)
    return epreuve                                                    #Elle lance ensuite la fonction (l'épreuve) choisie

"""jeu = epreuve_math()
jeu()"""












