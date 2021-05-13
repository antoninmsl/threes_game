import sys
sys.path.append('../')
from life_cycle.cycle_game import init_play
from tiles.tiles_moves import get_next_alea_tiles, put_next_tiles, line_pack, column_pack, line_move, column_move, lines_move, columns_move, play_move


def test_get_next_alea_tiles():
    """ Fonction de test de get_next_alea_tiles()."""
    p = init_play()

    tiles = get_next_alea_tiles(p, 'init')
    assert tiles['mode'] == 'init', "Erreur : fonction get_next_alea_tiles()."
    assert tiles['0']['val'] == 2, "Erreur : fonction get_next_alea_tiles()."
    assert tiles['1']['val'] == 1, "Erreur : fonction get_next_alea_tiles()."
    assert tiles['0']['lig'] is not None and tiles['0']['col'] is not None, "Erreur : fonction get_next_alea_tiles()."
    assert tiles['1']['lig'] is not None and tiles['1']['col'] is not None, "Erreur : fonction get_next_alea_tiles()."
    assert tiles['check'], "Erreur : fonction get_next_alea_tiles()."

    tiles = get_next_alea_tiles(p, 'encours')
    assert tiles['mode'] == 'encours', "Erreur : fonction get_next_alea_tiles()."
    assert tiles['0']['val'] in [1, 2, 3], "Erreur : fonction get_next_alea_tiles()."
    assert tiles['0']['lig'] is not None and tiles['0']['col'] is not None, "Erreur : fonction get_next_alea_tiles()."
    assert tiles['check'], "Erreur : fonction get_next_alea_tiles()."

    print('Fonction get_next_alea_tiles() : OK')


def test_put_next_tiles():
    """ Fonction de test de put_next_tiles()."""
    p = init_play()
    tiles1 = {'mode': 'init',
                '0': {'val': 2, 'lig': 0, 'col': 1},
                '1': {'val': 1, 'lig': 3, 'col': 3},
                'check': True}
    put_next_tiles(p, tiles1)
    assert p == {'n': 4,
                 'nb_cases_libres': 14,
                 'tiles': [0,2,0,0,0,0,0,0,0,0,0,0,0,0,0,1]
                 }, 'Erreur : fonction put_next_tiles().'
    tiles2 = {'mode': 'encours',
                '0': {'val': 3, 'lig': 0, 'col': 2},
                'check': True}
    put_next_tiles(p, tiles2)
    assert p == {'n': 4,
                 'nb_cases_libres': 13,
                 'tiles': [0, 2, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]
                 }, 'Erreur : fonction put_next_tiles().'
    p = {'n': 4,
                 'nb_cases_libres': 3,
                 'tiles': [2, 2, 3, 2, 6, 12, 24, 48, 96, 192, 384, 768, 0, 0, 0, 1]
                 }
    tiles3 = {'mode': 'encours',
              '0': {'val': 3, 'lig': 0, 'col': 0},
              'check': True}
    put_next_tiles(p, tiles3)
    assert p == {'n': 4,
                 'nb_cases_libres': 2,
                 'tiles': [2, 2, 3, 2, 6, 12, 24, 48, 96, 192, 384, 768, 3, 0, 0, 1]
                 } or p == {'n': 4,
                 'nb_cases_libres': 2,
                 'tiles': [2, 2, 3, 2, 6, 12, 24, 48, 96, 192, 384, 768, 0, 3, 0, 1]
                 } or p == {'n': 4,
                 'nb_cases_libres': 2,
                 'tiles': [2, 2, 3, 2, 6, 12, 24, 48, 96, 192, 384, 768, 0, 0, 3, 1]
                 }, 'Erreur : fonction put_next_tiles().'
    print('Fonction put_next_tiles() : OK')


def test_line_pack():
    """ Fonction de test de line_pack()."""
    p = {'n': 4, 'nb_cases_libres': 10, 'tiles': [0, 2, 0, 0, 0, 2, 3, 3, 0, 2, 2, 0, 0, 0, 0, 0]}
    line_pack(p, 1, 0, 1)
    assert p['tiles'] == [0, 2, 0, 0, 2, 3, 3, 0, 0, 2, 2, 0, 0, 0, 0, 0]
    line_pack(p, 1, 2, 1)
    assert p['tiles'] == [0, 2, 0, 0, 2, 3, 0, 0, 0, 2, 2, 0, 0, 0, 0, 0]
    line_pack(p, 1, 3, 0)
    assert p['tiles'] == [0, 2, 0, 0, 0, 2, 3, 0, 0, 2, 2, 0, 0, 0, 0, 0]
    line_pack(p, 1, 2, 0)
    assert p['tiles'] == [0, 2, 0, 0, 0, 0, 2, 0, 0, 2, 2, 0, 0, 0, 0, 0]
    print('Fonction line_pack() : OK')


