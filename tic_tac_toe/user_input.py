# Functions assist with user input validation
def allow_move(move:int, board:dict) -> int:
    """Determine if a move is legal"""
    if move not in range(1, 10) or board.get(move) != ' ':
        return False
    else:
        return move

def confirm_move(board:dict) -> int:
    """Ask the player to make a legal move"""
    while True:
        try:
            move = int(input('Choose a space to move: '))
        except ValueError:
            continue
        if not allow_move(move, board):
            continue
        else:
            break
    return move

def confirm_rematch() -> bool:
    """Ask if the players want a rematch"""
    answer = ''
    while answer.lower() not in ['y', 'n']:
        answer = input('Would you like to play again? (y/n): ')
    return answer == 'y'





