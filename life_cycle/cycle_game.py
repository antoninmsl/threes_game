from json import *
import sys

sys.path.append('../')
from tiles.tiles_moves import get_nb_empty_rooms, get_next_alea_tiles, put_next_tiles, \
    play_move  # Import de get_nb_empty_rooms() pour la fonction is_game_over().
from ui.play_display import full_display
from ui.user_entries import get_user_move


# -------- Fonctions de la partie 1 --------

def init_play():
    """
    Retourne un plateau correspondant à une nouvelle partie.
    Une nouvelle partie est un dictionnaire avec les clefs et valeurs suivantes :
    - 'n' : vaut 4
    - 'nb_cases_libres' : 16 au départ (n * n)
    - 'tiles' : tableau de n*n cases initialisées à 0

    :Exemple:
    p = init_play() retourne le dictionnaire :
        {
            'n' : 4,
            'nb_cases_libres' : 16,
            'tiles' : [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        }
    """

    n = 4  # Nombre de tuiles sur une ligne (4)

    return {'n': n, 'nb_cases_libres': n * n, 'tiles': n * n * [0]}  # Retourne le plateau de la nouvelle partie.


def is_game_over(plateau):
    """
    Retourne True si la partie est terminée, False sinon.

    :Exemple:
    p1 = {'n': 4, 'nb_cases_libres': 6, 'tiles': [6, 2, 3, 2, 0, 2, 6, 2, 0, 2, 2, 0, 1, 0, 0, 0]}
    game_over = is_game_over(p1) # game_over vaut False

    p2 = {'n': 4, 'nb_cases_libres': 0, 'tiles': [6, 2, 3, 2, 12, 2, 6, 2, 6, 2, 2, 12, 1, 6, 3, 1]}
    game_over = is_game_over(p2) # game_over vaut True
    """
    return get_nb_empty_rooms(plateau) == 0  # Retourne True si la partie est terminée c'est à dire lorsqu'il n'y a
    # plus de cases libres, False sinon.


def get_score(plateau):
    """
    Retourne le score du plateau

    :Exemple:
    p = {'n': 4, 'nb_cases_libres': 0, 'tiles': [6, 2, 3, 2, 12, 2, 6, 2, 6, 2, 2, 12, 1, 6, 3, 1]}

    score = get_score(p) # score vaut 68
    """
    score = 0
    for n in plateau['tiles']:  # Boucle qui parcours toutes les cases du tableau plateau['tiles'].
        score += n  # Ajoute chaque valeur de la case du tableau à score.
    return score  # Retourne le score correspondant à la somme des valeurs des tuiles.


# -------- Fonctions de la partie 3 ---------

def create_new_play():
    """
    :return: dictionnaire d'une nouvelle partie ayant pour clefs:
        - 'plateau': (dictionnaire) mémorisant le plateau de jeu.
        - 'next_tile': (dictionnaire) mémorisant la prochaine tuile à placer. Au départ ce dictionnaire est vide.
        - 'score': (entier) le score courant du joueur.
    """
    plateau = init_play()
    next_tiles = get_next_alea_tiles(plateau, 'init')
    put_next_tiles(plateau, next_tiles)
    return {'plateau': plateau,
            'next_tile': {},
            'score': get_score(plateau)}


def cycle_play(partie):
    """
    Permet de jouer à Threes
    :param partie: Partie de jeu en cours ou None sinon
    :return: True si la partie est terminée, False si menu demandé

        Séquencement des actions pour cette fonction :
            1 - afficher le plateau de jeu,
            2 - affiche la prochaine tuile pour informer le joueur,
            3 - saisir le mouvement proposé par le joueur ; deux cas possibles :
                * jouer le coup du joueur courant, mettre à jour le score et revenir au point 1-
                * ou retourner False si menu demandé
            4 - si partie terminée, retourne True
    """
    if partie is None:
        partie = create_new_play()
    while not is_game_over(partie['plateau']):
        full_display(partie['plateau'])
        partie['next_tile'] = get_next_alea_tiles(partie['plateau'], 'encours')
        print('Tuile suivante : ', partie['next_tile']['0']['val'])
        user_move = get_user_move()
        if user_move == 'm':
            return False
        else:
            play_move(partie['plateau'], user_move)
            put_next_tiles(partie['plateau'], partie['next_tile'])
    print(full_display(partie['plateau']))
    return True


def save_game(partie):
    """ Sauvegarde une partie dans le fichier saved_game.json

    :Exemple:

    si partie contient
    {'plateau' : {
                  'n': 4,
                  'nb_cases_libres': 6,
                  'tiles': [6,2,3,2,0,2,1,2,6,2,0,0,0,6,1,1]
                  },
    'next_tile': {'mode': 'encours', 0: {'val': 3, 'lig': 0, 'col':1}, 'check': True},
    'score': 34}

    le fichier saved_game.json doit contenir
    {'plateau' : {'n': 4, 'nb_cases_libres': 6, 'tiles': [6,2,3,2,0,2,1,2,6,2,0,0,0,6,1,1]},
    'next_tile': {'mode': 'encours', "0": {'val': 3, 'lig': 0, 'col':1}, 'check': True},
    'score': 34}

     """

    fichier = open("./saved_game.json", "w")
    fichier.write(dumps(partie))
    fichier.close()


def restore_game():
    """ Restaure et retourne une partie auvegardée dans le fichier "game_saved.json", ou retourne une nouvelle partie si aucune partie n'est pas sauvegardée

    :Exemple:
    Si un fichier saved_game.json existe et contient :
    {'plateau' : {'n': 4, 'nb_cases_libres': 6, 'tiles': [6,2,3,2,0,2,1,2,6,2,0,0,0,6,1,1]},
    'next_tile': {'mode': 'encours', "0": {'val': 3, 'lig': 0, 'col':1}, 'check': True},
    'score': 34}

    p = restore_game()
    print(p)
    Affichage :
    {'plateau' : {
                  'n': 4,
                  'nb_cases_libres': 6,
                  'tiles': [6,2,3,2,0,2,1,2,6,2,0,0,0,6,1,1]
                  },
    'next_tile': {'mode': 'encours', "0": {'val': 3, 'lig': 0, 'col':1}, 'check': True},
    'score': 34}
    """

    fichier = open("./saved_game.json", 'a')
    fichier.close()

    fichier = open("./saved_game.json", 'r')
    strjson = fichier.read()
    fichier.close()

    partie_save = loads(strjson)
    if len(partie_save) != 3 or type(partie_save) != dict:
        return create_new_play()
    return partie_save