def test_column_pack():
    """ Fonction de test de column_pack()."""
    p = {'n': 4, 'nb_cases_libres': 10, 'tiles': [1, 2, 3, 6, 12, 24, 48, 96, 192, 384, 768, 1536, 3072, 6144, 12288, 0]}
    column_pack(p, 1, 0, 1)
    assert p['tiles'] == [1, 24, 3, 6, 12, 384, 48, 96, 192, 6144, 768, 1536, 3072, 0, 12288, 0]
    column_pack(p, 1, 2, 1)
    assert p['tiles'] == [1, 24, 3, 6, 12, 384, 48, 96, 192, 0, 768, 1536, 3072, 0, 12288, 0]
    column_pack(p, 1, 3, 0)
    assert p['tiles'] == [1, 0, 3, 6, 12, 24, 48, 96, 192, 384, 768, 1536, 3072, 0, 12288, 0]
    column_pack(p, 1, 2, 0)
    assert p['tiles'] == [1, 0, 3, 6, 12, 0, 48, 96, 192, 24, 768, 1536, 3072, 0, 12288, 0]
    print('Fonction column_pack() : OK')


def test_line_move():
    """ Fonction de test de line_move()."""
    p = {'n': 4, 'nb_cases_libres': 10, 'tiles': [0, 2, 0, 0, 0, 2, 3, 3, 0, 2, 2, 0, 0, 0, 0, 0]}
    line_move(p, 1, 1)
    assert p['tiles'] == [0, 2, 0, 0, 2, 3, 3, 0, 0, 2, 2, 0, 0, 0, 0, 0]
    line_move(p, 1, 1)
    assert p['tiles'] == [0, 2, 0, 0, 2, 6, 0, 0, 0, 2, 2, 0, 0, 0, 0, 0]  # Les 3 se tassent pour donner un 6 dans le sens du tassement
    line_move(p, 2, 0)
    assert p['tiles'] == [0, 2, 0, 0, 2, 6, 0, 0, 0, 0, 2, 2, 0, 0, 0, 0]
    line_move(p, 2, 0)
    assert p['tiles'] == [0, 2, 0, 0, 2, 6, 0, 0, 0, 0, 2, 2, 0, 0, 0, 0]  # Aucun changement car les 2 ne peuvent se tasser qu'avec les 1
    print('Fonction line_move() : OK')


def test_column_move():
    """ Fonction de test de column_move()."""
    p = {'n': 4, 'nb_cases_libres': 10, 'tiles': [0, 0, 0, 0,
                                                  2, 2, 2, 0,
                                                  0, 3, 2, 0,
                                                  0, 3, 0, 0]
         }
    column_move(p, 1, 1)
    assert p['tiles'] == [0, 2, 0, 0,
                          2, 3, 2, 0,
                          0, 3, 2, 0,
                          0, 0, 0, 0]
    column_move(p, 1, 1)
    assert p['tiles'] == [0, 2, 0, 0,
                          2, 6, 2, 0,
                          0, 0, 2, 0,
                          0, 0, 0, 0]  # Les 3 se tassent pour donner un 6 dans le sens du tassement
    column_move(p, 2, 0)
    assert p['tiles'] == [0, 2, 0, 0,
                          2, 6, 0, 0,
                          0, 0, 2, 0,
                          0, 0, 2, 0]
    column_move(p, 2, 0)
    assert p['tiles'] == [0, 2, 0, 0,
                          2, 6, 0, 0,
                          0, 0, 2, 0,
                          0, 0, 2, 0]  # Aucun changement car les 2 ne peuvent se tasser qu'avec les 1
    print('Fonction column_move() : OK')


