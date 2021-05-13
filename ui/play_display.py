from termcolor import *
import sys
sys.path.append("../")
from tiles.tiles_acces import get_value

# -------- Fonction de la partie 1 --------

def full_display(plateau):
    """
    Affichage en couleurs un plateau passé en paramètre.
    """
    line_separator = '  ' * (plateau['n'] + 1) + '     ' * plateau['n']  # Définition d'une chaine de caractères utilisée
    # pour afficher des lignes de séparations entre les lignes qui représentent les cases

    message = '\n'  # message est une chaine de caractères qui va être modifiée jusqu'à ce qu'elle contienne tout
    # l'affichage du plateau de jeu

    for i in range(0, plateau['n']*3):
        # On parcours le tableau ligne par ligne, ici la valeur 3 permet d'afficher des cases de 3 lignes de haut

        if i % 3 == 0:  # A chaque nouvelle ligne parcourue du plateau, on ajoute une ligne de séparation avant
            message += colored(line_separator, None, 'on_grey') + '\n'

        for j in range(0, plateau['n']):  # On parcours les lignes case par case
            message += colored('  ', None, 'on_grey')
            # A chaque nouvelle case parcourue du plateau, on ajoute une case de séparation avant

            val = get_value(plateau, i//3, j)  # On cherche la valeur de la case et on la garde en mémoire dans val

            if val == 0:
                # Si la valeur de la case est 0, on définie la couleur de la police en bleu
                # pour que la valeur ne soit pas visible sur la couleur de fond bleue que l'on définie aussi
                color = 'blue'
                on_color = 'on_blue'

            elif val == 1:
                # Si la valeur de la case est 1, on définie la couleur de la police en blanc et la couleur de fond bleue
                color = 'white'
                on_color = 'on_blue'

            elif val == 2:
                # Si la valeur de la case est 2, on définie la couleur de la police en blanc et la couleur de fond rouge
                color = 'white'
                on_color = 'on_red'

            else:
                # Sinon, on définie la couleur de la police en noir (None car c'est la couleur par défaut)
                # et la couleur de fond blanc
                color = None
                on_color = 'on_white'

            if i%3 == 1:  # Si la ligne est la deuxième ligne de la case, on ajoute la case en affichant la valeur
                message += colored(str.center(str(val), 5), color, on_color, attrs=['bold'])

            else:  # Sinon, on ajoute la case sans afficher la valeur
                message += colored('     ', None, on_color)

        message += colored('  ', None, 'on_grey') + '\n'
        # A chaque fin de ligne parcourue du plateau, on ajoute une case de séparation après

    message += colored(line_separator, None, 'on_grey') + '\n'  # On ajoute une ligne de séparation pour finir l'affichage
    print(message)  # On affiche le message (Le plateau mis en forme)
    return message  # On retourne le message (Le plateau mis en forme) pour les tests unitaires
