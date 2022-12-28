from art import logo
import random

ACE_POSITION = 0
OVER_SCORE = 22

def getCard(player_cards, player_ace_count, player_score, cards, domain_size):
  rand_index = random.randint(0, domain_size - 1)
  player_cards.append(cards[rand_index])
  player_score[0] += cards[rand_index]
  if rand_index == ACE_POSITION:
    player_ace_count[0] += 1

def blackJack():
  cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
  domain_size = len(cards)

  user_cards = []
  user_ace_count = [0]
  user_score = [0]

  comp_cards = []
  comp_ace_count = [0]
  comp_score = [0]
  
  print(logo)

  random.seed()

  ## Initiazling player and computer cards ##
  
  # Initializing user cards
  for i in range(2):
    getCard(user_cards, user_ace_count, user_score, cards, domain_size)
  
  # Initializing computer cards
  for i in range(1):
    getCard(comp_cards, comp_ace_count, comp_score, cards, domain_size)
  
  print(f'\t Your cards: {user_cards}, current score: {user_score[0]}')
  print(f'\t Computer\'s first card: {comp_cards[0]}')

  
  ## Adding cards to player's hand ##

  while (True):   
    # Adding cards to palyer's hand first
    # Validating yes or no prompt
    Valid = False
    more_cards = ""
    while (not Valid):
      more_cards = input("Type 'y' to get another card, type 'n' to pass: ")
      if (more_cards == 'y' or more_cards == 'Y' or
           more_cards == 'n' or more_cards == 'N'):
        Valid = True

    # adding cards if player decided yes
    if (more_cards == 'y' or more_cards == 'Y'):
      getCard(user_cards, user_ace_count, user_score, cards, domain_size)
    # checks if the user has over OVER_SCORE
      if (user_score[0] >= OVER_SCORE):
        # if the user has an ace card, make the ace card as 1. not yet over
        if (user_ace_count[0] > 0):
          user_score[0] -= 10
          user_ace_count[0] -= 1
      
      print(f'\t Your cards: {user_cards}, current score: {user_score[0]}')
      print(f'\t Computer\'s first card: {comp_cards[0]}')
      
    # stop adding cards if no
    else:
      break

    # checks if the user has over OVER_SCORE
    if (user_score[0] >= OVER_SCORE):
      break

        
  ## Adding cards to computer's hand ##
  while (comp_score[0] < 17):
    getCard(comp_cards, comp_ace_count, comp_score, cards, domain_size)
    # checks if the comp has over OVER_SCORE
    if (comp_score[0] >= OVER_SCORE):
      # if the computer has an ace card, make the ace card as 1.
      if (comp_ace_count[0] > 0):
        comp_score[0] -= 10
        comp_ace_count[0] -= 1


  ## Computing on who wins ##
  print(f'\t Your final hand {user_cards}, final score: {user_score[0]}')
  print(f'\t Computer\'s final hand {comp_cards}, final score: {comp_score[0]}')

  if (user_score[0] >= OVER_SCORE):
    print("You lose. You went over")
  elif (user_score[0] == 21):
    print("You win! Black Jack")
  elif (comp_score[0] >= OVER_SCORE):
    print("You win! Your openent went over")
  elif (user_score[0] < comp_score[0]):
    print("You lose. Your oponent has a greater score")
  elif (user_score[0] > comp_score[0]):
    print("You win! You have a greater score")
  elif (user_score[0] == comp_score[0]):
    print("Draw")