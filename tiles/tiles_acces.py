
# -------- Fonctions de la partie 1 --------

def check_indice(plateau, indice):
    """
    Retourne True si indice correspond à un indice valide de case pour le plateau (entre 0 et n-1)

    :Exemple:
    p = init_play()

    check_indice(p, 0) # retourne True
    check_indice(p, 10) # retourne False
    check_indice(p, 3) # retourne True
    check_indice(p, 4) # retourne False
    check_indice(p, -1) # retourne False
    """
    # Retourne True si indice correspond à un indice valide de case pour le plateau (entre 0 et n-1 compris).
    return 0 <= indice <= plateau['n'] - 1


def check_room(plateau, lig, col):
    """
    Retourne True si (lig, col) est une case du plateau (lig et col sont des indices valides).

    :Exemple:
    p = init_play()

    check_room(p, 2, 1) # retourne True
    check_room(p, 10, 2) # retourne False
    check_room(p, -1, 3) # retourne False
    check_room(p, 3, 3) # retourne True
    """
    # Retourne True si (lig, col) est une case du plateau (lig et col sont des indices valides).
    return check_indice(plateau, lig) and check_indice(plateau, col)


def get_value(plateau, lig, col):
    """
    Retourne la valeur de la case (lig, col).
    Erreur si (lig, col) n'est pas valide.

    :Exemple:
    p = {
        'n' : 4,
        'nb_cases_libres' : 6,
        'tiles' : [6, 2, 3, 2, 0, 2, 6, 2, 0, 2, 2, 0, 1, 0, 0, 0]
        }

    get_value(p, 0, 0) # retourne 6
    get_value(p, 2, 3) # retourne 0 (la case est vide)
    get_value(p, 1, 3) # retourne 2
    get_value(p, 3, 0) # retourne 1
    get_value(p, 18, 3) # lève une erreur
    """
    assert check_room(plateau, lig, col), 'Erreur : coordonnées non-valides.'  # Vérifie que les coordonnées (lig,col)
    # correspondent à une case valide de plateau, sinon renvoie d'une erreur.

    return plateau['tiles'][lig*plateau['n']+col]  # Retourne la valeur de la case dont les coordonnées sont (lig,col)
    # du plateau.


def set_value(plateau, lig, col, val):
    """
    Affecte la valeur val dans la case (lig, col) du plateau.
    Erreur si (lig, col) n'est pas une case valide
    ou si val n'est pas supérieure ou égale à 0.
    Met aussi à jour le nombre de cases libres (sans tuile(s)).

    :Exemple:
    p = init_play()

    set_value(p, 0, 0, 1) # met la valeur 1 dans la case (0, 0)
    set_value(p, 1, 2, 0) # met la valeur 0 dans la case (1, 2)
    set_value(p, 18, 3, 1) # génère une erreur
    set_value(p, 2, 3, 6) # met la valeur 6 dans la case (2, 3)
    """
    assert check_room(plateau,lig, col), 'Erreur : coordonnées non-valides.'  # Vérifie que les coordonnées (lig,col)
    # correspondent à une case valide de plateau, sinon renvoie d'une erreur.

    assert val >= 0, 'Erreur : val doit être positive.'  # Verifie que val est supérieure ou égale à 0, sinon renvoie
    # d'une erreur.

    # Met à jour le nombre de cases libres en fonction de val (+1 si val == 0 ou -1 si val > 0 )
    if val == 0 and plateau['tiles'][lig*plateau['n']+col] > 0:
        plateau['nb_cases_libres'] += 1
    elif val > 0 and plateau['tiles'][lig*plateau['n']+col] == 0:
        plateau['nb_cases_libres'] -= 1
    plateau['tiles'][lig*plateau['n']+col] = val  # Affecte la valeur val dans la case (lig, col) du plateau.


def is_room_empty(plateau, lig, col):
    """
    Teste si une case du plateau est libre ou pas.
    Retourne True si la case est libre, False sinon.

    :Exemple:
    p = {
            'n' : 4,
            'nb_cases_libres' : 14,
            'tiles' : [0, 2, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        }

    is_room_empty(p, 0, 1) # retourne False
    is_room_empty(p, 3, 2) # retourne True
    is_room_empty(p, 15, 2) # génère une erreur
    """
    assert check_room(plateau, lig, col), 'Erreur : coordonnées non-valides.'   # Vérifie que les coordonnées (lig,col)
    # correspondent à une case valide de plateau, sinon renvoie d'une erreur.

    return plateau['tiles'][lig*plateau['n']+col] == 0  # Retourne True si la case est libre, False sinon.