def test_lines_move():
    """ Fonction de test de lines_move()."""
    p = {'n': 4, 'nb_cases_libres': 10, 'tiles': [0, 0, 0, 0,
                                                  3, 3, 3, 0,
                                                  0, 3, 2, 0,
                                                  0, 3, 0, 0]
         }
    lines_move(p,1)
    assert p['tiles'] == [0, 0, 0, 0,
                          6, 3, 0, 0,
                          3, 2, 0, 0,
                          3, 0, 0, 0]
    p = {'n': 4, 'nb_cases_libres': 10, 'tiles': [0, 0, 0, 0,
                                                  3, 3, 3, 0,
                                                  0, 3, 2, 0,
                                                  0, 3, 0, 0]
         }
    lines_move(p,0)
    assert p['tiles'] == [0, 0, 0, 0,
                          0, 3, 3, 3,
                          0, 0, 3, 2,
                          0, 0, 3, 0]

    lines_move(p,0)
    assert p['tiles'] == [0, 0, 0, 0,
                          0, 0, 3, 6,
                          0, 0, 3, 2,
                          0, 0, 0, 3]

    print("Fonction lines_move() : OK ")


def test_columns_move():
    """ Fonction de test de columns_move()."""
    p = {'n': 4, 'nb_cases_libres': 10, 'tiles': [0, 0, 0, 0,
                                                  3, 3, 3, 0,
                                                  0, 3, 2, 0,
                                                  0, 3, 0, 0]
         }
    columns_move(p,0)
    assert p['tiles'] == [0, 0, 0, 0,
                          0, 0, 0, 0,
                          3, 3, 3, 0,
                          0, 6, 2, 0]
    p = {'n': 4, 'nb_cases_libres': 10, 'tiles': [0, 0, 0, 0,
                                                  3, 3, 1, 0,
                                                  0, 3, 2, 0,
                                                  0, 3, 0, 0]
         }
    columns_move(p,1)
    assert p['tiles'] == [3, 3, 1, 0,
                          0, 3, 2, 0,
                          0, 3, 0, 0,
                          0, 0, 0, 0]

    columns_move(p,1)
    assert p['tiles'] == [3, 6, 3, 0,
                          0, 3, 0, 0,
                          0, 0, 0, 0,
                          0, 0, 0, 0]

    print("Fonction columns_move() : OK ")


def test_play_move():
    p = {'n': 4, 'nb_cases_libres': 10, 'tiles': [0, 0, 0, 0,
                                                  3, 3, 3, 0,
                                                  0, 3, 2, 0,
                                                  0, 3, 0, 0]}
    play_move(p, 'g')
    assert p['tiles'] == [0, 0, 0, 0,
                          6, 3, 0, 0,
                          3, 2, 0, 0,
                          3, 0, 0, 0]
    p = {'n': 4, 'nb_cases_libres': 10, 'tiles': [0, 0, 0, 0,
                                                  3, 3, 3, 0,
                                                  0, 3, 2, 0,
                                                  0, 3, 0, 0]}
    play_move(p, 'd')
    assert p['tiles'] == [0, 0, 0, 0,
                          0, 3, 3, 3,
                          0, 0, 3, 2,
                          0, 0, 3, 0]
    play_move(p, 'd')
    assert p['tiles'] == [0, 0, 0, 0,
                          0, 0, 3, 6,
                          0, 0, 3, 2,
                          0, 0, 0, 3]
    p = {'n': 4, 'nb_cases_libres': 10, 'tiles': [0, 0, 0, 0,
                                                  3, 3, 3, 0,
                                                  0, 3, 2, 0,
                                                  0, 3, 0, 0]}
    play_move(p, 'b')
    assert p['tiles'] == [0, 0, 0, 0,
                          0, 0, 0, 0,
                          3, 3, 3, 0,
                          0, 6, 2, 0]
    p = {'n': 4, 'nb_cases_libres': 10, 'tiles': [0, 0, 0, 0,
                                                  3, 3, 1, 0,
                                                  0, 3, 2, 0,
                                                  0, 3, 0, 0]}
    play_move(p, 'h')
    assert p['tiles'] == [3, 3, 1, 0,
                          0, 3, 2, 0,
                          0, 3, 0, 0,
                          0, 0, 0, 0]
    play_move(p, 'h')
    assert p['tiles'] == [3, 6, 3, 0,
                          0, 3, 0, 0,
                          0, 0, 0, 0,
                          0, 0, 0, 0]
    print("Fonction play_move() : OK ")


"""
test_get_next_alea_tiles()
test_put_next_tiles()
test_line_pack()
test_column_pack()
test_line_move()
test_column_move()
test_lines_move()
test_columns_move()
test_play_move()
"""