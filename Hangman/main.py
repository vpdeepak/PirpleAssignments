import pygame
import re

# Initialize the game engine
pygame.init()

# Defining the colors used in the project
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

FONTHEADER = pygame.font.Font("freesansbold.ttf", 50)
FONTNORMAL = pygame.font.Font("freesansbold.ttf", 30)

APPLICATION_x_size = 1200
APPLICATION_y_size = 600


def getWordFromUser():
    x = 200
    inputWord = ""
    inputDone = False
    pygame.time.Clock().tick(10)
    while not inputDone:
        for event in pygame.event.get():
            if(event.type == pygame.KEYDOWN):
                if(event.key == 271):
                    inputDone = True
                elif(re.search("[A-Za-z]", chr(event.key))):
                    screen.blit(FONTNORMAL.render(chr(event.key), True, BLUE),
                                (x, 300))
                    x += 30
                    inputWord += chr(event.key)
                pygame.display.update()
    return inputWord


screen = pygame.display.set_mode((APPLICATION_x_size, APPLICATION_y_size))
pygame.display.set_caption("HANGMAN")

done = False
clock = pygame.time.Clock()
x = 200
screen.fill(WHITE)
screen.blit(FONTHEADER.render("HANGMAN", True, BLACK), (495, 10))

inputString = "Player 1 : Please enter the word to be used. "
screen.blit(FONTNORMAL.render(inputString, True, BLUE), (200, 200))
pygame.display.flip()

quizWord = getWordFromUser()
screen.blit(FONTNORMAL.render(quizWord, True, BLUE), (200, 400))
pygame.display.flip()

while not done:
    clock.tick(10)
    for event in pygame.event.get():
        if(event.type == pygame.QUIT):
            done = True
    # pygame.draw.line(screen, GREEN, [0, 0], [50, 30], 5)
    # pygame.draw.ellipse(screen, RED, [0, 0, 150, 150], 1)
    pygame.display.flip()

pygame.quit()
