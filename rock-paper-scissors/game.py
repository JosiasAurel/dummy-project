
#Rock, paper, scissors game for Glen to learn ;)

"""
A rock, paper, scissors game has three options (You know them)
- There is a possibilty the game goes on as follows :
{
    rock -> paper
    scissors -> rock
    paper -> scissors
}
As such, the number of possibilies for each option is 3! or 6
This therefore means that there is a total of 18 conditions to write in order to cover the probabilty
"""

import random

# The Rock, Paper, Scissors function to handle the game
def _rock_paper_scissors(player_option, pc_option):
  
    pc = pc_option.lower()
    player = player_option.lower()

    #Rock constraints
    if player == "rock" and pc == "rock":
            return (f"Result : Draw \n Player:{player} \n Computer:{pc} ")
    elif player == "rock" and pc == "paper":
            return (f"Result : You Lose \n Player:{player} \n Computer:{pc} ")
    elif player == "rock" and pc == "scissors":
            return (f"Result : You Win \n Player:{player} \n Computer:{pc} ")
            
    #Paper constraints
    elif player == "paper" and pc == "rock":
            return (f"Result : You Win \n Player:{player} \n Computer:{pc} ")
    elif player == "paper" and pc == "paper":
            return (f"Result : Draw \n Player:{player} \n Computer:{pc} ")
    elif player == "paper" and pc == "scissors":
            return (f"Result : You Lose \n Player:{player} \n Computer:{pc} ")
            
    #Scissors Constraints
    elif player == "scissors" and pc == "rock":
            return (f"Result : You Lose \n Player:{player} \n Computer:{pc} ")
    elif player == "scissors" and pc == "paper":
            return (f"Result : You Win \n Player:{player} \n Computer:{pc} ")
    elif player == "scissors" and pc == "scissors":
            return (f"Result : Draw \n Player:{player} \n Computer:{pc} ")
    else:
        return ("Unknown Choice")                
    
    return "Terminated"
            

#Choices the computer can pick from
choices = ["Rock", "paper", "Scissors"]

def game():
    while True:
         print("welcome to rock paper scissors game by Josias Aurel") #You can change the name ;)
         print("You have to chose between rock, paper or scissors when prompted to. Do not worry about the character caes, the game takes care of that")
         user = input("Enter rock, paper or scissors : ")
         comp = random.choice(choices)
     
         print( _rock_paper_scissors(user, comp))
         print("Done")
                     
         break
 

game() 
    
