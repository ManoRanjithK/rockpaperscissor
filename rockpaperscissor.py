import random as r


items = ["Rock", "Paper", "siccosor","exit"]
computer = items[r.randint(0, 2)]
computerWon = 0

playerWon = 0
player = False

tie = 0
temp = 0

while player == False:
    player = items[int(input("enter either 0 or 1 or 2 or 3 to exit \t"))]
    if player == "Rock":
        if computer == "Paper":
            computerWon += 1
            print("Sorry Buddy,The Computer Won ",player, "by", computer)
        elif computer == "Rock":
            print("tie")
            tie += 1
        else:
            playerWon += 1
            print("Congratulations, Player won ", computer, "by", player)
    elif player == "Paper":
        if computer == "Siccosor":
            computerWon += 1
            print("Your Bad Luck, Computer Won ",player, "by", computer)
        elif computer == "Paper":
            print("tie")
            tie += 1
        else:
            playerWon += 1
            print("Im the king of the world, Player won ", computer, "by", player)
    elif player == "siccosor":
        if computer == "Rock":
            computerWon += 1
            print("Im gonna take over the world, Computer Won ", player, "by", computer)
        elif computer == "Siccosor":
            print("tie")
            tie += 1
        else:
            playerWon += 1
            print("Guess You Ha Ha, Player won ", computer, "by", player)
    elif player == "exit":
        break
    else:
            print("Invalid number only 0 or 1 or 2 else GET LOST")
    player = False
    computer = items[r.randint(0, 2)]

print("player Scored ", playerWon)
print("computer scored", computerWon )
print("ties", tie)


