from collections.abc import Iterable

from GuessingGame import attempt_clear, interface, main
from GuessingGame_V2 import main_v2

def convert_to_bool(to_convert: str, true_list: Iterable=("yes", "1", "true")):
  to_convert = to_convert.lower()
  if to_convert in true_list: return True
  return False

while True:
  try:
    version = convert_to_bool(interface("Would you like to use preset difficulties?"))
    
  except Exception as e:
    print(f'An error has occurred!\n{e}\n\n')
    continue

  attempt_clear()
  
  if version: 
    if main_v2() is False:
      continue

  if main() is False:
    continue