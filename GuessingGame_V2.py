from GuessingGame import Game, GuessingGame, attempt_clear, handle_errors, interface

__modes = {'easy': [5, 20], 'medium': [10, 100], 'hard': [15, 500]}

modes_str = ""
for mode in __modes:
  modes_str += f"{mode}, "
modes_str = modes_str.removesuffix(", ")

@handle_errors
def main_v2():
  print(f"Available modes: {modes_str} \n")
  inputted_mode = interface("Please enter in the mode you wish to use")
  attempt_clear()
  if inputted_mode not in __modes: raise Exception("Mode is not available.")
  __mode = __modes[inputted_mode]
  # Will work on from here, add game object.
  game = GuessingGame(__mode[0], __mode[1])
  
  Game(game, __mode[0])
