import pygame
import time
import random

pygame.init()

display_width = 1152
display_height = 648

dinosaurWidth = 80
dinosaurHeight = 108

cactusWidth = 90
cactusHeight = 154

birdWidth = 130
birdHeight = 111

black = (0, 0, 0)
white = (255, 255, 255)

backgroundImage = pygame.image.load('DinosaurBackground.png')
dinosaurImage = pygame.image.load('dinosaur.png')
cactusImage = pygame.image.load('cactus.png')
birdImage = pygame.image.load('bird.png')

screen = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption("Dinosaur 2D")
clock = pygame.time.Clock()


def background():
    screen.blit(backgroundImage, (0, 0))


def dinosaur(x, y):
    screen.blit(dinosaurImage, (int(x), int(y)))


def cactus(x, y):
    screen.blit(cactusImage, (int(x), int(y)))


def bird(x, y):
    screen.blit(birdImage, (int(x), int(y)))


def collision1(x1, y1, w1, h1, x2, y2, w2, h2):
    if x2 < x1 + w1 < x2 + w2 and y1 + h1 > y2:
        return True


def collision2(x1, y1, w1, h1, x2, y2, w2, h2):
    if x2 < x1 + w1 < x2 + w2 and y2 < y1 < y2 + h2:
        return True


def scored(count):
    font = pygame.font.SysFont(None, 40)
    text = font.render(("Score: " + str(count)), True, black)
    screen.blit(text, (0, 0))


def text_objects(text, font):
    text_surface = font.render(text, True, black)
    return text_surface, text_surface.get_rect()


def message_display(text):
    largeText = pygame.font.Font('freesansbold.ttf', 80)
    text_surface, text_rectangle = text_objects(text, largeText)
    text_rectangle.center = (int((display_width / 2)), int((display_height / 2)))
    screen.blit(text_surface, text_rectangle)
    pygame.display.update()
    time.sleep(2)
    gameLoop()


def crash():
    message_display("Game Over")


def gameLoop():
    dinosaurX = 50
    dinosaurY = display_height - dinosaurHeight - 10
    dinosaurXvel = +5
    dinosaurYvel = 0

    cactusX = display_width
    cactusY = display_height - cactusHeight
    cactusXvel = -10
    cactusYvel = 0

    birdX = display_width + random.randint(0, 200)
    birdY = random.randint(0, display_height / 2. - birdHeight)
    birdXvel = -10
    birdYvel = 0

    score = 0
    gameExit = False
    while not gameExit:
        background()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    dinosaurYvel = -7

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_SPACE:
                    dinosaurYvel = +7

        dinosaurY += dinosaurYvel

        if dinosaurY + dinosaurHeight >= display_height:
            dinosaurYvel = 0

        cactusX += cactusXvel
        birdX += birdXvel

        if cactusX + cactusWidth < 0:
            cactusX = display_width
            cactusXvel += -2
            score += 1

        if birdX + birdWidth < 0:
            birdX = display_width + random.randint(0, 500)
            birdY= random.randint(0, display_height / 2. - birdHeight+10)
            birdXvel += -2
            score += 1

        if collision1(dinosaurX, dinosaurY, dinosaurWidth, dinosaurHeight, cactusX, cactusY, cactusWidth,
                      cactusHeight):
            crash()
        if collision2(dinosaurX + dinosaurWidth, dinosaurY, dinosaurWidth, dinosaurHeight,
                      birdX, birdY, birdWidth,
                      birdHeight):
            crash()

        scored(score)
        bird(birdX, birdY)
        dinosaur(dinosaurX, dinosaurY)
        cactus(cactusX, cactusY)
        pygame.display.update()
        clock.tick(150)


gameLoop()
pygame.quit()
quit()
