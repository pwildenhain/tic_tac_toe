def create_empty_game_board() -> dict:
  """Create an empty tic tac toe dict"""
  game_board = {1: ' ', 2: ' ', 3: ' ',
                4: ' ', 5: ' ', 6: ' ',
                7: ' ', 8: ' ', 9: ' '}
  return game_board

def print_game_board(board:dict):
  """Display the tic tac toe board in the console"""
  print(
    f"""
   {board.get(1)} | {board.get(2)} | {board.get(3)}
 -------------
   {board.get(4)} | {board.get(5)} | {board.get(6)}
 -------------
   {board.get(7)} | {board.get(8)} | {board.get(9)}     
    """)

