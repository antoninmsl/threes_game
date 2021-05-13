import sys
sys.path.append('../')
from life_cycle.cycle_game import init_play, is_game_over, get_score
from tiles.tiles_acces import check_indice, check_room, get_value, set_value, is_room_empty
from tiles.tiles_moves import get_nb_empty_rooms
from ui.play_display import full_display


def test_init_play():
    """
    Fonction de test de init_play().
    """
    p = init_play()
    assert p == {'n': 4, 'nb_cases_libres': 16, 'tiles': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]}, 'Erreur : fonction init_play()'
    print('Fonction init_play() : OK')


def test_check_indice():
    """
    Fonction de test de check_indice().
    """
    p = init_play()

    assert check_indice(p, 0), 'Erreur : fonction check_indice()'
    assert not check_indice(p, 10), 'Erreur : fonction check_indice()'
    assert check_indice(p, 3), 'Erreur : fonction check_indice()'
    assert not check_indice(p, 4), 'Erreur : fonction check_indice()'
    assert not check_indice(p, -1), 'Erreur : fonction check_indice()'
    print('Fonction check_indice() : OK')


def test_check_room():
    """
    Fonction de test de check_room().
    """
    p = init_play()

    assert check_room(p, 2, 1), 'Erreur, fonction check_room().'
    assert not check_room(p, 10, 2), 'Erreur, fonction check_room().'
    assert not check_room(p, -1, 3), 'Erreur, fonction check_room().'
    assert check_room(p, 3, 3), 'Erreur, fonction check_room().'
    print('Fonction check_room() : OK')


def test_get_value():
    """
    Fonction de test de check_value().
    """
    p = {'n': 4, 'nb_cases_libres': 6, 'tiles': [6, 2, 3, 2, 0, 2, 6, 2, 0, 2, 2, 0, 1, 0, 0, 0]}
    assert get_value(p, 0, 0) == 6, 'Erreur : fonction get_value().'
    assert get_value(p, 2, 3) == 0, 'Erreur : fonction get_value().'
    assert get_value(p, 1, 3) == 2, 'Erreur : fonction get_value().'
    assert get_value(p, 3, 0) == 1, 'Erreur : fonction get_value().'
    try :
        get_value(p, 18, 3) # lève une erreur
    except AssertionError:
        print('get_value(p, 18, 3) a bien levé une erreur.')
    else:
        assert True == False, 'get_value(p, 18, 3) aurait du lever une erreur.'
    print('Fonction get_value() : OK')


def test_set_value():
    """
    Fonction de test de set_value().
    """
    p = init_play()
    set_value(p, 0, 0, 1)  # met la valeur 1 dans la case (0, 0)
    set_value(p, 1, 2, 0)  # met la valeur 0 dans la case (1, 2)
    set_value(p, 2, 3, 6)  # met la valeur 6 dans la case (2, 3)
    assert p == {'n' : 4, 'nb_cases_libres' : 14, 'tiles' : [1,0,0,0,0,0,0,0,0,0,0,6,0,0,0,0]}, 'Erreur fonction set_value'
    try:
        set_value(p, 18, 3, 1) # génère une erreur
    except AssertionError:
        print('set_value(p, 18, 3, 1) a bien levé une erreur.')
    else:
        assert True == False, 'set_value(p, 18, 3, 1) aurait du lever une erreur.'
    print('Fonction set_value() : OK')


def test_is_room_empty():
    """
    Fonction de test de is_room_empty().
    """
    p = {'n': 4,'nb_cases_libres': 14,'tiles': [0, 2, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]}
    assert not is_room_empty(p, 0, 1), 'Erreur : fonction is_room().'
    assert is_room_empty(p, 3, 2), 'Erreur : fonction is_room().'
    try:
        is_room_empty(p, 15, 2) # génère une erreur
    except AssertionError:
        print('is_room_empty(p, 15, 2) a bien levé une erreur.')
    else:
        assert True == False, 'is_room_empty(p, 15, 2) aurait du lever une erreur.'
    print('Fonction is_room_empty() : OK')


def test_get_nb_empty_rooms():
    """
    Fonction de test de get_nb_empty_rooms().
    """
    p = {'n': 4, 'nb_cases_libres': 42, 'tiles': [6, 2, 3, 2, 0, 2, 6, 2, 0, 2, 2, 0, 1, 0, 0, 0]}
    assert get_nb_empty_rooms(p) == 6, 'Erreur : fonction get_nb_empty_rooms().'
    assert p['nb_cases_libres'] == 6, 'Erreur : fonction get_nb_empty_rooms().'
    print('Fonction get_nb_empty_rooms() : OK')


