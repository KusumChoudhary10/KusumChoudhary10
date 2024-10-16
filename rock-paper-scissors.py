It is a simple rock-paper-scissors game in python!!

import random

def play():
    user = input("what is your choice? 'r' for rock, 'p' for paper and 's' for scissors\n")
    computer = random.choice(["r","p","s"])

    if user == computer:
        return "It is a tie!"
    
    if is_win(user,computer):
        return "Hurray!, you win"
    
    return "You lost :("
    

def is_win(player,opponent):
    if (player =="r" and opponent == "s") or (player == "p" and opponent == "r") or (player == "s" and opponent == "p"):
        return True
    
print(play())

I hope you like it !! 
:)
