from random import choice
from tic_tac_toe_ai import TicTacToeAI


def tic_tac_toe_game():
    # Initialize game
    while True:
        try:
            mode = input("Do you want to start the game in single player or multiplayer mode?"
                         " Type '1' for single and '2' for multi.\n")
            mode = int(mode)
            if mode == 1 or mode == 2:
                pass
            else:
                raise ValueError
        except ValueError:
            print("Please enter '1' or '2'")
        else:
            break
    players = ["X", "O"]
    # Randomly selects who goes first
    p1 = choice(players)
    if p1 == players[0]:
        p2 = players[1]
    else:
        p2 = players[0]
    p2_is_ai = None
    print(f"You play as {p1}")
    if mode == 1:
        p2_is_ai = True
        ai = TicTacToeAI()
        print(f"AI plays as {p2}")
    game_is_on = True
    game_round = 1
    fields = {
        "a1": "   ",
        "b1": "   ",
        "c1": "   ",
        "a2": "   ",
        "b2": "   ",
        "c2": "   ",
        "a3": "   ",
        "b3": "   ",
        "c3": "   "
    }

    def print_game_board():
        """
        Renders the current state of the board into the console.

        """
        guide_row = ["  ", "a", "   ", "b", "   ", "c"]
        row_1 = [1, fields["a1"], "|", fields["b1"], "|", fields["c1"]]
        row_2 = [2, fields["a2"], "|", fields["b2"], "|", fields["c2"]]
        row_3 = [3, fields["a3"], "|", fields["b3"], "|", fields["c3"]]
        separator = "-----------------"
        print(*guide_row)
        print(*row_1)
        print(separator)
        print(*row_2)
        print(separator)
        print(*row_3)

    def place_sign(player: str):
        """
        Asks the passed in player to choose a cell, if they choose an already populated cell or give a nonexistent cell,
        asks them to try again.
        :param player: the player to take a turn
        """
        while True:
            if game_round > 1:
                selection = input(f"{player}'s turn, select a column and a row like 'a1' or 'c2:\n")
            else:
                selection = input(f"{player} starts the game, select a column and a row like 'a1' or 'c2:\n")
            try:
                if selection in fields:
                    if fields[selection] == "   ":
                        fields[selection] = f" {player} "
                    else:
                        raise ValueError
                else:
                    raise KeyError
            except KeyError:
                print("This is not a valid field on the board, please input a column (a,b,c) and a row(1,2,3) such as "
                      "'c2'")
            except ValueError:
                print("This field is already populated, please choose another one.")
            else:
                break

    def check_winner() -> str:
        """
        Checks if any possible win condition was met on the board.
        :return:
        If there was a winner, returns the winner's sign.
        """
        if fields["a1"] == fields["a2"] and fields["a2"] == fields["a3"] and fields["a1"] != "   ":
            return fields["a1"][1]
        if fields["b1"] == fields["b2"] and fields["b2"] == fields["b3"] and fields["b1"] != "   ":
            return fields["b1"][1]
        if fields["c1"] == fields["c2"] and fields["c2"] == fields["c3"] and fields["c1"] != "   ":
            return fields["c1"][1]
        if fields["a1"] == fields["c1"] and fields["c1"] == fields["b1"] and fields["a1"] != "   ":
            return fields["c1"][1]
        if fields["a1"] == fields["b2"] and fields["b2"] == fields["c3"] and fields["a1"] != "   ":
            return fields["a1"][1]
        if fields["c1"] == fields["b2"] and fields["b2"] == fields["a3"] and fields["c1"] != "   ":
            return fields["c1"][1]
        if fields["a3"] == fields["b3"] and fields["b3"] == fields["c3"] and fields["a3"] != "   ":
            return fields["a3"][1]
        if fields["a2"] == fields["b2"] and fields["b2"] == fields["c2"] and fields["a2"] != "   ":
            return fields["a2"][1]

    # Starts the game
    while game_is_on:
        # Renders the board into the console
        print_game_board()
        # Checks if any win condition was met and declares the winner
        if not check_winner():
            # Checks if all fields have been populated
            if game_round < 10:
                # Decides which player is up next
                if game_round % 2 == 0:
                    if p1 == players[1]:
                        place_sign(p1)
                        game_round += 1
                    else:
                        if p2_is_ai:
                            fields = ai.next_move(fields=fields, sign=p2, opponent_sign=p1)
                        else:
                            place_sign(p2)
                        game_round += 1
                else:
                    if p1 == players[0]:
                        place_sign(p1)
                        game_round += 1
                    else:
                        if p2_is_ai:
                            fields = ai.next_move(fields=fields, sign=p2, opponent_sign=p1)
                        else:
                            place_sign(p2)
                        game_round += 1
            else:
                print("No more fields left, game ended in a tie.")
                game_is_on = False
        else:
            print(f"{check_winner()} won the game!")
            game_is_on = False
    play_again = input("Do you want to play another game? Type Y for yes, anything else to quit").lower()
    if play_again == "y":
        tic_tac_toe_game()


tic_tac_toe_game()
