from life_cycle.cycle_game import cycle_play, create_new_play, restore_game, save_game, get_score,is_game_over
from ui.user_entries import get_user_menu


def threes():
    """ Permet d'enchainer les parties au jeu Threes, de reprendre une partie sauvegardée et de sauvegarder une
    partie en cours """


    user_entries = get_user_menu(None)

    while user_entries != "Q":

        if user_entries == "N":

            partie = create_new_play()
            x = cycle_play(partie)
            if not x:
                user_entries = get_user_menu(partie)

        elif user_entries == "L":

            partie = restore_game()
            x = cycle_play(partie)
            if not x:
                user_entries = get_user_menu(partie)

        elif user_entries == "S":

            if not is_game_over(partie['plateau']):
                save_game(partie)
                print("\nLa partie a bien été sauvegardée.")
                user_entries = get_user_menu(partie)

            else :
                print("\nImpossible de sauvegarder une partie terminée.")

        elif user_entries == "C":

            if not is_game_over(partie['plateau']):
                x = cycle_play(partie)
                if not x:
                    user_entries = get_user_menu(partie)
            else :
                print("\nVous ne pouvez pas continuer une partie terminée !")

        if x:
            print("Partie terminée. Score :",get_score(partie['plateau']))
            print("\n")

            user_entries = get_user_menu(partie)


    return

threes()