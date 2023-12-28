import random
import os
from higher_lower_DB import *
print(game_logo)
score=0
def display_accountinfo(account):
    name=account["name"]
    description=account["description"]
    country=account["country"]
    return f"{name}, a {description}, from {country}"

def check_answer(guess,fc1,fc2):
    if fc1<fc2:
        if guess == 1:
            return False
        else:
            return True
    else:
        if guess == 1:
            return True
        else:
            return False
account_2=random.choice(data)
continue_flag = True
while continue_flag:
    account_1 = account_2
    account_2 = random.choice(data)
    while account_1 == account_2:
        account_2 = random.choice(data)

    print(f"Compare 1: {display_accountinfo(account_1)}")
    print(f"{vs}")
    print(f"Compare 2: {display_accountinfo(account_2)}\n")
    guess=int(input("who has more followers ?, Type 1 or 2 :"))
    followers_count_1 = account_1["follower_count"]
    followers_count_2 = account_2["follower_count"]
    is_correct = check_answer(guess,followers_count_1,followers_count_2)
    os.system('cls')
    print(game_logo)
    if is_correct == True:
        score += 1

        print("You are right and your score is :",score)

    else:
        print("You are wrong..your final score is : ",score)
        continue_flag = False
