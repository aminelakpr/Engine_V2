import pygame
import time
from engine_v2 import Particle,Vector
import sys

width,height = 800,400
white = (255,255,255)
gray = (125,125,125)

running = True

square = width/32

def returner(t):
    (x,y) = t


    x1 = int(x/square)*square+square


    return int(x/square)*square+square/2,int(y/square)*square+square/2

def main():
    global running, screen
    particle1 = Particle(600,180,3,Vector(35,0))
    particle2 = Particle(300,220,7,Vector(-15,0))

    particles = []
    for i in range(1,15):
        particles += [Particle(50+i*30,100,0.45,Vector(2,3))]
        particles += [Particle(50+i*30,50,0.45,Vector(4,2))]
        particles += [Particle(50+i*30,150,0.45,Vector(-3,5))]
        particles += [Particle(50+i*30,200,0.45,Vector(-4,3))]


    pygame.init()
    screen = pygame.display.set_mode((width,height))
    pygame.display.set_caption("simul")
    screen.fill(white)
    pygame.display.update()
    sequ = True
    dir = Vector(0,0)
    force = 0.06

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT]:
            print("Left")  
            dir=Vector(-force,0)
        elif keys[pygame.K_RIGHT]:
            print("Right")
            dir=Vector(force,0)
        elif keys[pygame.K_UP]:
            print("Up")
            dir=Vector(0,-force)
        elif keys[pygame.K_DOWN]:
            print("Down")
            dir=Vector(0,force)
        elif keys[pygame.K_SPACE]:
            print("Space")
            dir=Vector(0,0)

        screen.fill(white)

        
        for i in range(16):
            pygame.draw.line(screen,"#000000", (2*i*square, 0), (2*i*square, height))
            pygame.draw.line(screen,"#000000", (((2*i)+1)*square, 0), (((2*i)+1)*square, height))
            pygame.draw.line(screen,"#000000", (0, i*square), (width, i*square))
            
        
        for particle in particles:
            pygame.draw.circle(screen,"#000000",particle.tupl(),particle.r)
            xpos,ypos = returner(particle.tupl())
            #print(xpos,ypos)
            pygame.draw.rect(screen,"#AA76AA",(xpos-square/2,ypos-square/2,square,square))


        #pygame.draw.circle(screen,gray,particle1.tupl(),particle1.r)
        #pygame.draw.circle(screen,gray,particle2.tupl(),particle2.r)
        #if particle1.collide():
        #print(particle1.tupl())

        for i in range(len(particles)):
            for j in range(len(particles)):
                if particles[i].collide(particles[j]) and i!=j:
                     particles[j].velocity, particles[j].position = particles[i].resolution(particles[j])

        #if particle1.collide(particle2):
        #    particle2.velocity, particle2.position = particle1.resolution(particle2)

        for particle in particles:
            particle.update(dir)
        #particle1.update()
        #particle2.update()
        pygame.display.update()
        pygame.time.delay(5)

if __name__=="__main__":
    main()


