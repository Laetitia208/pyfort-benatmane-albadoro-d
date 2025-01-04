## **1. Présentation générale**

   - **Titre du projet** : Fort Boyard Simulator
   - **Contributeurs** : Nicolas ALBADORO (épreuve hasard, fonctions utiles, main), Laetitia BENATMANE (épreuve mathématique, épreuve logique, énigme père fouras, épreuve finale)
   - **Description** : ce projet est un simulateur de la célèbre émission Fort Boyard. L'objectif est de créer une équipe pour passer des épreuves et récolter trois clés.
                       Une fois les trois clés récoltées, les joueurs auront accès à l'épreuve finale pour tenter de gagner le jeu.
   - **Fonctionnalités principales** : les différentes épreuves tout le long du jeu (mathématiques, hasard, logique, énigmes, épreuve finale),
                                       la fonctions main et les fonctions utiles qui permettent le bon déroulement du jeu.
   - **Technologies utilisées** : le language de programmation utilisé est le Python. Les bibliothèques utilisées sont "random", "time", "re" et "math". Les outils utilisés sont PyCharm, Git et GitHub.
   - **Installation** : copiez le lien suivant : https://github.com/Laetitia208/pyfort-benatmane-albadoro-d.git et entrez le dans un navigateur. Vous aurez accès à tous les fichiers via GitHub. Pour y accéder via PyCharm, il faut d'abord avoir installé Git, posséder un compte GitHub et installer PyCharm. Après avoir suivi toutes ces instructions, copiez le lien puis allez sur PyCharm et entrez le dans "Clone repostory". Et enfin, télécharger le dossier Fort Boyard Simulator sur votre appareil. **Attention ! Ne déplacez pas les sous dossier et fichiers de leur emplacement initial !**
   - **Utilisation** : pour utiliser l'application, ouvrez le fichier main.py dans PyCharm et lancez le programme. La fonction jeu() sera automatiquement lancée. Faites attention à bien lancer le fichier main.py et pas un autre fichier. Vous pouvez également tester d'autres fonction dans d'autres fichiers comme la fonction enigme_pere_fouras() dans le fichier enigme_pere_fouras.py. Durant le jeu, vous aurez l'occasion de saisir une réponse dans la console.

