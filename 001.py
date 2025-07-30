import pygame
import time
from engine_v2 import Particle,Vector
import sys

width,height = 800,400
white = (255,255,255)
gray = (125,125,125)

running = True

particle1 = Particle(300,100,5)


def main():
    global running, screen

    pygame.init()
    screen = pygame.display.set_mode((width,height))
    pygame.display.set_caption("simul")
    screen.fill(white)
    pygame.display.update()

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        screen.fill(white)
        pygame.draw.circle(screen,gray,particle1.tupl(),particle1.r)
        print(particle1.tupl())
        particle1.update(Vector(0,0))
        pygame.display.update()
        pygame.time.delay(20)

if __name__=="__main__":
    main()