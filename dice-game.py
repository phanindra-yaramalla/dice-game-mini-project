import random

while True:
    user_choice=input("Roll the Dice(y/n) : " )
    if user_choice == "y" or user_choice == "Y":
        dice1= random.randint(1,6)
        dice2= random.randint(1, 6)
        print(f"Dice1 : {dice1}\nDice2 : {dice2}")
    elif user_choice=="n" or user_choice=="N":
        print("Thanks for Playing")
        break
    else:
        print("Invalid Choice")
