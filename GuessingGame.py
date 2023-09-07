class GuessingGame:
  def __init__(self, max_guesses: int=3, max_num: int=20) -> None:
    from random import randint
    
    self.__MAX_GUESSES = max_guesses
    self.__NUMBER = randint(1, max_num)
    self.guess = 0
    self.__attempts = 0

  def check_guess(self, guess: int) -> bool:
    self.__attempts += 1
    
    if self.__attempts >= self.__MAX_GUESSES:
      raise Exception("Maximum amount of attempts reached.")
      return False
    elif guess < self.__NUMBER: 
      print("Your guess is lower.")
      return False
    elif guess > self.__NUMBER:
      print("Your guess is higher.")
      return False
      
    return True

def handle_errors(func):

  def inner1(*args, **kwargs):
    try:
      func(*args, **kwargs)
    except Exception as e:
      print(f'An error has occurred!\n{e}\n\n')
      return False
  
  return inner1

def interface(text) -> str: # Not necessary, but still nice to have.
  inp = input(f"{text}:\n> ")
  return inp

def attempt_clear():
  import os, platform
  
  if platform.platform().startswith("Windows"):
    os.system("cls")
    return
    
  os.system("clear")

def Game(game: GuessingGame, max_guesses: int):
  attempts = 0
  
  while True:
    print(f'{max_guesses - attempts} attempts left.\n\n')
    try:
      guess = int(interface("Please enter your guess"))
      attempts += 1
    except TypeError:
      print("Please ensure you have entered a valid integer! (0-9 digits)")
      return
    attempt_clear()
    if game.check_guess(guess):
      print("You win!\n\n")
      break

@handle_errors
def main():
  max_guesses = int(interface("Please type in the maxium amount of guesses"))
  max_num = int(interface("Please type in the maximum random number"))
  game = GuessingGame(max_guesses, max_num)

  Game(game, max_guesses)

if __name__ == "__main__":
  while True:
    try:
      main()
    except Exception as e:
      print(f'An error has occurred!\n{e}\n\n')
      continue