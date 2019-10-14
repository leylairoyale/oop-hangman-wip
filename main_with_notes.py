# remember to activate hangman-env
import random

# variables assigned outside of my classes.
wordlist = ['python', 'boa', 'victoria']
secret_word = list(random.choice(wordlist))
letter = " "

# class HangmanGameSet does everything to set up the game.
# class CLPrint will print things to the command line
# class PlayGame will take instances of everything to get it set up and running and is the game logic.
# class UserInput will handle the user inputs.
# class GameRules will handle the rules of the game.
class HangmanGameSet:

    def __init__(self, underscore, guesses_taken=0, guesses_left=8):
        self.underscore = underscore
        self.guesses_taken = guesses_taken
        self.guesses_left = guesses_left


class GameRules:

    def __init__(self):
    
    def is_letter(self, letter):
        self.letter = letter
        if str(letter).isalpha():
            return True
        else:
            print("That's not a letter. Letters only, please.")
            return False

    def is_not_multiple_chars(self, letter):
        self.letter = letter
        if len(letter) == 1:
            return True
        elif len(letter) > 1:
            if self.letter == "".join(secret_word):
                print("You've guessed the secret word! It was {}".format(letter.title()))
                Playing = False
            else:
                print("That's more than one letter! No go!")
                return False

    # here's a new version of is letter in word but returns true or false.
    def is_letter_in_word(self, letter):
        # self.letter = letter this says the instance letter you put in that's in hangsaman is being pulledin here
        # but you don't need that so you can just put letter as a variable that's pulled in
        # and don't bother with self.letter cause it's just letter entered here...brain melt you understand.
        return letter in secret_word
        # above is a statement that returns true or false so you don't need the other stuff.

    def replace_underscore_with_letter(self, letter):
        for l in range(len(secret_word)):
            if secret_word[l] == letter:
                self.underscore[l] = secret_word[l]
                self.underscore = " ".join(self.underscore)
            else:
                pass
        print(self.underscore)

    def change_underscore_from_list_to_string(self):
        pass

    def change_underscore_from_string_to_list(self):
        self.underscore = self.underscore.split()
        # self.underscore = list(self.underscore)
        # split already returns a list!!!

    def is_word_guessed(self, letter):
        self.letter = letter
        if self.letter == "".join(secret_word):
            print("You've guessed the secret word! It was {}".format(letter.title()))
            return True
        else:
            return False

        # pair this down by having a function that keeps track of guesses left 
    # and also another that does math to return the guesses taken.  
    def are_guesses_left(self):
        self.guesses_left -= 1
        self.guesses_taken += 1
        if self.guesses_left > 0:
            print("{} guesses left and {} taken.".format(self.guesses_left, self.guesses_taken))
        elif self.guesses_left == 0:
            print("You're out of guesses! The secret word was {}.".format("".join(secret_word)))     
            Playing = False

class CLPrint:

    def __init__(self):
        pass
    # think about naming this to be more descriptive. also, in general. 
    def print_underscore(self):
        for letter in range(len(secret_word)):
            self.underscore.append("_")
        self.underscore = " ".join(self.underscore)
        print(self.underscore + " is your word!")

class UserInput:

    def __init__(self):

    def guess_a_letter(self):
        letter = input("Guess a letter. ").strip().lower()
        print(letter)
        self.are_guesses_left()
        if self.is_letter(letter) and self.is_not_multiple_chars(letter):
            self.is_letter_in_word(letter)
        else:
            pass

# redefine this function to just check if in the word. put the print statement
# in the other class you'll create eventually later.
    # def is_letter_in_word(self, letter):
    #     self.letter = letter
    #     if letter in secret_word:
    #         self.underscore = self.underscore.split()
    #         self.underscore = list(self.underscore)
    #         for l in range(len(secret_word)):
    #             if secret_word[l] == letter:
    #                 self.underscore[l] = secret_word[l]
    #                 self.underscore = " ".join(self.underscore)
    #             else:
    #                 pass
    #     print(self.underscore)

        
# class Playing is the game logic.

class Playing:

    def __init__(self):
        pass


# hang = Hangsaman([], 0, 8)
# hang.print_underscore()
# while Playing:
#     hang.guess_a_letter()
#     if Playing == False:
#         break
    
        


# letter does not need to be an instance or global variable; you can just assign use and dump it every method you have.
# You could get rid of guesses left.

# Kes' thoughts:
# Break it out into multiple classes, so a class for pritning to the cl, a class for 
# handling game rules (is it one char, multiple, etc),
# a class to handle the user inputs for everything. 
# put the game logic as an object. 
# so you would create an instance of all the objects and pass them into the game logic class
# the init of the game logic class will take an instance of all the objects to pass in the __init__ of the 
# game logic classes. 
