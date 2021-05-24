logo = """
--[[
   _____                          _______  _             _   _                    _                 
  / ____|                        |__   __|| |           | \ | |                  | |                
 | |  __  _   _   ___  ___  ___     | |   | |__    ___  |  \| | _   _  _ __ ___  | |__    ___  _ __ 
 | | |_ || | | | / _ \/ __|/ __|    | |   | '_ \  / _ \ | . ` || | | || '_ ` _ \ | '_ \  / _ \| '__|
 | |__| || |_| ||  __/\__ \\__ \    | |   | | | ||  __/ | |\  || |_| || | | | | || |_) ||  __/| |   
  \_____| \__,_| \___||___/|___/    |_|   |_| |_| \___| |_| \_| \__,_||_| |_| |_||_.__/  \___||_|   
                                                                                                    
                                                                                                    
--]]
"""
print(logo)

import random

def hard_level():
  """For hard level"""
  attempt = 5
  while not attempt == 0:
    guess_number = int(input("Guess your number: "))
    if guess_number > choice_number:
      attempt -= 1
      print("Too high")
      print(f"Your attempt in current:{attempt}")
    elif guess_number < choice_number:
      attempt -= 1
      print("Too low")
      print(f"Your attempt in current:{attempt}")
    elif guess_number == choice_number:
      print("Great Guess")
      print(f"Your attempt in current:{attempt}")
      break
  print(f"The answer is {choice_number}")
  print("End game")

def easy_level():
  """For easy level"""
  attempt = 10
  while not attempt == 0:
    guess_number = int(input("Guess your number: "))
    if guess_number > choice_number:
      attempt -= 1
      print("Too high")
      print(f"Your attempt in current:{attempt}")
    elif guess_number < choice_number:
      attempt -= 1
      print("Too low")
      print(f"Your attempt in current:{attempt}")
    elif guess_number == choice_number:
      print("Great Guess")
      print(f"Your attempt in current:{attempt}")
      break
  print(f"The answer is {choice_number}")
  print("End Game")

# Game start
player = input("Welcome to guessing number game. Do you want to play game? Type 'y' or 'n': ")
game_play = True

if player == "y":  
  while game_play:
    choice_number = random.randint(1,100)
    #print(choice_number)
    if input("What's level do you want to play? Type 'easy' or 'hard': ") == 'easy':
      easy_level()
      if input("Do you want to continues? Type 'y' or n': ") == 'n':
        print("Thank you for playing")
        game_play = False
    else:
      hard_level()
      if input("Do you want to continues? Type 'y' or n': ") == 'n':
        print("Thank you for playing")
        game_play = False
else:
  game_play = False
  print("Thank you for comming!!!")
  