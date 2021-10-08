import random

class hangman():

    def __init__(self):
        self.random_word = ""
        self.guesses = 0
        self.limit = 10
        self.guessed_letters = []
        self.secret_word = ""


    def get_random_word(self):
        with open("hangman_words.txt") as f:
            words = []
            for word in f:
                words.append(word[:-1])
        random_number = random.randint(0,len(words))
        self.random_word = words[random_number]
        self.secret_word = "_" * len(self.random_word)

    def guess_letter(self, letter):
        if letter in self.random_word:
            for i in range(len(self.random_word)):
                if self.random_word[i] == letter:
                    self.secret_word = self.secret_word[:i] + letter + self.secret_word[i + 1:] 
        else:
            self.guessed_letters += letter
            self.guesses += 1

    def start_game(self):
        self.get_random_word()
        
        while self.guesses != self.limit:
            print('ALREADY GUESSED:' + str(self.guessed_letters) + '\n\n' + self.secret_word + '\n\n')
            self.guess_letter(input('guess a letter:'))
            if self.random_word == self.secret_word:
                print("CONGRATS YOU WIN!!!")
                break       
            print("\n\n\n\nsorry you lose, the word was: " + self.random_word)


hangman().start_game()
