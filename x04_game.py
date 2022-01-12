#!python3

"""
Create a full rock paper scissors game
You can incorporate the other files in this project to help you
"""

from x01_player import *
from x02_computer import *
from x03_winner import *

x = "You Lose! Try Again"
y = "You Win Good Job!"
z = "Tie! Try Again"
def playerWins(computer,player):
  if player == 0 and computer == 1:
    return x
  if player == 0 and computer == 2:
    return y
  if player == 0 and computer== 0:
    return z
  if player == 1 and computer == 2:
    return x
  if player == 1 and computer==0:
    return y
  if player == 1 and computer==1:
    return z
  if player == 2 and computer == 0:
    return x
  if player == 2 and computer== 1:
    return y
  if player == 2 and computer== 2:
    return z

if __name__ == "__main__":
  output = playerWins(1,1)
  print(output)