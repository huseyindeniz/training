import pygame
import random
import math

pygame.init()
#screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN | pygame.HWSURFACE | pygame.DOUBLEBUF)
screen = pygame.display.set_mode((800,600))
clock = pygame.time.Clock()

done = False
color = (255, 255, 255)
color2 = (0, 0, 20)
color3 = (50, 120, 240)

surface1 = pygame.Surface((240, 150))
surface2 = pygame.Surface((240, 150))

maskImage = pygame.image.load("images.png").convert_alpha()

is_open = True
counter = 0
x = random.randint(100,300)

while not done:
    
    clock.tick(60)
    screen.fill((0, 0, 0))
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                done = True

    if counter > x and counter < x+10: 
        is_open = False
    else: is_open = True

    if counter == x + 10:
        x = random.randint(100,300)

    if is_open:
        pygame.draw.ellipse(surface1, color3, (0,0, 240, 150)) 
        surfacer1 = pygame.transform.rotate(surface1, -10)
        pygame.draw.ellipse(surface2, color3, (0,0, 240, 150)) 
        surfacer2 = pygame.transform.rotate(surface2, 10)

        masked_result = maskImage.copy()
        surfacer1.blit(masked_result, (0, 0), None, pygame.BLEND_RGBA_MULT)
        surfacer2.blit(masked_result, (0, 0), None, pygame.BLEND_RGBA_MULT)
        
        screen.blit(surfacer1, (10, 10))
        screen.blit(surfacer2, (320, 10))    
    else:
        pygame.draw.arc(screen, color3, (10, 100, 300, 50),-math.pi, 0, 10) 
        pygame.draw.arc(screen, color3, (330, 100, 300, 50),-math.pi, 0, 10) 
    
    counter += 1
    counter %= 300
    pygame.display.flip()

pygame.quit()        