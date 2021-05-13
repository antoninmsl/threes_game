# -------- Fonctions de la partie 3 --------
#import sys
#sys.path.append("../")
#from life_cycle.cycle_game import is_game_over

def get_user_move():
    """
    Saisi et retourne le coup joué par le joueur parmi les choix :
    :return: Choix de l'utilisateur (en minuscule)

    - 'h' pour haut,
    - 'b' pour bas,
    - 'g' pour gauche,
    - 'd' pour droite,
    - 'm' pour menu principal.
    """
    user_move = input()
    while user_move not in ['h', 'H', 'b', 'B', 'g', 'G', 'd', 'D', 'm', 'M', 'z', 'Z', 'q', 'Q', 's', 'S', 'd', 'D']:
        user_move = input()
    return user_move.lower()


def get_user_menu(partie):
    """
    Saisi et retourne le choix du joueur dans le menu principal
    :param partie: Partie de jeu en cours ou None sinon
    :return: Choix de l'utilisateur (en majuscule)

    - 'N' : Commencer une nouvelle partie,
    - 'L' : Charger une partie,
    - 'S' : Sauvegarder la partie en cours (si le paramètre partie correspond à une partie en cours),
    - 'C' : Reprendre la partie en cours (si le paramètre partie correspond à une partie en cours),
    - 'Q' : Terminer le jeu.
    """
    if partie == None : #or is_game_over(partie['plateau])
        user_choice = input(
            "\n -N pour commencer une nouvelle partie. \n -L pour charger une partie. \n -Q pour terminer le jeu. \n")
        while user_choice not in ['N', 'n', 'L', 'l', 'Q', 'q']:
            user_choice = input(
                " -N pour commencer une nouvelle partie. \n -L pour charger une partie. \n -Q pour terminer le "
                "jeu. \n")

    else:
        user_choice = input(
            "\n -N pour commencer une nouvelle partie. \n -L pour charger une partie. \n -S pour sauvegarder la "
            "partie en cours \n -C pour reprendre la partie en cours \n -Q pour terminer le jeu. \n")
        while user_choice not in ['N', 'n', 'L', 'l', 'S', 's', 'C', 'c', 'Q', 'q']:
            user_choice = input(" -N pour commencer une nouvelle partie. \n -L pour charger une partie. \n -S pour "
                                "sauvegarder "
                                "la partie en cours \n -C pour reprendre la partie en cours \n -Q pour terminer le "
                                "jeu. \n \n")

    return user_choice.upper()
