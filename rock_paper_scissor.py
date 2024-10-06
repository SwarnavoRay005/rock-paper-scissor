import random

options=['rock','paper','scissor']
userInput=0

while userInput not in options:
    userInput=input("enter the choice (rock,paper,scissor) or press q to exit:").lower()
    if userInput=='q':
        print("Exiting......")
        break

    if userInput not in options: # checks whether the updated userInput is in the options or not
        print("Invalid input. Please choose again.")
        continue

    computer_choice=random.choice(options)

    print(f"User-Input : {userInput}")
    print(f"Computer-Input : {computer_choice}")

    if userInput==computer_choice:
        print("It is a tie")
    elif(userInput=='rock' and computer_choice=='scissor'):
        print("You Win!")
    elif(userInput=='paper' and computer_choice=='rock'):
        print("You Win!")
    elif(userInput=='scissor' and computer_choice=='paper'):
        print("You Win!")
    else:
        print("You Lose!!!")

    
