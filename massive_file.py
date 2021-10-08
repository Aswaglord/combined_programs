import os

program_running = True

def menu():
    print("""
(B)inary Calculator
(P)ython Bank
(C)oin flip
(M)agic 8 ball
(H)angman
(N)umber game
(Q)uit
    """)

while program_running:

    menu()
    choice = input("what program would you like to run? ").upper()

    if choice == "P":
        os.system("Bank_of_python.py")
    elif choice == "C":
        os.system("coin_flip.py")
    elif choice == "M":
        os.system("magic_8_ball.py")
    elif choice == "H":
        os.system("hangman.py")
    elif choice == "N":
        os.system("number_game.py")
    elif choice == "B":
        os.system("binary_calculator.py")
    elif choice == "Q":
        quit()
    else:
        print("character does not exist")
        
os.system("massive_file.py")



