import pygame
import re
from abstractInteractor import Interactor


class PyGameInteractor(Interactor):
    # Defining the colors used in the project
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    RED = (255, 0, 0)
    GREEN = (0, 255, 0)
    BLUE = (0, 0, 255)

    APPLICATION_x_size = 1200
    APPLICATION_y_size = 600

    def __init__(self):
        # Initialize the game engine
        pygame.init()
        pygame.time.Clock().tick(10)
        self.screen = pygame.display.set_mode(
            (self.APPLICATION_x_size, self.APPLICATION_y_size))
        self.FONTHEADER = pygame.font.Font("freesansbold.ttf", 50)
        self.FONTNORMAL = pygame.font.Font("freesansbold.ttf", 30)
        self.FONTNOTE = pygame.font.Font("freesansbold.ttf", 20)
        self.HangmanMap = {
            1: self.drawRope,
            2: self.drawHead,
            3: self.drawBody,
            4: self.drawLeftHand,
            5: self.drawRightHand,
            6: self.drawLeftLeg,
            7: self.drawRightLeg,
        }

    def clearDisplay(self):
        self.screen.fill(self.WHITE)
        pygame.display.update()

    def getInputWord(self, maxLength):
        message_X = 200
        message_Y = 200
        message = f"Please enter the input word (max length {maxLength}): "
        self.screen.blit(self.FONTNORMAL.render(message, True, self.BLUE),
                         (message_X, message_Y))
        pygame.display.update()

        message_Y += 100
        word = " "
        inputDone = False
        while not inputDone:
            for event in pygame.event.get():
                if(event.type == pygame.KEYDOWN):
                    if(event.key == 271):
                        inputDone = True
                    elif(re.search("[A-Za-z0-9 ]", chr(event.key))):
                        self.screen.blit(self.FONTNORMAL.render(chr(event.key),
                                                                True,
                                                                self.BLUE),
                                         (message_X, message_Y))
                        message_X += 30
                        word += chr(event.key)
                        pygame.display.update()
                elif(event.type == pygame.QUIT):
                    word = "quit"
                    inputDone = True
        return word

    def drawGallows(self):
        pygame.draw.line(self.screen, self.BLACK, [1000, 100], [1000, 500], 3)
        pygame.draw.line(self.screen, self.BLACK, [900, 500], [1100, 500], 5)
        pygame.draw.line(self.screen, self.BLACK, [800, 100], [1000, 100], 3)

    def drawRope(self):
        pygame.draw.line(self.screen, self.BLACK, [900, 100], [900, 150], 3)

    def drawHead(self):
        pygame.draw.circle(self.screen, self.GREEN, [900, 180], 30, 3)

    def drawBody(self):
        pygame.draw.line(self.screen, self.GREEN, [900, 210], [900, 300], 3)

    def drawLeftHand(self):
        pygame.draw.line(self.screen, self.GREEN, [900, 230], [960, 270], 3)

    def drawRightHand(self):
        pygame.draw.line(self.screen, self.GREEN, [900, 230], [840, 270], 3)

    def drawLeftLeg(self):
        pygame.draw.line(self.screen, self.GREEN, [900, 300], [960, 370], 3)

    def drawRightLeg(self):
        pygame.draw.line(self.screen, self.GREEN, [900, 300], [840, 370], 3)

    def drawPuzzle(self, word):
        message_X = 100
        message_Y = 175
        for index in range(0, len(word)):
            self.screen.blit(self.FONTNORMAL.render(
                f"{word[index]} ", True, self.BLUE), (message_X, message_Y))
            message_X += 30

    def drawRemainingChances(self, chances, remainingChances):
        message_X = 100
        message_Y = 500
        message = f"{remainingChances} / {chances} chances are remaining."
        self.screen.blit(self.FONTNOTE.render(
            message, True, self.GREEN), (message_X, message_Y))

    def drawIncorrectResponses(self, incorrectResponses):
        message_X = 100
        message_Y = 550
        message = "Incorrect Responses : "
        self.screen.blit(self.FONTNOTE.render(
            message, True, self.BLUE), (message_X, message_Y))
        message_X += len(message) + 200
        for letter in incorrectResponses:
            self.screen.blit(self.FONTNOTE.render(
                f"{letter}, ", True, self.RED), (message_X, message_Y))
            message_X += 30

    def updateDisplay(self, word, chances, incorrectResponses,
                      remainingChances):
        # draw the gallows
        self.drawGallows()

        # depending on the inverse of the remaining chances draw the man
        countInvalidReponses = chances - remainingChances
        for count in range(1, countInvalidReponses + 1):
            draw = self.HangmanMap.get(count)
            draw()

        # display the puzzle
        self.drawPuzzle(word)

        # display the remaining chances
        self.drawRemainingChances(chances, remainingChances)

        # display the incorrect responses
        self.drawIncorrectResponses(incorrectResponses)

        pygame.display.update()

    def getAnswerLetter(self):
        message_X = 100
        message_Y = 300
        message = f"Please enter a letter :  "
        inputDone = False
        self.screen.blit(self.FONTNOTE.render(message, True, self.BLUE),
                         (message_X, message_Y))
        pygame.display.update()

        message_X += len(message) + 200
        while not inputDone:
            for event in pygame.event.get():
                if(event.type == pygame.KEYDOWN):
                    if(re.search("[A-Za-z0-9]", chr(event.key))):
                        self.screen.blit(self.FONTNORMAL.render(chr(event.key).
                                                                upper(),
                                                                True,
                                                                self.BLUE),
                                         (message_X, message_Y))
                        letter = chr(event.key)
                        pygame.display.update()
                    else:
                        letter = None
                    inputDone = True
        return letter

    def displayEndMessage(self, success, chances, remainingChances):
        message_X = 200
        message_Y = 250

        self.drawGallows()
        # depending on the inverse of the remaining chances draw the man
        countInvalidReponses = chances - remainingChances
        for count in range(1, countInvalidReponses + 1):
            draw = self.HangmanMap.get(count)
            draw()

        if(success):
            message = "You have guessed the word. You WON."
            self.screen.blit(self.FONTNORMAL.render(
                message, True, self.GREEN), (message_X, message_Y))
        else:
            message = "You have run out of chances. You LOST"
            self.screen.blit(self.FONTNORMAL.render(
                message, True, self.RED), (message_X, message_Y))
        pygame.display.update()