def test_is_game_over():
    """
    Fonction de test de is_game_over().
    """
    p1 = {'n': 4, 'nb_cases_libres': 6, 'tiles': [6, 2, 3, 2, 0, 2, 6, 2, 0, 2, 2, 0, 1, 0, 0, 0]}
    p2 = {'n': 4, 'nb_cases_libres': 0, 'tiles': [6, 2, 3, 2, 12, 2, 6, 2, 6, 2, 2, 12, 1, 6, 3, 1]}
    assert is_game_over(p1) == False, 'Erreur : fonction is_game_over().'
    assert is_game_over(p2) == True, 'Erreur : fonction is_game_over().'
    print('Fonction is_game_over() : OK')


def test_get_score():
    """
    Fonction de test de get_score().
    """
    p1 = {'n': 4, 'nb_cases_libres': 6, 'tiles': [6, 2, 3, 2, 0, 2, 6, 2, 0, 2, 2, 0, 1, 0, 0, 0]}
    p2 = {'n': 4, 'nb_cases_libres': 0, 'tiles': [6, 2, 3, 2, 12, 2, 6, 2, 6, 2, 2, 12, 1, 6, 3, 1]}
    p3 = {'n': 4, 'nb_cases_libres': 16, 'tiles': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]}
    assert get_score(p1) == 28, 'Erreur : fonction get_score().'
    assert get_score(p2) == 68, 'Erreur : fonction get_score().'
    assert get_score(p3) == 0, 'Erreur : fonction get_score().'
    print('Fonction get_score() : OK')


