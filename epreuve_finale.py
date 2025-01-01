import json
import random

def salle_De_Tresor():
    with open('./data/indicesSalle.json','r',encoding='utf-8') as f:
        jeu_tv = json.load(f)
    d = {}
    annee = []
    emission = []
    for a in jeu_tv["Fort Boyard"].keys():
        annee.append(a)
    annee = random.choice(annee)
    for e in jeu_tv["Fort Boyard"][annee].keys():
        emission.append(e)
    emission = random.choice(emission)
    indices = jeu_tv["Fort Boyard"][annee][emission]["Indices"]
    mot_code = jeu_tv["Fort Boyard"][annee][emission]["MOT-CODE"]
    print("Voici les trois premiers indices :", indices[0],",",indices[1],",",indices[2])
    essais = 3
    reponse_correcte = False
    i = 2
    while essais > 0 and reponse_correcte == False:
        print("Saisissez une réponse :")
        reponse = input()
        reponse_min = reponse.lower()
        mot_code_min = mot_code.lower()
        if reponse == mot_code or reponse_min == mot_code or reponse == mot_code_min or reponse_min == mot_code_min:
            print("Félicitation, vous avez trouvé le bon code !")
            reponse_correcte = True
        else:
            essais = essais - 1
            i = i + 1
            if essais > 1:
                print("Il ne vous reste plus que", essais,"essais.")
                print("Voici un indice supplémentaire :",indices[i])
            if essais == 1:
                print("Il ne vous reste plus que", essais, "essai.")
                print("Voici un indice supplémentaire :", indices[i])
            if essais == 0:
                print("Dommage, vous avez perdu l'épreuve finale. Le bon code était", mot_code)

salle_De_Tresor()