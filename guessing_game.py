#Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).
import random
from replit import clear
from pic import logo 
answer = random.randint(1,100)
easy_level=10
hard_level=5
def game_level():
  level = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
  if level =="easy":
    return easy_level 
  else:
    return hard_level

def guessing(num,answer,remaining): 
  if num<answer:
    print("Too low.")
    return remaining-1 
  elif num>answer:
    print("Too high.")
    return remaining-1


def game(): 
  print(logo)
  print("Welcome to the Number Guessing Game!\nI'm thinking of a number between 1 and 100.") 
  remaining=game_level()
  num=0
  while num!=answer:
    print(f"You have {remaining} attempts remaining to guess the number.")
    num = int(input("Make a guess: ")) 
    remaining=guessing(num,answer,remaining)
    if remaining==0:
      print(f"You've run out of guesses, you lose.The answer is {answer}")
      break 
    if num==answer:
      print(f"You've got the answer. The answer is {answer}")
game()
while input("Play again? 'y' or 'n': ")=="y": 
  clear()
  game()