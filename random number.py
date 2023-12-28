# Description - creating a random value from (1-6) and we add each value
# except 1 . If we get the value 1 all the value added remains to zero
# as the same way who reches 50 is the winner


import random

def roll():
    min_value=1
    max_value=6
    roll=random.randint(min_value,max_value)
    return roll

while True:
    players = input("enter the number of players (2-4): ")
    if players.isdigit():
        players=int(players)
        if players>=2 and players<=4:
            break
        else:
            print("enter the values between (2-4) ")
    else:
        print("Invalid try again")


max_score=50
player_score=[0 for _ in range(players)]
while max(player_score) < max_score:

    for player_idx in range(players):
        print("\nplayer number",player_idx+1,"turn has just started")
        print(("Your total score is:",player_score[player_idx],"\n"))
        current_score=0

        while True:
            should_roll=input("Would you like to roll(y) ?")
            if should_roll.lower() != "y":
                break
            value=roll()
            if value==1:
                print("You rolled 1!, Your turn done")
                current_score=0
                break
            else:
                current_score  +=value
                print("you rolled a",value)

            print("your score is ", current_score)

        player_score[player_idx] += current_score
        print("your total score is ",player_score[player_idx])

max_score=max(player_score)
winning=player_score.index(max_score)
print("Player number",winning+1,
      "is the winner with a score of :",max_score)