## **2. Documentation technique**

   - **Algorithme du jeu** :
   1) epreuves_mathématiques.py / Ce fichier comporte trois épreuves mathématiques, l'épreuve de la factorielle, l'épreuve du nombre premier le plus proche et l'épreuve de la roulette mathématique. Pour faire toutes ces épreuves, sept fonction ont été créées. 
   2) epreuves_hasard.py / Ce fichier comporte deux épreuves de hasard, le bonneteau ainsi que le lancé de dés. Pour créer ces deux épreuves, trois fonctions ont été faites.
   3) epreuves_logiques.py / Ce fichier comporte une épreuve de logique, le jeu de la Bataille Navale. Pour faire l'épreuve logique, dix fonctions ont été céées.
   4) enigme_pere_fouras.py / Ce fichier comporte une épreuve, il s'agit de la célèbre énigme du Père Fouras. Pour faire cette épreuve, trois fonctions ont été nécessaires.
   5) epreuve_finale.py / Ce fichier comporte une épreuve, épreuve finale dans la salle de trésor. Elle consiste à trouver un mot à l'aide d'indices. Pour faire cette épreuve, une seule fonction a été nécessaire.
   6) fonctions_utiles.py / Ce fichier comporte plusieurs fonction qui sont nécessaires au bon déroulement du jeu. Il y a quatre fonctions.
   7) main.py / Ce fichier comporte une seule fonction qui permet de faire tourner complètement le jeu.
   8) enigmesPF.json / Ce fichier .json comporte toutes les énigmes de l'émission Fort Boyard
   9) indicesSalle.json / Ce fichier .json comporte tous les indices pour trouver le mot-clé de l'épreuve finale 
   - **Détail des fonctions implémentées** :
   1) factorielle(n) / Trouve la factorielle d'un nombre entier n pris en paramètre
   2) epreuve_math_factorielle() / Lance l'épreuve de la fatorielle 
   3) est_premier(n) / Retourne un booléen en fontion de si le nombre n pris en paramètre est premier ou non
   4) premier_plus_proche(n) / Trouve le nombre premier supérieur ou égal au paramètre n (nombre entier) le plus proche
   5) epreuve_math_premier() / Lance l'épreuve du nombre premier
   6) epreuve_roulette_mathematique() / Lance l'épreuve de la roulette mathématique. Elle propose un calcul aléatoire au joueur
   7) epreuve_math() / Choisi une épreuve mathématique au hasard parmi les trois précédentes et l'exécute
   8) bonneteau() / Lance l'épreuve du bonneteau. Le joueur doit trouver où se cache la clé parmi trois bonneteau
   9) jeu_lance_des() / Lance l'épreuve du lancé de dés. Le but du jeu est d'obtenir un 6 en premier
   10) epreuve_hasard() / Choisi une épreuve de hasard aléatoirement parmi les précédentes
   11) suiv(indice) / Prend en paramètre le numéro du joueur et retoune le numéro de l'autre joueur
   12) grille_vide() / Crée un tableau 2D 3x3 rempli d'espaces " "
   13) affiche_grille(grille,message) / Affiche le message pris en paramètre puis fais un affichage spécial de la grille prise en paramètre (tableau 2D)
   14) demande_position() / Demande au joueur une position sous la forme de deux chiffres compris entre 1 et 3 (ligne,colonne) et retourne une liste qui comprend ces deux chiffres
   15) init() / Initialise la grille du joueur, demande la position de ses bateaux et fais un affichage spécial
   16) tour(joueur, grille_tirs_joueur, grille_adversaire) / Fait le déroulement d'un tour, soit du joueur, soit du maître du jeu. Elle prend en paramètre le numéro du joueur, sa grille de tirs et la grille de l'adversaire
   17) gagne(grille_tirs_joueur) / Renvoie un booléen en fonction de si la grille de tirs du joueur prise en paramètre est gagnante ou non 
   18) init_grille_maitre() / Initialise la grille du maître du jeu, la position des bateaux est choisie aléatoirement
   19) jeu_bataille_navale() / Fais tourner le jeu de la bataille navale
   20) epreuve_logique() / Retourne la fonction jeu_bataille_navale()
   21) charger_enigmes() / Charge les énigmes du fichier enigmesPF.json et les met dans un dictionnaire
   22) enigme_pere_fouras() / Fais tourner l'épreuve de l'énigme du Père Fouras
   23) epreuve_pere_fouras() / Retourne la fonction enigme_pere_fouras()
   24) salle_De_Tresor() / Fais tourner l'épreuve finale de la salle de trésor
   25) introduction() / Affiche les consignes du jeu
   26) composer_equipe() / Compose l'équipe avec tous les joueurs, leur profession et leur rôle
   27) menu_epreuves() / Propose les types d'épreuves disponibles et le joueur en choisi un. Une épreuve sera choisie au hasard parmi le type choisi. Par exemple, le type choisi est l'épreuve mathématique et la roulette mathématique est l'épreuve choisie aléatoirement
   28) choisir_joueur(equipe) / Un joueur parmi l'équipe est choisi pour faire l'épreuve
   29) jeu() / Lance le jeu Fort Boyard Simulator
   - **Gestion des Entrées et Erreurs** : pour gérer les intervalles, il y a une saisie sécurisée afin de ne pas avoir d'erreur dans le programme. Les bugs les plus rencontrés sont "TypeError: 'NoneType' object is not subscriptable", "KeyError" et "AttributeError: 'str' object has no attribute 'append'"

## **3. Journal de bord**

   - **Chronologie du Projet** :
