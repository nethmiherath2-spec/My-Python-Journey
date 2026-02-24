pin = 1234
user_input = int(input("Enter Your PIN :"))

if user_input == pin :
    print("Welcome! You come in.")
else:
    print("Wrong This PIN!")

balance = 5000
withdraw = int(input("How many to take? :"))
if withdraw <= balance:
    balence = balance - withdraw
    print("Got the money! The rest is up : " , balance)
else:
    print("Not enough money")