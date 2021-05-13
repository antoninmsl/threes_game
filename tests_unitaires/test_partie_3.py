import sys
sys.path.append('../')
from life_cycle.cycle_game import create_new_play, save_game, restore_game
from ui.user_entries import get_user_move, get_user_menu
from json import *


def test_create_new_play():
    """ Fonction de test de create_new_play()."""
    test = create_new_play()
    assert test['next_tile'] == {}
    assert test['score'] == 3
    print('Fonction create_new_play() : OK')


def test_get_user_move():
    """ Fonction de test de get_user_move() impossible car elle utilise input()."""
    print('Ceci ne teste rien, donc get_user_move() marche très bien d\'après nos tests.')

def test_get_user_menu():
    """ Fonction de test de get_user_move(). """

    print("Entrez 'N' :")
    test = get_user_menu(None)
    assert test == 'N', "Erreur de la fonction get_user_move()."

    print("Entrez 'n' :")
    test = get_user_menu(None)
    assert test == 'N', "Erreur de la fonction get_user_move()."

    print("Entrez '5' puis 'x' puis 'B' puis 'l' :")
    test = get_user_menu(None)
    assert test == 'L', "Erreur de la fonction get_user_move()."

    print("Entrez 'c' puis 'C' puis 'q' :")
    test = get_user_menu(None)
    assert test == 'Q', "Erreur de la fonction get_user_move()."

    print("Entrez 's' puis 'S' puis 'L' :")
    test = get_user_menu(None)
    assert test == 'L', "Erreur de la fonction get_user_move()."

    print("Entrez 'N' :")
    test = get_user_menu("partie")
    assert test == 'N', "Erreur de la fonction get_user_move()."

    print("Entrez 'n' :")
    test = get_user_menu("partie")
    assert test == 'N', "Erreur de la fonction get_user_move()."

    print("Entrez '5' puis 'x' puis 'B' puis 'l' :")
    test = get_user_menu("partie")
    assert test == 'L', "Erreur de la fonction get_user_move()."

    print("Entrez 'c' :")
    test = get_user_menu("partie")
    assert test == 'C', "Erreur de la fonction get_user_move()."

    print("Entrez 's' :")
    test = get_user_menu("partie")
    assert test == 'S', "Erreur de la fonction get_user_move()."

    print("Fonction get_user_menu() : OK")

def test_save_game():
    """ Fonction de test de la fonction save_game()."""

    partie = {'plateau' : {'n': 4, 'nb_cases_libres': 6, 'tiles': [6,2,3,2,0,2,1,2,6,2,0,0,0,6,1,1]},
    'next_tile': {'mode': 'encours', 0: {'val': 3, 'lig': 0, 'col':1}, 'check': True},
    'score': 34}

    save_game(partie)
    fichier = open("./saved_game.json", 'r')
    strjson = fichier.read()
    fichier.close()
    partie_save = loads(strjson)

    assert partie_save == {'plateau' : {'n': 4, 'nb_cases_libres': 6, 'tiles': [6,2,3,2,0,2,1,2,6,2,0,0,0,6,1,1]},
    'next_tile': {'mode': 'encours', "0": {'val': 3, 'lig': 0, 'col':1}, 'check': True},
    'score': 34}

    partie = "Message de test"

    save_game(partie)
    fichier = open("./saved_game.json", 'r')
    strjson = fichier.read()
    fichier.close()
    partie_save = loads(strjson)

    assert partie_save == "Message de test"

    print("Test de la fonction save_game() : OK")

def test_restore_game() :
    """Fonction de test de la fonction restore_game()."""

    partie = {'plateau' : {'n': 4, 'nb_cases_libres': 6, 'tiles': [6,2,3,2,0,2,1,2,6,2,0,0,0,6,1,1]},
    'next_tile': {'mode': 'encours', "0": {'val': 3, 'lig': 0, 'col':1}, 'check': True},
    'score': 34}

    fichier = open("./saved_game.json", "w")
    fichier.write(dumps(partie))
    fichier.close()

    p = restore_game()
    assert p == {'plateau' : {
                  'n': 4,
                  'nb_cases_libres': 6,
                  'tiles': [6,2,3,2,0,2,1,2,6,2,0,0,0,6,1,1]
                  },
    'next_tile': {'mode': 'encours', "0": {'val': 3, 'lig': 0, 'col':1}, 'check': True},
    'score': 34}

    partie = "Farida (mot choisi au hasard)"

    fichier = open("./saved_game.json", "w")
    fichier.write(dumps(partie))
    fichier.close()

    p = restore_game()
    assert len(p) == 3 and p['plateau']['nb_cases_libres']== 14 and p['score']== 3

    print("Test de la fonction restore_game() : OK")






test_create_new_play()
test_get_user_move(n)
test_get_user_menu()
test_save_game()
test_restore_game()


