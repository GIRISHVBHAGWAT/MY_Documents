print("hari om")
bn = int(input("Enter A number begin :"))
en = int(input("Enter A number End"))
list_of_user_numbers = []
for i in range(bn,en):
    list_of_user_numbers.append(i)

import random
random_number = random.choice(list_of_user_numbers)
while(True):
    user_guess = int(input("Guess The Number:"))

    if user_guess<random_number:
        print("Guess Heigh Number")
        if user_guess in list_of_user_numbers:
            list_of_user_numbers.remove(user_guess)

    elif user_guess>random_number :
        print("Guess Low Number")
        if user_guess in list_of_user_numbers:
            list_of_user_numbers.remove(user_guess)

    elif user_guess==random_number:
        print("You'r Guess Is Currect !!!")
        quit()


    print(random_number-user_guess)