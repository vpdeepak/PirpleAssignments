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
        quit = False
        maxLength = 30

        while(not quit):
            success = False
            remainingChances = self.chances

            # Clear the interactor
            self.interactor.clearDisplay()

            # Get the input from Player 1
            quizWord = self.validateInputWord(
                str(self.interactor.getInputWord(maxLength)), maxLength)

            if(quizWord is None):
                continue
            elif(str(quizWord).upper() == "QUIT"):
                quit = True
                continue

            puzzleWord = self.formulatePuzzle(quizWord, None, None)
            incorrectRespones = []
            self.updateDisplay(
                puzzleWord, incorrectRespones, remainingChances)

            while(remainingChances > 0 and not success):
                self.updateDisplay(
                    puzzleWord, incorrectRespones, remainingChances)
                # get the input from Player 2
                letter = self.validateInputLetter(
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

    def validateInputLetter(self, letter):
        if(len(letter) > 1 or letter.isspace()):
            return None
        else:
            return letter

    def validateInputWord(self, word, maxLength):
        if(len(word) > maxLength):
            return None
        word = re.sub(" +", " ", word)
        if(word.replace(" ", "").isalnum()):
            return word.strip()
        else:
            return None

    def formulatePuzzle(self, word, puzzleWord, letter):
        puzzle = ""
        for ch in range(0, len(word)):
            if(word[ch] == " "):
                puzzle += ' '
            elif(word[ch] == letter):
                puzzle += letter.upper()
            elif(puzzleWord is not None):
                puzzle += puzzleWord[ch]
            else:
                puzzle += '_'
        return puzzle


def main():
    # interactor = ConsoleInteractor()
    interactor = PyGameInteractor()
    game = Hangman(interactor, 5)
    game.play()


main()
