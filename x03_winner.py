#!python3

'''
Create a function that takes 2 input parameters:
int: computer choice
int: player choice

the choices correspond to:
0: rock
1: paper
2: scissors

Based on the classic rules for Rock Paper Scissors, the return value should be an integer value that indicates if the player is the wins, loses or ties
Output:
-1: player loses
0: tie
1: player wins
'''
x = -1
y = 0
z = 1
def playerWins(computer,player):
  if player == 0 and computer == 1:
    return x
  if player == 0 and computer == 2:
    return z
  if player == 0 and computer== 0:
    return y
  if player == 1 and computer == 2:
    return x
  if player == 1 and computer==0:
    return z
  if player == 1 and computer==1:
    return y
  if player == 2 and computer == 0:
    return x
  if player == 2 and computer== 1:
    return z
  if player == 2 and computer== 2:
    return y
  return 0

if __name__ == "__main__":
  assert playerWins(1,1) == 0
  assert playerWins(1,0) == -1
  assert playerWins(1,2) == 1
  assert playerWins(2,1) == -1
  