def test_full_display():
    """
    Fonction de test de full_display().
    """
    p1 = {'n': 4, 'nb_cases_libres': 6, 'tiles': [6, 2, 3, 2, 0, 2, 6, 2, 0, 2, 2, 0, 1, 0, 0, 0]}
    p2 = {'n': 2, 'nb_cases_libres': 3, 'tiles': [0, 1, 2, 192]}
    a1 = full_display(p1)
    a2 = full_display(p2)
    assert a1 == '\n\x1b[40m                              \x1b[0m\n\x1b[40m  \x1b[0m\x1b[47m     \x1b[0m\x1b[40m  \x1b[0m\x1b[41m     \x1b[0m\x1b[40m  \x1b[0m\x1b[47m     \x1b[0m\x1b[40m  \x1b[0m\x1b[41m     \x1b[0m\x1b[40m  \x1b[0m\n\x1b[40m  \x1b[0m\x1b[1m\x1b[47m  6  \x1b[0m\x1b[40m  \x1b[0m\x1b[1m\x1b[41m\x1b[37m  2  \x1b[0m\x1b[40m  \x1b[0m\x1b[1m\x1b[47m  3  \x1b[0m\x1b[40m  \x1b[0m\x1b[1m\x1b[41m\x1b[37m  2  \x1b[0m\x1b[40m  \x1b[0m\n\x1b[40m  \x1b[0m\x1b[47m     \x1b[0m\x1b[40m  \x1b[0m\x1b[41m     \x1b[0m\x1b[40m  \x1b[0m\x1b[47m     \x1b[0m\x1b[40m  \x1b[0m\x1b[41m     \x1b[0m\x1b[40m  \x1b[0m\n\x1b[40m                              \x1b[0m\n\x1b[40m  \x1b[0m\x1b[44m     \x1b[0m\x1b[40m  \x1b[0m\x1b[41m     \x1b[0m\x1b[40m  \x1b[0m\x1b[47m     \x1b[0m\x1b[40m  \x1b[0m\x1b[41m     \x1b[0m\x1b[40m  \x1b[0m\n\x1b[40m  \x1b[0m\x1b[1m\x1b[44m\x1b[34m  0  \x1b[0m\x1b[40m  \x1b[0m\x1b[1m\x1b[41m\x1b[37m  2  \x1b[0m\x1b[40m  \x1b[0m\x1b[1m\x1b[47m  6  \x1b[0m\x1b[40m  \x1b[0m\x1b[1m\x1b[41m\x1b[37m  2  \x1b[0m\x1b[40m  \x1b[0m\n\x1b[40m  \x1b[0m\x1b[44m     \x1b[0m\x1b[40m  \x1b[0m\x1b[41m     \x1b[0m\x1b[40m  \x1b[0m\x1b[47m     \x1b[0m\x1b[40m  \x1b[0m\x1b[41m     \x1b[0m\x1b[40m  \x1b[0m\n\x1b[40m                              \x1b[0m\n\x1b[40m  \x1b[0m\x1b[44m     \x1b[0m\x1b[40m  \x1b[0m\x1b[41m     \x1b[0m\x1b[40m  \x1b[0m\x1b[41m     \x1b[0m\x1b[40m  \x1b[0m\x1b[44m     \x1b[0m\x1b[40m  \x1b[0m\n\x1b[40m  \x1b[0m\x1b[1m\x1b[44m\x1b[34m  0  \x1b[0m\x1b[40m  \x1b[0m\x1b[1m\x1b[41m\x1b[37m  2  \x1b[0m\x1b[40m  \x1b[0m\x1b[1m\x1b[41m\x1b[37m  2  \x1b[0m\x1b[40m  \x1b[0m\x1b[1m\x1b[44m\x1b[34m  0  \x1b[0m\x1b[40m  \x1b[0m\n\x1b[40m  \x1b[0m\x1b[44m     \x1b[0m\x1b[40m  \x1b[0m\x1b[41m     \x1b[0m\x1b[40m  \x1b[0m\x1b[41m     \x1b[0m\x1b[40m  \x1b[0m\x1b[44m     \x1b[0m\x1b[40m  \x1b[0m\n\x1b[40m                              \x1b[0m\n\x1b[40m  \x1b[0m\x1b[44m     \x1b[0m\x1b[40m  \x1b[0m\x1b[44m     \x1b[0m\x1b[40m  \x1b[0m\x1b[44m     \x1b[0m\x1b[40m  \x1b[0m\x1b[44m     \x1b[0m\x1b[40m  \x1b[0m\n\x1b[40m  \x1b[0m\x1b[1m\x1b[44m\x1b[37m  1  \x1b[0m\x1b[40m  \x1b[0m\x1b[1m\x1b[44m\x1b[34m  0  \x1b[0m\x1b[40m  \x1b[0m\x1b[1m\x1b[44m\x1b[34m  0  \x1b[0m\x1b[40m  \x1b[0m\x1b[1m\x1b[44m\x1b[34m  0  \x1b[0m\x1b[40m  \x1b[0m\n\x1b[40m  \x1b[0m\x1b[44m     \x1b[0m\x1b[40m  \x1b[0m\x1b[44m     \x1b[0m\x1b[40m  \x1b[0m\x1b[44m     \x1b[0m\x1b[40m  \x1b[0m\x1b[44m     \x1b[0m\x1b[40m  \x1b[0m\n\x1b[40m                              \x1b[0m\n', 'Erreur : fonction full_display().'
    assert a2 == '\n\x1b[40m                \x1b[0m\n\x1b[40m  \x1b[0m\x1b[44m     \x1b[0m\x1b[40m  \x1b[0m\x1b[44m     \x1b[0m\x1b[40m  \x1b[0m\n\x1b[40m  \x1b[0m\x1b[1m\x1b[44m\x1b[34m  0  \x1b[0m\x1b[40m  \x1b[0m\x1b[1m\x1b[44m\x1b[37m  1  \x1b[0m\x1b[40m  \x1b[0m\n\x1b[40m  \x1b[0m\x1b[44m     \x1b[0m\x1b[40m  \x1b[0m\x1b[44m     \x1b[0m\x1b[40m  \x1b[0m\n\x1b[40m                \x1b[0m\n\x1b[40m  \x1b[0m\x1b[41m     \x1b[0m\x1b[40m  \x1b[0m\x1b[47m     \x1b[0m\x1b[40m  \x1b[0m\n\x1b[40m  \x1b[0m\x1b[1m\x1b[41m\x1b[37m  2  \x1b[0m\x1b[40m  \x1b[0m\x1b[1m\x1b[47m 192 \x1b[0m\x1b[40m  \x1b[0m\n\x1b[40m  \x1b[0m\x1b[41m     \x1b[0m\x1b[40m  \x1b[0m\x1b[47m     \x1b[0m\x1b[40m  \x1b[0m\n\x1b[40m                \x1b[0m\n', 'Erreur : fonction full_display().'
    print('Fonction full_display() : OK')


"""
test_is_room_empty()
test_set_value()
test_get_value()
test_check_indice()
test_init_play()
test_check_room()
test_get_nb_empty_rooms()
test_is_game_over()
test_get_score()
test_full_display()
"""