import json

def charger_enigmes():
    with open('./data/enigmesPF.json','r',encoding='utf-8') as f:
        enigmes = json.load(f)
    d = {}
    for enigme in enigmes:
        d[enigme['question']] = enigme['reponse']
    return d

import random

def enigme_pere_fouras():
    nb_essais = 3
    liste_enigmes = (charger_enigmes())
    enigme_choisie,rep = random.choice(list(liste_enigmes.items()))
    print(enigme_choisie)
    while nb_essais > 0:
        print("Saisissez une réponse :")
        reponse = input()
        reponse_min = reponse.lower()
        rep_min = rep.lower()
        if reponse_min == rep or reponse == rep or reponse_min == rep_min or reponse == rep_min:
            print("Félicitation, votre réponse esr correcte ! Vous avez gagné une clé")
            return True
        else:
            nb_essais -= 1
            if nb_essais > 1:
                print("Malheureusement, votre réponse est incorrecte. Il vous reste",nb_essais,"essais.")
            if nb_essais == 1:
                print("Malheureusement, votre réponse est incorrecte. Il vous reste", nb_essais, "essai.")
            if nb_essais == 0:
                print("Dommage, vous avez échoué à cette épreuve. La réponse était :",rep)
                return False

"""enigme_pere_fouras()"""
