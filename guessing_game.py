
import random 
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
  game()
