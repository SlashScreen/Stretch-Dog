#stretchgame.py - main.lua basically

import pygame
import BARKOS as bark

###INIT###

pygame.init()
screen = pygame.display.set_mode((400, 300))
foot_distance = 0
gravity = -1
vel = 0
clock = pygame.time.Clock()
width= 15

def main():
    
    ##GLOBALS###
    
    global foot_distance
    global gravity
    global vel
    global clock
    global width
    
    ###VARIABLES###
    
    myimage = pygame.image.load("assets/feetv1.png")
    imagerect = myimage.get_rect()
    background = pygame.Surface(screen.get_size())
    background = background.convert()
    background.fill((250, 250, 250))
    level = bark.loadLevel("level1.bark")
    dogpos = 0
    scroll = 0
    
    ###LOOP###
    
    while True:
        background.fill((255,255,255))
        
        ###INCREMENT###
        
        vel+=gravity
        foot_distance -= vel
        scroll += 1
        rowcount = 0
        
        ###LIMITS###
        
        if foot_distance >= 300:
            foot_distance = 300
            vel = 0
        if foot_distance <= dogpos:
            foot_distance = dogpos+1

        ##DRAW DEBUG BOX AND LEGS###
            
        feetrect = pygame.Rect(screen.get_size()[0]/2,15+dogpos,30,foot_distance) ##Where foot is
        background.fill((0,0,0),rect = feetrect) #fill
        myimage = pygame.transform.scale(myimage, (30, foot_distance)) #transform
        screen.blit(background, (0, 0)) ##Blit
        screen.blit(myimage, feetrect) #Blit

        ###LOAD LEVEL###
        
        for row in level.values():
            rowcount -= 1
            pos = 0
            for tile in row.values():
                if tile["tile"] == "dirt":
                    tileimg = pygame.image.load("assets/dirt.png")
                elif tile["tile"] == "grass":
                    tileimg = pygame.image.load("assets/grass.png")
                elif tile["tile"] == "stone":
                    tileimg = pygame.image.load("assets/stone.png")
                pos+=1
                if not tile["tile"] == "air":
                    screenrect = pygame.Rect(rowcount*32+scroll,screen.get_size()[1]-(pos*32),32,32)
                    screen.blit(tileimg, screenrect)
                    
        ###CONTROL###
                    
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    vel = 10 #Jump Strength
        keys_pressed = pygame.key.get_pressed()
        if keys_pressed[pygame.K_w]:
            dogpos -= 1
        if keys_pressed[pygame.K_s]:
            dogpos += 1

        ###LIMITS###

        if dogpos <= 0: #Limit on Dog Up
            dogpos = 1
        elif dogpos >= screen.get_size()[1]:
            dogpos = screen.get_size()[1]-1
            
        ###SYSTEM###
            
        pygame.display.flip()
        clock.tick(60)
    
main()
