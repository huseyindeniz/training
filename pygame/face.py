import pygame
import random
import math

pygame.init()
screen = pygame.display.set_mode((700, 456))
clock = pygame.time.Clock()

PI=math.pi

done = False
color = (255, 255, 255)
color2 = (0, 0, 20)
color3 = (0, 200, 255)
is_open = True
counter = 0
x = random.randint(100,300)

while not done:
    
    clock.tick(60)
    screen.fill((0, 0, 0))
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    if counter > x and counter < x+10: 
        is_open = False
    else: is_open = True

    if counter == x + 10:
        x = random.randint(100,300)
    
    if is_open:
        pygame.draw.ellipse(screen, color, (10,10, 300, 150))
        pygame.draw.ellipse(screen, color, (330,10, 300, 150))      
        pygame.draw.circle(screen, color2, (160,100), 50)
        pygame.draw.circle(screen, color2, (480,100), 50)   
        pygame.draw.circle(screen, color3, (160,100), 25)
        pygame.draw.circle(screen, color3, (480,100), 25)      
        pygame.draw.circle(screen, color2, (160,100), 10)
        pygame.draw.circle(screen, color2, (480,100), 10)                          
    else:
        pygame.draw.arc(screen, color, (10, 100, 300, 50),-PI, 0, 10) 
        pygame.draw.arc(screen, color, (330, 100, 300, 50),-PI, 0, 10)  

    counter += 1
    counter %= 300
    pygame.display.flip()

pygame.quit()