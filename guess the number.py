import random
EASY_LEVEL_ATTEMPTS = 10
HARD_LEVEL_ATTEMPTS = 5



logo = """
  ________                                         __   .__                                            ___.                    
 /  _____/  __ __   ____    ______  ______       _/  |_ |  |__    ____           ____   __ __   _____  \_ |__    ____  _______ 
/   \  ___ |  |  \_/ __ \  /  ___/ /  ___/       \   __\|  |  \ _/ __ \         /    \ |  |  \ /     \  | __ \ _/ __ \ \_  __ \
\    \_\  \|  |  /\  ___/  \___ \  \___ \         |  |  |   Y  \\  ___/        |   |  \|  |  /|  Y Y  \ | \_\ \\  ___/  |  | \/
 \______  /|____/  \___  >/____  >/____  > ______ |__|  |___|  / \___  > ______|___|  /|____/ |__|_|  / |___  / \___  > |__|   
           

        """
def set_difficulty(level):
    if level == "easy":
        return  EASY_LEVEL_ATTEMPTS
    elif level == "hard":
        return HARD_LEVEL_ATTEMPTS
    else:
        return

def check_answer(guessed_number,answer,attempts):
    if guessed_number > answer:
        print("Your guess is Too high, try to low")
        return attempts-1
    elif guessed_number < answer:
        print("Your guess is Too low, try to high")
        return attempts-1
    else:
        print(f"Your guessed number is correct and number is{answer} ")
def game():
    print(logo)
    print("Let you think of a number between 1 to 50.")
    answer = random.randint(1,50)
    level=input("choose level of difficulty..Type 'Easy' or 'Hard' :").lower()
    attempts = set_difficulty(level)
    if attempts!=EASY_LEVEL_ATTEMPTS and attempts!=HARD_LEVEL_ATTEMPTS:
        print("Wrong Information")
        return
    guessed_number = 0
    while guessed_number != answer:
        print(f"You have {attempts} remaining to guess the number")
        guessed_number=int(input("guess a number :"))
        attempts = check_answer(guessed_number,answer,attempts)

        if attempts == 0:
            print("You are out of guess...You loose!")
            return
        elif guessed_number != answer:
            print("Guess again")
game()
