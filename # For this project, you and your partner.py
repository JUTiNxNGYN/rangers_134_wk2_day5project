#Rock Paper Scissor Generator

# For this project, you and your partner(s) will work to create a program that has a "player" and a "computer" adversary.
# The computer should randomly choose its decision based on a list of actions it can take ("Rock", "Paper" or "Scissors"). 
# The player should then have a chance to input their decision. 


def rps(p1, p2):
    beats = {'rock': 'scissors', 'scissors': 'paper', 'paper': 'rock'}
    if beats [p1] == p2:
        return "Player 1 won!"
    if beats [p2] == p1:
        return "Player 2 won!"
    return "Draw!"

def rock_paper_scissor(p, c):
  #  if rock > scissor = rock (wins)
  #  if rock < paper = paper (wins)
  #  if scissor < rock = rock (wins)
  # if scissor > paper = scissor (wins)
  # if paper > rock = paper (wins)
  # if paper < scissor = scissor (wins)