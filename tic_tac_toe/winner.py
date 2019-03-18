def check_for_win(board:dict, win_conditions:list) -> bool:
    """
    Given the current state of the board, and all possible
    win conditions, determine if a player won after their move
    """
    for spaces in win_conditions:
        space_values = [board.get(space) for space in spaces]
        # Remove empty spaces
        space_values = list(filter(lambda space:space != ' ', space_values))
        # Skip the check if not all the spaces are filled
        if len(space_values) < 3:
            continue
        all_equal = space_values.count(space_values[0]) == 3
        if all_equal:
            return True
    return False

def check_for_tie(board:dict) -> bool:
    """
    Given the current state of the board, determine if
    there are any empty spaces left to play
    """
    available_spaces = [space == ' ' for space in board.values()]
    return not any(available_spaces)