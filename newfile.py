import random
def get_choices():
  player_choice = input("input a choice (rock paper or scissors):")
  options=["rock","paper","scissors"]
  computer_choice = random.choice(options)
  choices = {"player": player_choice,"computer": computer_choice}
  return choices
  
def check_win(player,computer) : 
  print(f"your choice {player}, conputer's choice {computer}")
  if player == computer :
     print("its a tie")
  elif player == "rock":
      if computer =="paper":    
        print("you win")
      else :
        print("you lose")    
  elif player == "scissors":
      if computer =="paper":    
        print("you win")
      else :
        print("you lose") 
  elif player == "paper":
      if computer =="rock":    
        print("you win")
      else :
        print("you lose") 
choices = get_choices()
result = check_win(choices ["player"], choices ["computer"])
