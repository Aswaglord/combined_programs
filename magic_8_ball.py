import random

random_number = random.randint(1,8)
user_question = input("Ask the 8 ball a question: (press enter to quit)")

if user_question == "":
    quit("program terminated")

if random_number == 1:
    print("Outlook good")
elif random_number == 2:
    print("You may rely on it")
elif random_number == 3:
    print("Ask again later")
elif random_number == 4:
    print("Concentrate and ask again")
elif random_number == 5:
    print("Reply hazy, try again")
elif random_number == 6:
    print("My reply is no")
elif random_number == 7:
    print("It is certain")
else:
    print("My sources say no")