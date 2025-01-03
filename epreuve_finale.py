#Fort Boyard Simulator
#Laetitia BENATMANE, Nicolas ALBADORO
#Ce fichier comporte l'épreuve finale et permet de la lancer

import json
import random

def salle_De_Tresor():                   #Cette fonction effectue le déroulement de l'épreuve finale
    with open('./data/indicesSalle.json','r',encoding='utf-8') as f:
        jeu_tv = json.load(f)            #Elle ouvre et charge le fichier indicesSalle.json
    d = {}
    annee = []
    emission = []
    for a in jeu_tv["Fort Boyard"].keys(): #Cette boucle parcours les années
        annee.append(a)                  #Elles sont ensuite ajoutées au tableau annee
    annee = random.choice(annee)         #Et une année est choisie au hasard
    for e in jeu_tv["Fort Boyard"][annee].keys(): #Cette boucle parcours toutes les émissions de l'année annee choisie
        emission.append(e)               #Elles sont ensuite ajoutées dans le tableau emission
    emission = random.choice(emission)   #Et une émission est choisie au hasard
    indices = jeu_tv["Fort Boyard"][annee][emission]["Indices"]  #Les indices de l'émission de l'année choisie sont extraits
    mot_code = jeu_tv["Fort Boyard"][annee][emission]["MOT-CODE"]  #Ainsi que le mot_code
    print("Voici les trois premiers indices :", indices[0],",",indices[1],",",indices[2]) #Les trois premiers indices d'affichent
    essais = 3                           #Le joueur possède 3 essais pour trouver la bonne réponse
    reponse_correcte = False
    i = 2
    while essais > 0 and reponse_correcte == False: #Tant que le joueur n'a pas gagné et qu'il possède au moins 1 essai,
        print("Saisissez une réponse :")
        reponse = input()                #Le joueur saisi une réponse
        reponse_min = reponse.lower()    #Sa réponse est mise en minuscule
        mot_code_min = mot_code.lower()  #La bonne réponse est mise en minuscule
        if reponse == mot_code or reponse_min == mot_code or reponse == mot_code_min or reponse_min == mot_code_min:
            print("Félicitation, vous avez trouvé le bon code !")
            reponse_correcte = True      #Si le joueur a trouvé la bonne réponse, alors il a gagné et la boucle se ferme
        else:
            essais = essais - 1          #Sinon, il perd un essai
            i = i + 1
            if essais > 1:               #S'il reste au moins 1 essai, l'indice suivant s'affiche
                print("Il ne vous reste plus que", essais,"essais.")
                print("Voici un indice supplémentaire :",indices[i])
            if essais == 1:
                print("Il ne vous reste plus que", essais, "essai.")
                print("Voici un indice supplémentaire :", indices[i])
            if essais == 0:              #S'il ne reste plus d'essais, alors le joueur a perdu et la bonne réponse s'affiche
                print("Dommage, vous avez perdu l'épreuve finale. Le bon code était", mot_code)

"""salle_De_Tresor()"""