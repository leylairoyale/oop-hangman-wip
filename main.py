# remember to activate hangman-env
import random


# class HangmanGameSet does everything to set up the game.
# class CLPrint will print things to the command line
# class PlayGame will take instances of everything to get it set up and running and is the game logic.
# class UserInput will handle the user inputs.
# class GameRules will handle the rules of the game.
class HangmanGameSet:

    def __init__(self, underscore=[], secret_word=""):
        self.underscore = underscore
        self.secret_word = secret_word

    def set_secret_word(self):
        wordlist = ['python', 'boa', 'victoria']
        self.secret_word = list(random.choice(wordlist))

    def set_letter_underscores_for_secret_word(self):
        for letter in range(len(secret_word)):
            self.underscore.append("_")
        self.underscore = " ".join(self.underscore)

class UserInput:

    def __init__(self):
        pass

    def guess_a_letter(self):
        letter = input("Guess a letter. ").strip().lower()
        
class GameRules:

    def __init__(self, guesses_left=8):
        self.guesses_left = guesses_left
    
    def is_letter(self, letter):
        if str(letter).isalpha():
            print("true")
            return True
        else:
            print("false")
            return False

    def is_not_multiple_chars(self, letter):
        if len(letter) == 1:
            print("it's 1 char")
            return True
        elif len(letter) > 1:
            if letter == "".join(secret_word):
                print("correct guess")
                return True
            else:
                print("That's more than one letter! No go!")
                return False

    def is_letter_in_word(self, letter):
        return letter in secret_word
        # above is a statement that returns true or false so you don't need the other stuff.

    def replace_underscore_with_letter(self, letter):
        self.underscore = self.underscore.split()
        for l in range(len(HangmanGameSet.secret_word)):
            if HangmanGameSet.secret_word[l] == letter:
                HangmanGameSet.underscore[l] = secret_word[l]
                self.underscore = " ".join(self.underscore)
            else:
                pass

    def change_underscore_from_list_to_string(self):
        pass

    def are_guesses_left(self):
        self.guesses_left -= 1
        if self.guesses_left > 0:
            return True
        else:
            return False

    def how_many_guesses_have_been_taken(self):
        return self.guesses_left - 8


class CLPrint:

    def __init__(self):
        pass
    # think about naming this to be more descriptive. also, in general. 
    def print_underscore(self):
        print(self.underscore + " is your word!")

        
# class Playing is the game logic.

class Playing:

    def __init__(self):
        pass
        

    def is_letter_guessed_in_word(self):
        # more code goes here
        if self.is_letter(letter) and self.is_not_multiple_chars(letter):
            self.is_letter_in_word(letter)
        else:
            pass


testing = UserInput()
testing2 = GameRules()
letter = testing.guess_a_letter()
print(type(letter))
testing2.is_letter(letter)
testing2.is_not_multiple_chars(letter)
testing2.is_letter_in_word(letter)


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
