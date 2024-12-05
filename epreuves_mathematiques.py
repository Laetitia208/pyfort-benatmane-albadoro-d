from pydoc import importfile

def factorielle(n):
    f = 1
    if n == 0:
        return 1
    for i in range(1, n+1):
        f = f*i
    return f

import random

def epreuve_math_factorielle():
    n = random.randint(1, 10)
    print("Epreuve de Mathématiques : calculer la factorielle de", n)
    joueur = int(input())
    print("Votre réponse :", joueur)
    reponse = factorielle(n)
    if reponse == joueur :
        print("Correct ! Vous gagnez une clé.")
        return True
    else:
        return False

def est_premier(n):
    pr = True
    if n <= 1 :
        return False
    for i in range(2, n):
        if n % i == 0:
            pr = False
    return pr

def premier_plus_proche(n):
    proche = False
    i = n
    while proche == False :
        if est_premier(i) == True:
            proche = True
            return i
        else:
            i = i + 1

def epreuve_math_premier():
    n = random.randint(10, 20)
    print("Epreuve de Mathématiques : trouver le nombre premier le plus proche de", n)
    joueur = int(input())
    print("Votre réponse :", joueur)
    reponse = premier_plus_proche(n)
    if reponse == joueur :
        print("Correct ! Vous gagnez une clé.")
        return True
    else:
        return False

def epreuve_roulette_mathematique():
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
        return False

def epreuve_math():
    epreuves = ()













