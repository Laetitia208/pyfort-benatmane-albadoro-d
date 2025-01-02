from fonctions_utiles import*


def jeu():
    introduction()
    equipe = composer_equipe()
    cles_obtenus = {joueur['nom']: 0 for joueur in equipe}
    nombre_cles = 0
    while nombre_cles < 3:
        print("\nVous avez : ",nombre_cles,"clés.")
        type_epreuve = menu_epreuves()
        choix_joueur = choisir_joueur(equipe)
        type_epreuve()
        if type_epreuve == True:
            nombre_cles = nombre_cles + 1
        for joueur in equipe:  #Calcule la somme des clés
            nombre_cles = nombre_cles + equipe[joueur['nom']]




jeux = jeu()
jeux()