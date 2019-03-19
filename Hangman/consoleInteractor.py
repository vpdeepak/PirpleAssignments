from abstractInteractor import Interactor


class ConsoleInteractor(Interactor):

    def clearDisplay(self):
        super().clearDisplay()

    def getInputWord(self, maxLength):
        word = str(
            input(f"Please enter the input word (max length {maxLength}): "))
        return word

    def updateDisplay(self, word, chances, incorrectRespones,
                      remainingChances):
        for count in range(0, len(word)):
            print(word[count] + " ", end="")
        print(f"\n {remainingChances} / {chances} chances are remaining.")
        print(f"Incorrect responses : ", end="")
        for letter in incorrectRespones:
            print(f"{letter}, ", end="")
        print("\n")

    def getAnswerLetter(self):
        letter = str(input("Please enter a letter : "))
        return letter

    def displayEndMessage(self, chances, remainingChances):
        if(success):
            print("You have guessed the word. You WON.")
        else:
            print("You have run out of chances. You LOST")
