import random

random_number = random.randint(1,100)
number_guessed = False
tries = 0
user_guess = int(input("what is your guess?"))

while number_guessed == False:
    if tries == 9:
        print("YOU LOSE:(")
        number_guessed = True

    elif user_guess == random_number:
        print(f"congrats you guessed right! it only took you {tries+1}")
        number_guessed = True
        quit()

    elif user_guess > random_number:
        user_guess = int(input("your guess was to high, guess again"))
        tries += 1
    else:
        user_guess = int(input("you guess was to low, guess again."))
        tries += 1