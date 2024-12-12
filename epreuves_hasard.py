from random import*

def bonneteau():
    Liste = ['A','B','C']
    BonneLettre = str()
    Choix = str()
    print("Bienvenue sur le jeu Bonneteau !\nLes règles de ce jeu sont : \nLe joueur doit deviner sous quel bonneteau (A, B ou C) se cache la clé. Il dispose de deux essais pour le trouver. À chaque essai, la clé est placée aléatoirement sous l'un des bonneteaux.")
    print("\nLes bonneteaux disponibles sont : le A, le B et le C")
    for i in range(2):
        BonneLettre = choice(Liste)
        print("Il vous reste :",i+1,"tentatives !")
        print("Saississez un bonneteau entre le A, le B et le C : ")
        Choix =