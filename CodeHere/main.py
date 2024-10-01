import random

def main():
    start = input("Start new game? (y/n): ")
    if start == "y":
        game()
    elif start == "n":
        return 0
    else:
        print("Invalid")
        return main()

def game():
    string = ["rock", "paper", "scissors"]
    print("\nRock, Paper, Scissors")
    userin = input("\nEnter your choice: ")
    compinput = random.choice(string)

    if userin == "rock" and compinput == "scissors":
        print("User: Rock \nComputer: Scissors\nUser Wins\n")
        main()
    elif userin == "rock" and compinput == "paper":
        print("User: Rock \nComputer: Paper\nComputer Wins\n")
        main()
    elif userin == "rock" and compinput == "rock":
        print("User: Rock \nComputer: Rock\nDraw\n")
        main()
    elif userin == "paper" and compinput == "scissors":
        print("User: Rock \nComputer: Scissors\nComputer Wins\n")
        main()
    elif userin == "paper" and compinput == "paper":
        print("User: Paper \nComputer: Paper\nDraw\n")
        main()
    elif userin == "paper" and compinput == "rock":
        print("User: Paper \nComputer: Rock\nUser Wins\n")
        main()
    elif userin == "scissors" and compinput == "scissors":
        print("User: Rock \nComputer: Scissors\nDraw\n")
        main()
    elif userin == "scissors" and compinput == "paper":
        print("User: Scissors \nComputer: Paper\nUser Wins\n")
        main()
    elif userin == "scissors" and compinput == "rock":
        print("User: Scissors \nComputer: Rock\nComputer Wins\n")
        main()
    else:
        print("Invalid")
        main()


main()