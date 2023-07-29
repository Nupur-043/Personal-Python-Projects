
############### Our Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.
import random
from replit import clear
from art import logo 

def deal_card():
  """Returns a random card from the deck."""
  cards=[11,2,3,4,5,6,7,8,9,10,10,10,10]
  return random.choice(cards)

def calculate_score(cards):
  #if 11 in cards and 10 in cards and len(cards)==1:
  if sum(cards)==21 and len(cards)==2 :
    return 0
  if 11 in cards and sum(cards)>21:
    cards.remove(11)
    cards.append(1)
  
  return sum(cards)

def compare(user_score, computer_score):
  if user_score == computer_score:
    return "Draw🙃"
  elif computer_score == 0:
    return "Opponent has blackjack,You loose!😱"
  elif user_score == 0 :
    return 'You Win with a blackjack!😎'
  elif user_score > 21:
    return "You went over. You lose😭"
  elif computer_score>21:
    return "Opponent went over, you win😁"
  elif user_score > computer_score:
    return "You win!😃"
  else:
    return "You lose😤"
  
def play_game():
  print(logo)
  game_over=False
  computer_cards = []
  user_cards=[]
  for _ in range(2):
    user_cards.append(deal_card())
    computer_cards.append(deal_card())
      
  while not game_over:
    user_score = calculate_score(user_cards)
    computer_score = calculate_score(computer_cards)
    print(f"Your cards:{user_cards} Your current score:{user_score}")
    print(f"Dealer's first card:{computer_cards[0]}")
    if user_score==0 or computer_score==0 or user_score > 21 :
      game_over=True
    else:
      draw = input('Do you want to draw another card? Y for yes , N for No: ').lower()
      if draw == 'y':
        user_cards.append(deal_card())
      else:
        game_over = True
        
  while computer_score != 0 and computer_score < 17:
    computer_cards.append(deal_card())
    computer_score = calculate_score(computer_cards)
  
  print(f"Your final hand is {user_cards} and final score is {user_score}")
  print(f"Dealer's final hand is {computer_cards} and final score is {computer_score}")
  print(compare(user_score, computer_score))
  

while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
  clear()
  play_game()