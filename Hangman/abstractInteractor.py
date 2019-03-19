from abc import ABC, abstractmethod


class Interactor(ABC):
    @abstractmethod
    def getInputWord(self, maxLength):
        pass

    @abstractmethod
    def getAnswerLetter(self):
        pass

    @abstractmethod
    def clearDisplay(self):
        system("cls")

    @abstractmethod
    def updateDisplay(self, word, chances, incorrectRespones):
        pass

    @abstractmethod
    def displayEndMessage(self, chances, remainingChances):
        pass
