import pygame
import time
from engine_v2 import Particle,Vector
import sys

width,height = 800,400
white = (255,255,255)
gray = (125,125,125)
black = (0,0,0)

green = (0, 255, 0)
blue = (0, 0, 128)

running = True




def main():
    global running, screen
    particle1 = Particle(600,180,3,Vector(35,0))
    particle2 = Particle(300,220,7,Vector(-15,0))
    particle3 = Particle(100,180,0.5,Vector(35,0))
    particle4 = Particle(200,220,0.5,Vector(-15,0))

    particles = []
    for i in range(1,2):
        particles += [particle1,particle2,particle3,particle4]
        #particles += [Particle(50+i*30,50,0.45,Vector(4,2))]
        #particles += [Particle(50+i*30,150,0.45,Vector(-3,0 ))]
        #particles += [Particle(50+i*30,200,0.45,Vector(-4,3))]

    pygame.init()
    screen = pygame.display.set_mode((width,height))
    pygame.display.set_caption("simul")
    screen.fill(white)
    pygame.display.update()
    sequ = True
    dir = Vector(0,0)
    force = 0.05


    font = pygame.font.Font('freesansbold.ttf', 32)
    text = font.render('GeeksForGeeks', True, green, blue)

    textRect = text.get_rect()
    textRect.center = (150, 30)

    action = ""

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT]:
            action = "Left"
            dir=Vector(-force,0)
        elif keys[pygame.K_RIGHT]:
            action = "Right"
            dir=Vector(force,0)
        elif keys[pygame.K_UP]:
            action = "Up"
            dir=Vector(0,-force)
        elif keys[pygame.K_DOWN]:
            action = "Down"
            dir=Vector(0,force)
        elif keys[pygame.K_SPACE]:
            action = "No gravity"
            dir=Vector(0,0)

        text = font.render(action, True, black)
        screen.fill(white)
        screen.blit(text, textRect)
        
        for particle in particles:
            pygame.draw.circle(screen,gray,particle.tupl(),particle.r)
        #pygame.draw.circle(screen,gray,particle1.tupl(),particle1.r)
        #pygame.draw.circle(screen,gray,particle2.tupl(),particle2.r)
        #if particle1.collide():
        #print(particle1.tupl())
        for i in range(len(particles)):
            particles[i].update(dir)
        for i in range(len(particles)):
            for j in range(i+1,len(particles)):
                if particles[i].collide(particles[j]):
                    particles[j].velocity, particles[j].position = particles[i].resolution(particles[j])

        #if particle1.collide(particle2):
        #    particle2.velocity, particle2.position = particle1.resolution(particle2)

        #particle1.update()
        #particle2.update()
        pygame.display.update()
        pygame.time.delay(5)

if __name__=="__main__":
    main()