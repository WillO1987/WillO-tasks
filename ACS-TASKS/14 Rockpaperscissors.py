import pygame
from random import  randint

choices = ["Rock", "Paper", "Scissors"]


computer = choices[randint(0,2)] # computer randomly picks rock paper or scissors



player = input("Rock, Paper, Scissors?")
if player == computer:
    print("Tie!")
elif player == "Rock":          # if statements for game logic
    if computer == "Paper":
        print("You lose!", computer, "covers", player)
    else:
        print("You win!", player, "smashes", computer)
elif player == "Paper":
    if computer == "Scissors":
        print("You lose!", computer, "cut", player)
    else:
        print("You win!", player, "covers", computer)
elif player == "Scissors":
    if computer == "Rock":
        print("You lose...", computer, "smashes", player)
    else:
        print("You win!", player, "cut", computer)
else:
    print("That's not a valid play. Check your spelling!")
#endiif