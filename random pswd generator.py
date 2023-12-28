import random
print("Welcome to the random password generator !!")
randomchar="ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz123456789@#$&*"
number_of_password=int(input("Please enter the number of passwords to generated :"))
password_length=int(input("Enter the length of the password :"))


print("Here are your random passwords :")

for i in range(number_of_password):
    pwd=""
    for char in range(password_length):
        pwd=pwd+random.choice(randomchar)
    print(pwd)

print("\nThank You !!")
