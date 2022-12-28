from BlackJack import blackJack
import os

Valid = False
shouldPlay = True

while (shouldPlay):
  while (not Valid):
    init_game = input("Do you want to play a game of Black-jack? Type 'y' or 'n': ")
    
    if (init_game == 'y' or init_game == 'Y') :
      shouldPlay = True
      Valid = True
      os.system('clear')
    
    elif (init_game == 'n' or init_game == 'N') :
      shouldPlay = False
      Valid = True

  Valid = False
  
  if (shouldPlay):
    blackJack()
  