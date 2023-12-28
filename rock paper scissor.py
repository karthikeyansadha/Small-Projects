import random

choice=["rock","paper","scissors"]
computer = random.choice(choice)

user_input=None
while user_input not in choice:
    user_input=input("Rock, Paper, scissors ? :").lower()

if (computer == user_input):
    print("Player : ",user_input)
    print("Computer : ",computer)
    print("Tie !")

elif user_input == "rock" :

     if(computer=="paper"):
            print("Player : ",user_input)
            print("Computer : ",computer)
            print("You lose !")
     if(computer=="scissors"):
            print("Player : ",user_input)
            print("Computer : ",computer)
            print("You won !")

elif(user_input=="paper"):

     if(computer=="rock"):
            print("Player : ",user_input)
            print("Computer : ",computer)
            print("You won !")
     if(computer=="scissors"):
            print("Player : ",user_value)
            print("Computer : ",computer)
            print("You lose !")

elif(user_input=="scissors"):

     if(computer=="paper"):
            print("Player : ",user_input)
            print("Computer : ",computer)
            print("You Won !")
     if(computer=="rock"):
            print("Player : ",user_input)
            print("Computer : ",computer)
            print("You lose !")
