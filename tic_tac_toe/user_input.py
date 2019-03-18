# Functions assist with user input validation
def allow_move(move:int, board:dict) -> int:
    """Determine if a move is legal"""
    if move not in range(1, 10) or board.get(move) != ' ':
        return False
    else:
        return move

def confirm_move(board:dict) -> int:
    """Ask the player to make a legal move"""
    move = 0
    while not allow_move(move, board):
        try:
            move = int(input('Choose an available space (1-9): '))
        except ValueError:
            continue
    return move

def confirm_rematch() -> bool:
    """Ask if the players want a rematch"""
    answer = ''
    while answer.lower() not in ['y', 'n']:
        answer = input('Would you like to play again? (y/n): ')
    return answer == 'y'





