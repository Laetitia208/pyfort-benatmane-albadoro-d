from pydoc import importfile

def factorielle(n):                                                   #Ce programme calcule la factorielle du nombre n
    f = 1
    if n == 0:
        return 1                                                      #0! = 1
    for i in range(1, n+1):                                           #On multiplie f par tous les termes de 1 à n+1
        f = f*i
    return f

import random

def epreuve_math_factorielle():                                       #Ce programme est une épreuve pour trouver la factorielle d'un nombre entre 1 et 10
    n = random.randint(1, 10)
    print("Epreuve de Mathématiques : calculer la factorielle de", n)
    joueur = int(input())                                             #Le joueur entre sa réponse
    print("Votre réponse :", joueur)
    reponse = factorielle(n)                                          #Le programme utilise la fonction factorielle(n) pour calculer n!
    if reponse == joueur :
        print("Correct ! Vous gagnez une clé.")
        return True                                                   #Si c'est correcte, la fonction retourne True
    else:
        print("Dommage, mauvaise réponse.")
        return False                                                  #Sinon elle retourne False

def est_premier(n):                                                   #Cette fonction  vérifie si un nombre n est premier
    pr = True
    if n <= 1 :
        return False                                                  #Si n<=1, alors n n'est pas premier
    for i in range(2, n):                                             #On vérifie pour toutes les valeurs inférieures à n (2 à n-1) s'il y a des diviseurs de n
        if n % i == 0:
            pr = False
    return pr

def premier_plus_proche(n):                                           #Cette fonction trouve le nombre premier sépérieur ou égal à n le plus proche
    proche = False
    i = n
    while proche == False :
        if est_premier(i) == True:                                    #Si i est permier, la boucle se ferme et la fonction retourne i
            proche = True
            return i
        else:
            i = i + 1                                                 #Sinon on ajoute 1 à i tant que i n'est pas premier

def epreuve_math_premier():
    n = random.randint(10, 20)
    print("Epreuve de Mathématiques : trouver le nombre premier supérieur ou égal le plus proche de", n)
    joueur = int(input())
    print("Votre réponse :", joueur)
    reponse = premier_plus_proche(n)                                  #Le programme utilise la fonction premier_plus_proche() pour n
    if reponse == joueur :                                            #Ensuite, il compare la réponse du joueur à la bonne réponse
        print("Correct ! Vous gagnez une clé.")
        return True
    else:
        print("Dommage, mauvaise réponse.")
        return False

def epreuve_roulette_mathematique():                                  #Ce programme génère un calcul aléatoire et demande au joueur de toruver le résultat
    nb1 = random.randint(1, 20)
    nb2 = random.randint(1, 20)
    nb3 = random.randint(1, 20)
    nb4 = random.randint(1, 20)
    nb5 = random.randint(1, 20)
    nombres = [nb1, nb2, nb3, nb4, nb5]
    print("Nombres sur la roulette :", nombres)
    operation = ("addition", "soustraction", "multiplication")
    o = random.choice(operation)
    if o == "addition":
        print("Calculez le résultat en combinant ces nombres avec une addition")
        joueur = int(input())
        print("Votre réponse :", joueur)
        reponse = nb1 + nb2 + nb3 + nb4 + nb5
    if o == "soustraction":
        print("Calculez le résultat en combinant ces nombres avec une soustraction")
        joueur = int(input())
        print("Votre réponse :", joueur)
        reponse = nb1 - nb2 - nb3 - nb4 - nb5
    if o == "multiplication":
        print("Calculez le résultat en combinant ces nombres avec une multiplication")
        joueur = int(input())
        print("Votre réponse :", joueur)
        reponse = nb1 * nb2 * nb3 * nb4 * nb5
    if joueur == reponse :
        print("Bonne réponse ! Vous avez gagné une clé.")
        return True
    else:
        print("Dommage, mauvaise réponse.")
        return False

def epreuve_math():
    epreuves = (epreuve_math_factorielle, epreuve_math_premier, epreuve_roulette_mathematique)
    epreuve = random.choice(epreuves)
    epreuve()
    return epreuve

print(epreuve_math())












