print("Welcome to the Quiz Game")
player = input("Do you want to play the game ? :")
if player.lower() != "yes":
    print("Thank you")
    quit()
print("ok!,Lets play")

score = 0

question1=input("How many days in a week :")
if question1.lower()=="seven" or question1 == "7":
    print("You are correct")
    score +=1
else:
    print("You are wrong")


question1=input("sun rises in :")
if question1.lower()=="east":
    print("You are correct")
    score +=1
else:
    print("You are wrong")

question1=input("What is india's National bird :")
if question1.lower()=="peacock":
    print("You are correct")
    score +=1
else:
    print("You are wrong")


question1=input("largest ocean in the world :")
if question1.lower()=="pacific ocean":
    print("You are correct")
    score +=1
else:
    print("You are wrong")

print("Your score is :",score)



