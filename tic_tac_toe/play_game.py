from tic_tac_toe import game_board
from tic_tac_toe import user_input
from tic_tac_toe import winner

def play_tic_tac_toe():
    """Play a rousing game of tic tac toe in the terminal"""
    # Setup the game
    win_conditions = [(1, 2, 3), (4, 5, 6), (7, 8, 9),
                      (1, 4, 7), (2, 5, 8), (3, 6, 9),
                      (1, 5, 9), (3, 5, 7)]
    board = game_board.create_empty_game_board()
    player = 'X'
    # Start playing
    while True:    
        game_board.print_game_board(board)
        print(f"{player}'s turn")
        move = user_input.confirm_move(board)
        board[move] = player

        winner_found = winner.check_for_win(board, win_conditions)
        tie_found = winner.check_for_tie(board)
        if winner_found or tie_found:
            if winner_found:
                print(f"{player}'s win! Woot Woot!")
            else:
                print("Aw shucks, it's a tie...")
            game_board.print_game_board(board)
            rematch = user_input.confirm_rematch()
            if rematch:
                board = game_board.create_empty_game_board()
                player = 'X'
                continue
            else:
                print('Thanks for playing!')
                break
        # If no win or tie, then switch players
        player = 'O' if player == 'X' else 'X'