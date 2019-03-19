"""
This is the solution for the Project #2: Hangman

"""

import re
import time
from consoleInteractor import ConsoleInteractor
from pygameInteractor import PyGameInteractor


class Hangman(object):
    def __init__(self, interactor, noOfChances):
        self.interactor = interactor
        self.chances = noOfChances

    def play(self):
        close = False
        maxLength = 30

        while(not close):
            success = False
            remainingChances = self.chances

            # Clear the interactor
            self.interactor.clearDisplay()

            # Get the input from Player 1
            quizWord = Hangman.validateInputWord(
                str(self.interactor.getInputWord(maxLength)), maxLength)

            if(quizWord is None):
                continue
            elif(str(quizWord).upper() == "QUIT"):
                close = True
                continue

            puzzleWord = Hangman.formulatePuzzle(quizWord, None, None)
            incorrectRespones = []
            self.updateDisplay(
                puzzleWord, incorrectRespones, remainingChances)

            while(remainingChances > 0 and not success):
                self.updateDisplay(
                    puzzleWord, incorrectRespones, remainingChances)
                # get the input from Player 2
                letter = Hangman.validateInputLetter(
                    str(self.interactor.getAnswerLetter()))

                time.sleep(0.5)
                if(letter is None):
                    # instruct the interactor to update display based on user
                    #  input
                    continue
                elif(quizWord.__contains__(letter)):
                    puzzleWord = self.formulatePuzzle(
                        quizWord, puzzleWord, letter)
                elif(incorrectRespones.__contains__(letter)):
                    continue
                else:
                    remainingChances -= 1
                    incorrectRespones.append(letter)
                if(not puzzleWord.__contains__("_")):
                    success = True

            # instruct the interactor to update display based on user input
            self.updateDisplay(puzzleWord, incorrectRespones, remainingChances)

            time.sleep(3)
            self.interactor.clearDisplay()
            self.interactor.displayEndMessage(
                success, self.chances, remainingChances)
            time.sleep(3)

    def updateDisplay(self, puzzleWord, incorrectRespones, remainingChances):
        self.interactor.clearDisplay()
        self.interactor.updateDisplay(puzzleWord, self.chances,
                                      incorrectRespones,
                                      remainingChances)

    @staticmethod
    def validateInputLetter(letter):
        try:
            if(len(letter) > 1 or letter.isspace()):
                return None
            else:
                return letter
        except:
            return None

    @staticmethod
    def validateInputWord(word, maxLength):
        try:
            if(len(word) > maxLength):
                return None
            word = re.sub(" +", " ", word)
            if(word.replace(" ", "").isalnum()):
                return word.strip()
            else:
                return None
        except:
            return None

    @staticmethod
    def formulatePuzzle(word, puzzleWord, letter):
        puzzle = ""
        for index, character in enumerate(word):
            if(character == " "):
                puzzle += ' '
            elif(character == letter):
                puzzle += letter.upper()
            elif(puzzleWord is not None):
                puzzle += puzzleWord[index]
            else:
                puzzle += '_'
        return puzzle


def main():
    # interactor = ConsoleInteractor()
    interactor = PyGameInteractor()
    game = Hangman(interactor, 7)
    game.play()


main()
