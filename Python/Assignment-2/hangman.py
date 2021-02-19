#HANGMAN code python

from words import word_list
from random import choice,sample,randint
import os
from time import sleep


class Hangman():  ## Define the Hangman class
    def __init__(self) -> None:
        self.hangman_states = stages = [  # final state: head, torso, both arms, and both legs
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / \\
                   -
                """,
                # head, torso, both arms, and one leg
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / 
                   -
                """,
                # head, torso, and both arms
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |      
                   -
                """,
                # head, torso, and one arm
                """
                   --------
                   |      |
                   |      O
                   |     \\|
                   |      |
                   |     
                   -
                """,
                # head and torso
                """
                   --------
                   |      |
                   |      O
                   |      |
                   |      |
                   |     
                   -
                """,
                # head
                """
                   --------
                   |      |
                   |      O
                   |    
                   |      
                   |     
                   -
                """,
                # initial empty state
                """
                   --------
                   |      |
                   |      
                   |    
                   |      
                   |     
                   -
                """
        ]

    def get_word(self) -> str:
        """
        returns a random word at random

        Returns:
            str: random word
        """        
        #return str(choice(word_list).upper())
        return "ANONYMOUS"

    def display_state(self,tries : int,word_completion_state : list) -> None:
        """
        This Function printes the current state of hangman with
        some preset messages as well as print the remaining tries

        Args:
            tries ([int]): Number of tries remaining 
            word_completion_state ([list]): The current state of the hidden character
                                            in the word
        """        
        print(f"{'-' * 20}HANGMAN{ '-' * 20}\n\n")
        print(self.hangman_states[-(tries+1)] + "\n")
        print(f"WORD ------> {' '.join(word_completion_state)}")
        print(f"Tries Remaining : {tries}")        


    def play_hangman(self) -> None:
        """
        Initiates a game of hangman
        Use has 6 tries to complete the word selected at random
        after tries run out or word is guessed , display a win
        or loss message and exit the game
        """        
        tries=6
        current_word=self.get_word()
        guessed_word = False
        word_hidden_states = [current_word[indx] for indx in sample(range(0, len(current_word)-1), randint(1, len(current_word)-2))]
        word_completion_state = [letter if letter not in word_hidden_states else "_" for letter in current_word]

        while tries > 0 and not guessed_word: 
            os.system('cls' if os.name == 'nt' else 'clear') ## Clear the terminal for new lines to be printed
            self.display_state(tries,word_completion_state)
            guessed_char=str(input("Guess a Character : ")).upper()

            if guessed_char in word_hidden_states :
                print("\nCorrect Guess !!!!!! Updating..........")
                for indx,_ in enumerate(word_completion_state) : 
                    if guessed_char == current_word[indx]:
                        word_completion_state[indx]=guessed_char
                
                word_hidden_states = [char for char in word_hidden_states if char != guessed_char]
                guessed_word = False if "_" in word_completion_state else True
                sleep(5)
            else :
                print("\nIncorrect Guess!!! Updating!!!!!!")
                sleep(5)
                tries=tries-1
        
        if tries == 0 and not guessed_word:
            os.system('cls' if os.name == 'nt' else 'clear') ## Clear the terminal for new lines to be printed
            print(f"{'-' * 20}HANGMAN{ '-' * 20}\n\n")
            print(self.hangman_states[-1] + "\n")
            print(f"No Tries Remaining , YOU LOST !!!!!")
            print(f"CORRECT WORD was ------> {current_word}")
            print(f"GAME OVER")
        
        if guessed_word:
            os.system('cls' if os.name == 'nt' else 'clear') ## Clear the terminal for new lines to be printed
            print(f"{'-' * 20}HANGMAN{ '-' * 20}\n\n")
            print(self.hangman_states[-tries] + "\n")
            print(f"YOU GUESSED THE WORD CORRECTLY !!!")
            print(f"WORD was ------> {current_word}")
            print(f"Congratulations You win")


if __name__ == "__main__":
    hangman=Hangman()
    continue_choice='y'
    while continue_choice == 'y':
        hangman.play_hangman()

        continue_choice=str(input("Do you want to play another game (Y/n) : "))
        os.system('cls' if os.name == 'nt' else 'clear') ## Clear the terminal for new lines to be printed

