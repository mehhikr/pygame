'''
pygame has to be the least developer friendly platform
very simple ball catching game
'''

import pygame
import random
import sys
import time
import os
from pygame.locals import *

WINDOWWIDTH = 1920
WINDOWHEIGHT = 1080
BALLSIZE = 20
BUCKETSIZE = 10
FPS = 165 #165hz ftw


WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLACK = (0, 0, 0)
BLUE = (0, 193, 255)

def terminate():
    pygame.quit()
    sys.exit()


def playerHasHitBall(playerRect, ball):
    for ball in balls:
        if playerRect.colliderect(ball['rect']):
            return True
    return False


def ballHasHitGround(ball):
    if ball['rect'].top > WINDOWHEIGHT:
        return True
    return False


def drawText(text, font, surface, x, y):
    textobj = font.render(text, 1, WHITE)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)


def gameover():
    gosound = pygame.mixer.Sound('gameover.wav') #AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
    gosound.play()

    


pygame.init()
mainClock = pygame.time.Clock()
windowSurface = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
pygame.display.set_caption('Ball Catch')
pygame.mouse.set_visible(False)


font = pygame.font.SysFont(None, 48)

starttime = time.time()
bucketimg = pygame.image.load('bucket.png')


playerRect = bucketimg.get_rect()
playerRect.topleft = (50, 50)


ballImage = pygame.Surface((5,20))
ballImage.fill(BLUE)

backgroundImage = pygame.Surface((WINDOWWIDTH, WINDOWHEIGHT))
backgroundImage.fill((0,0,0))


windowSurface.blit(backgroundImage, (0,0))
windowSurface.blit(bucketimg, (WINDOWWIDTH / 2, WINDOWHEIGHT - BUCKETSIZE - 10))
drawText('Press Enter to start', font, windowSurface, (WINDOWWIDTH / 3), (WINDOWHEIGHT / 3))
pygame.display.update()







while True:

    drawText(f'Catch the rain!', font, windowSurface, WINDOWWIDTH // 3, WINDOWHEIGHT // 3)

    gamesound = pygame.mixer.Sound('gamesound.wav') #?? idk what to put
    gamesound.play()

    balls = []
    balls.append({'rect': pygame.Rect(random.randint(0, WINDOWWIDTH - BALLSIZE), 0 - BALLSIZE, BALLSIZE, BALLSIZE),
                  'speed': random.randint(1, 2),
                  'surface':pygame.transform.scale(ballImage, (BALLSIZE, BALLSIZE)),
                 })

    score = 0

    playerRect.topleft = (50, WINDOWHEIGHT - BUCKETSIZE - 10)
    moveLeft = moveRight = False

    gameOverSoundPlayed = False

    while True: 
        for event in pygame.event.get():
            if event.type == QUIT:
                terminate()

            if event.type == KEYDOWN:
                if event.key == K_LEFT or event.key == ord('a'):
                    moveRight = False
                    moveLeft = True
                if event.key == K_RIGHT or event.key == ord('d'):
                    moveLeft = False
                    moveRight = True

            if event.type == KEYUP:
                if event.key == K_ESCAPE:
                        terminate()

                if event.key == K_LEFT or event.key == ord('a'):
                    moveLeft = False
                if event.key == K_RIGHT or event.key == ord('d'):
                    moveRight = False

        if not random.randrange(0, 50):
            balls.append({'rect': pygame.Rect(random.randint(0, WINDOWWIDTH - BALLSIZE), 0 - BALLSIZE, BALLSIZE, BALLSIZE),
                  'speed': random.randint(1, 2),
                  'surface': pygame.transform.scale(ballImage, (BALLSIZE, BALLSIZE)),
                 })

        if moveLeft and playerRect.left > 0:
            playerRect.move_ip(-5 ,0)
        if moveRight and playerRect.right < WINDOWWIDTH:
            playerRect.move_ip(5 ,0)

        for ball in balls:
            ball['rect'].move_ip(0 ,ball['speed'])

        for ball in balls[:]:
            if ball['rect'].top > WINDOWHEIGHT:
                balls.remove(ball)
        

        
        windowSurface.blit(backgroundImage , (0 ,0))

        
        windowSurface.blit(bucketimg , playerRect)

        
        for ball in balls:
            windowSurface.blit(ball['surface'] ,ball['rect'])
        

        pygame.display.update()

        
        if playerHasHitBall(playerRect ,ball): 
            score += 1
            balls = [ball for ball in balls if not playerRect.colliderect(ball['rect'])]
        
        if time.time() - starttime >= 30:
            drawText(f'Final Score: {score} Nice one! You saved {score} Litres of Water!', font, windowSurface, WINDOWWIDTH // 3, WINDOWHEIGHT // 3)
            drawText(f'In Singapore, much water is wasted a day by many. Many litres of water is just emptied down the drain. Lets save water!', font, windowSurface, WINDOWWIDTH // 2, WINDOWHEIGHT // 3 - 50)
            """
            may not work on some displays
            it works on my home computer but not on others so the text formatting may be wonky
            """
            gameover()
            pygame.display.update()
            pygame.time.delay(15000)  
            terminate()




        mainClock.tick(200)
