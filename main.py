import random

def main():
    print ("Welcome to Stanley's Rock Paper Scissors game!")

    while True:   
        userchoice = input("Choose between rock, paper, or scissors: ")
        
        possiblechoice = ("rock","paper","scissors")
        computerchoice = random.choice(possiblechoice)
        
        if userchoice == computerchoice:
            print("Both selected " + computerchoice + ". It's a tie!")
        elif userchoice == 'rock':
            if computerchoice == 'scissors':
                print("Rock crushes scissors, you won! :) ")
            else :
                print("Paper covers rock, you lost. :( ")
        elif userchoice == 'paper':
            if computerchoice == 'rock':
                print("Paper covers rock, you won! :) ")
            else :
                print("Scissors cuts paper, you lost. :( ")
        elif userchoice == 'scissors':
            if computerchoice == 'paper':
                print("Scissors cuts paper, you won! :) ")
            else :
                print("Rock crushes scissors, you lost. :( ")
        play_again = input("Play again? (y/n): ")
        if play_again.lower() != "y":
            break
main()  
