import random

number_of_flips = int(input("how many times would you like to flip the coin?"))

def coin_flip(number_of_flips):
    for x in range(number_of_flips):
        random_number = random.randint(1,2)
    if random_number == 1:
        print("Heads")
    else: 
        print("Tails")

coin_flip(number_of_flips)