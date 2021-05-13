from random import randint
import sys
sys.path.append('../')
from tiles.tiles_acces import is_room_empty, set_value, get_value

# -------- Fonctions de la partie 1 --------

def get_nb_empty_rooms(plateau):
    """
    Met à jour le dictionnaire plateau avec le nombre de case(s) libre(s) du plateau
    Renvoie le nombre de case(s) libre(s)

    :Exemple:
    p = {'n': 4, 'nb_cases_libres': 6, 'tiles': [6, 2, 3, 2, 0, 2, 6, 2, 0, 2, 2, 0, 1, 0, 0, 0]}

    p['nb_cases_libres'] = 5 # pour le test
    n = get_nb_empty_rooms(p) # n vaut 6
    print(p['nb_cases_libres']) # affiche 6
    """
    plateau['nb_cases_libres'] = plateau['tiles'].count(0)  # Met à jour le dictionnaire plateau avec le nombre de
    # case(s) libre(s) du plateau

    return plateau['tiles'].count(0)  # Renvoie le nombre de case(s) libre(s)

# -------- Fonctions de la partie 2 --------

def get_next_alea_tiles(plateau, mode):
    """ Retoune une ou deux tuile(s) dont la position (lig, col) est tirée
        aléatoirement et correspond à un emplacement libre du plateau

        plateau : dictionnaire contenant le plateau du jeu
        mode : valeurs possibles pour ce paramètre et significations

        *************************************************************************************
        *                                        mode                                       *
        *************************************************************************************
        *                  'init' :               *               'encours' :               *
        *************************************************************************************
        * Un dictionnaire contenant deux tuiles   * Un dictionnaire contenant une tuile, de *
        * de valeur 1 et 2 est retourné.          * valeur comprise entre 1 et 3 est        *
        * La position de chaque tuile est tirée   * retournée. La position de la tuile est  *
        * aléatoirement et correspond à un        * tirée aléatoirement et correspond à un  *
        * emplacement libre du plateau ; ce mode  * emplacement libre du plateau ; ce mode  *
        * est utilisé lors de l'initialisation    * est utilisé en cours de jeu.            *
        * du jeu.                                 *                                         *
        *************************************************************************************

        Voir l'exemple pour connaître la structure du dictionnaire.

        :Exemple:
        p = init_play()
        tiles = get_next_alea_tiles(p,'init')
        print(tiles)

        {'mode': 'init',
            '0': {'val': 2, 'lig': 0, 'col': 1},
            '1': {'val': 1, 'lig': 3, 'col': 3},
            'check': True}

        tiles=get_next_alea_tiles(p,'encours')
        print(tiles)

        {'mode': 'encours',
            '0': {'val': 3, 'lig': 0, 'col': 2},
            'check': True}

        Remarques :
            * Les positions et valeurs de tuiles pourront être différentes
                pour vos tests car elles sont tirées aléatoirement.
            * La clef 'check' a une valeur True si la partie n'est pas terminée,
                False sinon.
    """
    if mode == 'init':
        tile_0 = randint(0, plateau['n'] ** 2 - 1)
        tile_1 = randint(0, plateau['n'] ** 2 - 1)
        while not is_room_empty(plateau, tile_0 // plateau['n'], tile_0 % plateau['n']):
            tile_0 = randint(0, plateau['n'] ** 2 - 1)
        while not is_room_empty(plateau, tile_1 // plateau['n'], tile_1 % plateau['n']) or tile_1 == tile_0:
            tile_1 = randint(0, plateau['n'] ** 2 - 1)
        return {'mode': mode,
                '0': {'val': 2, 'lig': tile_0 // plateau['n'], 'col': tile_0 % plateau['n']},
                '1': {'val': 1, 'lig': tile_1 // plateau['n'], 'col': tile_1 % plateau['n']},
                'check': plateau['nb_cases_libres'] - 2 > 0}
    elif mode == 'encours':
        tile_0 = randint(0, plateau['n'] ** 2 - 1)
        while not is_room_empty(plateau, tile_0 // plateau['n'], tile_0 % plateau['n']):
            tile_0 = randint(0, plateau['n'] ** 2 - 1)
        return {'mode': mode,
                '0': {'val': randint(1, 3), 'lig': tile_0 // plateau['n'], 'col': tile_0 % plateau['n']},
                'check': plateau['nb_cases_libres'] - 1 > 0}
    else:
        assert mode in ['init', 'encours'], 'Erreur : fonction get_next_alea_tiles().'


def put_next_tiles(plateau, tiles):
    """
    Permet de placer une ou deux tuiles dans le plateau.
    plateau : dictionnaire contenant le plateau d'un jeu
    tiles : dictionnaire sous la forme de celui renvoyé par la fonction get_next_alea_tiles().
    """
    while tiles['mode'] == 'encours' and not is_room_empty(plateau, tiles['0']['lig'], tiles['0']['col']):
        tile_0 = randint(0, plateau['n'] ** 2 - 1)
        tiles['0']['lig'] = tile_0 // plateau['n']
        tiles['0']['col'] = tile_0 % plateau['n']
    set_value(plateau, tiles['0']['lig'], tiles['0']['col'], tiles['0']['val'])
    if tiles['mode'] == 'init':
        set_value(plateau, tiles['1']['lig'], tiles['1']['col'], tiles['1']['val'])
    get_nb_empty_rooms(plateau)  # Ne pas oublier d'actualiser nb_cases_libres dans plateau.


def line_pack(plateau, lig, debut, sens):
    """
    Tasse les tuiles d'une ligne dans un sens donné
    plateau : dictionnaire contenant le plateau d'un jeu
    lig : indice de la ligne à "tasser"
    debut : indice à partir duquel se fait le "tassement"
    sens : sens du "tassement", 1 vers la gauche, 0 vers la droite

    :Exemple:
    p = {
            'n': 4,
            'nb_cases_libres': 10,
            'tiles': [0, 2, 0, 0, 0, 2, 3, 3, 0, 2, 2, 0, 0, 0, 0, 0]
        }

    line_pack(p, 1, 0, 1)
    print(p['tiles']) # affiche [0, 2, 0, 0, 2, 3, 3, 0, 0, 2, 2, 0, 0, 0, 0, 0]

    line_pack(p, 1, 2, 1)
    print(p['tiles']) # affiche [0, 2, 0, 0, 2, 3, 0, 0, 0, 2, 2, 0, 0, 0, 0, 0]

    line_pack(p, 1, 3, 0)
    print(p['tiles']) # affiche [0, 2, 0, 0, 0, 2, 3, 0, 0, 2, 2, 0, 0, 0, 0, 0]

    line_pack(p, 1, 2, 0)
    print(p['tiles']) # affiche [0, 2, 0, 0, 0, 0, 2, 0, 0, 2, 2, 0, 0, 0, 0, 0]
    """
    if sens == 0:
        while debut > 0:
            plateau['tiles'][lig * plateau['n'] + debut] = plateau['tiles'][lig * plateau['n'] + debut - 1]
            debut -= 1
        plateau['tiles'][lig * plateau['n'] + debut] = 0
    if sens == 1:
        while debut < plateau['n'] - 1:
            plateau['tiles'][lig * plateau['n'] + debut] = plateau['tiles'][lig * plateau['n'] + debut + 1]
            debut += 1
        plateau['tiles'][lig * plateau['n'] + debut] = 0


def column_pack(plateau, col, debut, sens):
    """
    Tasse les tuiles d'une colonne dans un sens donné
    plateau : dictionnaire contenant le plateau d'un jeu
    col : indice de la ligne à "tasser"
    debut : indice à partir duquel se fait le "tassement"
    sens : sens du "tassement", 1 vers le haut, 0 vers le bas
    """
    if sens == 0:
        while debut > 0:
            plateau['tiles'][debut * plateau['n'] + col] = plateau['tiles'][(debut - 1) * plateau['n'] + col]
            debut -= 1
        plateau['tiles'][debut * plateau['n'] + col] = 0
    if sens == 1:
        while debut < plateau['n'] - 1:
            plateau['tiles'][debut * plateau['n'] + col] = plateau['tiles'][(debut + 1) * plateau['n'] + col]
            debut += 1
        plateau['tiles'][debut * plateau['n'] + col] = 0


def line_move(plateau, lig, sens):
    """
    Déplacement des tuiles d'une ligne donnée dans un sens donné en appliquant les règles du jeu Threes.
    plateau : dictionnaire contenant le plateau d'un jeu
    lig : indice de la ligne pour laquelle il faut déplacer les tuiles
    sens : sens du déplacement des tuiles, 1 vers la gauche, 0 vers la droite

    :Exemple:
    p = {
            'n': 4,
            'nb_cases_libres': 10,
            'tiles': [0, 2, 0, 0, 0, 2, 3, 3, 0, 2, 2, 0, 0, 0, 0, 0]
        }

    line_move(p, 1, 1)
    print(p['tiles']) # affiche [0, 2, 0, 0, 2, 3, 3, 0, 0, 2, 2, 0, 0, 0, 0, 0]

    line_move(p, 1, 1)
    print(p['tiles']) # affiche [0, 2, 0, 0, 2, 6, 0, 0, 0, 2, 2, 0, 0, 0, 0, 0] Les 3 se tassent pour donner un 6 dans le sens du tassement

    line_move(p, 2, 0)
    print(p['tiles']) # affiche [0, 2, 0, 0, 2, 6, 0, 0, 0, 0, 2, 2, 0, 0, 0, 0]

    line_move(p, 2, 0)
    print(p['tiles']) # affiche [0, 2, 0, 0, 2, 6, 0, 0, 0, 0, 2, 2, 0, 0, 0, 0] Aucun changement car les 2 ne peuvent se tasser qu'avec les 1
    """
    if sens == 0:
        continuer = True
        n = plateau['n'] - 1
        while continuer and n > 0:
            if get_value(plateau, lig, n) == 0:
                line_pack(plateau, lig, n, sens)
                continuer = False
            elif (get_value(plateau, lig, n) in [1, 2] and get_value(plateau, lig, n - 1) + get_value(plateau, lig, n) == 3) or (get_value(plateau, lig, n) == get_value(plateau, lig, n - 1) and get_value(plateau, lig, n) % 3 == 0):
                set_value(plateau, lig, n, get_value(plateau, lig, n) + get_value(plateau, lig, n - 1))
                line_pack(plateau, lig, n - 1, sens)
                continuer = False
            n -= 1
    elif sens == 1:
        continuer = True
        n = 0
        while continuer and n < plateau['n'] - 1:
            if get_value(plateau, lig, n) == 0:
                line_pack(plateau, lig, n, sens)
                continuer = False
            elif (get_value(plateau, lig, n) in [1, 2] and get_value(plateau, lig, n + 1) + get_value(plateau, lig, n) == 3) or (get_value(plateau, lig, n) == get_value(plateau, lig, n + 1) and get_value(plateau, lig, n) % 3 == 0):
                set_value(plateau, lig, n, get_value(plateau, lig, n) + get_value(plateau, lig, n + 1))
                line_pack(plateau, lig, n + 1, sens)
                continuer = False
            n += 1


def column_move(plateau, col, sens):
    """
    Déplacement des tuiles d'une colonne donnée dans un sens donné en appliquant les règles du jeu Threes.
    plateau : dictionnaire contenant le plateau d'un jeu
    col : indice de la colonne pour laquelle il faut déplacer les tuiles
    sens : sens du déplacement des tuiles, 1 vers le haut, 0 vers le bas
    """
    if sens == 0:
        continuer = True
        n = plateau['n'] - 1
        while continuer and n > 0:
            if get_value(plateau, n, col) == 0:
                column_pack(plateau, col, n, sens)
                continuer = False
            elif (get_value(plateau, n, col) in [1, 2] and get_value(plateau, n - 1, col) + get_value(plateau, n, col) == 3) or (get_value(plateau, n, col) == get_value(plateau, n - 1, col) and get_value(plateau, n, col) % 3 == 0):
                set_value(plateau, n, col, get_value(plateau, n, col) + get_value(plateau, n - 1, col))
                column_pack(plateau, col, n - 1, sens)
                continuer = False
            n -= 1
    elif sens == 1:
        continuer = True
        n = 0
        while continuer and n < plateau['n'] - 1:
            if get_value(plateau, n, col) == 0:
                column_pack(plateau, col, n, sens)
                continuer = False
            elif (get_value(plateau, n, col) in [1, 2] and get_value(plateau, n + 1, col) + get_value(plateau, n, col) == 3) or (get_value(plateau, n, col) == get_value(plateau, n + 1, col) and get_value(plateau, n, col) % 3 == 0):
                set_value(plateau, n, col, get_value(plateau, n, col) + get_value(plateau, n + 1, col))
                column_pack(plateau, col, n + 1, sens)
                continuer = False
            n += 1


def lines_move(plateau, sens):
    """
    Déplace les tuiles de toutes les lignes du plateau dans un sens donné en appliquant les règles du jeu Threes.
    plateau : dictionnaire contenant le plateau d'un jeu
    sens : sens du déplacement des tuiles, 1 vers la gauche, 0 vers la droite
    """
    for i in range(0, plateau['n']):
        line_move(plateau, i, sens)


def columns_move(plateau, sens):
    """
    Déplace les tuiles de toutes les colonnes du plateau dans un sens donné en appliquant les règles du jeu Threes.
    plateau : dictionnaire contenant le plateau d'un jeu
    sens : sens du déplacement des tuiles, 1 vers le haut, 0 vers le bas
    """
    for i in range(0, plateau['n']):
        column_move(plateau, i, sens)


def play_move(plateau, sens):
    """
    Déplace les tuiles du plateau dans un sens donné en appliquant les règles du jeu Threes.
    plateau : dictionnaire contenant le plateau d'un jeu
    sens : sens du déplacement des tuiles
            'b' : bas
            'h' : haut
            'd' : droite
            'g' : gauche
    """
    if sens == 'b' or sens == 's':
        columns_move(plateau, 0)
    elif sens == 'h' or sens == 'z':
        columns_move(plateau, 1)
    elif sens == 'd':
        lines_move(plateau, 0)
    elif sens == 'g' or sens == 'q':
        lines_move(plateau, 1)