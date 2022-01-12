#!python3
"""
Create a function that creates a random choice for the computer player:
input parameters: none required
output:

0 : rock
1 : paper
2 : scissors
"""
import random
x = "Rock"
y = "Paper"
z = "Scissors"
def computerChoice():
  selection = random.randint(0,2)
  if selection == 0:
    return x
  if selection == 1:
    return y
  if selection == 2:
    return z
  
  
  return value


if __name__ == "__main__":
  computer = computerChoice()
  print(computer)
