#This is the Python file the Week 02
import random
choices = ["Rock", "Paper", "Scissors"]
playerChoice = input("Enter your choice (1=Rock, 2=Paper, 3=Sciccors): ")
playerChoice = int(playerChoice)
if playerChoice < 1 or playerChoice > 3:
    print("Error: Choice must be between 1 and 3!")
else:
    computerChoice = random.randint(1, 3)

    playerChoiceIndex = choices[playerChoice -1]
    computerChoiceIndex = choices[computerChoice -1]
    print("You choose: ", playerChoiceIndex)
    print("Computer choose: ", computerChoiceIndex)

    #Determine the winner using if/elseif/else
    if playerChoiceIndex == computerChoiceIndex:
        print("It's a tier")
    elif playerChoice == 0 and playerChoiceIndex == 2:
        print("Rock beats Scissorts - You win!")
    elif playerChoice == 1 and playerChoiceIndex == 0:
        print("Paper beats Rock - You win!")
    elif playerChoice == 2 and playerChoiceIndex == 1:
        print("Rock beats Paper} - You win!")
    else:
        print("You lose!")