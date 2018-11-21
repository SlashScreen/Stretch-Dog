#stretchgame.py - main.lua basically

import pygame
import BARKOS as bark

def getStandardRect(screen,rowcount,direction,scroll,pos):
    return pygame.Rect(screen.get_size()[1]-(rowcount*32+scroll),screen.get_size()[1]-(pos*32),32,32)

def main(level):

    ###INIT###

    pygame.init()
    screen = pygame.display.set_mode((400, 300))
    foot_distance = 0
    gravity = -3
    vel = 0
    clock = pygame.time.Clock()
    width= 15
    dogpos = 0
    scrollstart = 175
    scroll = scrollstart
    jump = 50

    ###VARIABLES###
    
    myimage = pygame.image.load("assets/feetv1.png")
    imagerect = myimage.get_rect()
    background = pygame.Surface(screen.get_size())
    background = background.convert()
    background.fill((250, 250, 250))
    dead = False
    direction = 1
    
    ###LOOP###
    
    while not dead:
        background.fill((255,255,255))
        
        ###INCREMENT###

        dt = (clock.get_time())/100
        vel+=gravity
        foot_distance -= int(vel*dt)
        scroll += (1*direction)
        rowcount = 0
            
        #print(win)
        
        ###LIMITS###
        
        if foot_distance+dogpos >= 300:
            foot_distance = 299-dogpos
            vel = 0
        if foot_distance <= 0:
            foot_distance = 1

        ##DRAW DEBUG BOX AND LEGS###
            
        feetrect = pygame.Rect(screen.get_size()[0]/2,15+dogpos,30,foot_distance) ##Where foot is
        colbox = pygame.Rect(screen.get_size()[0]/2,15+dogpos,30,foot_distance-15) ##where dog dies
        floorbox = pygame.Rect(0,screen.get_size()[1],screen.get_size()[0],2)
        footbox = pygame.Rect(screen.get_size()[0]/2,foot_distance+dogpos,30,15) ##Bottom of foot
        background.fill((0,0,0),rect = feetrect) #fill
        background.fill((0,0,255),rect = colbox) #fill
        background.fill((0,255,0),rect = footbox) #fill
        myimage = pygame.transform.scale(myimage, (30, foot_distance)) #transform
        screen.blit(background, (0, 0)) ##Blit
        screen.blit(myimage, feetrect) #Blit

        ###RENDER LEVEL###
       # print(win)
        for row in level["level"].values():
            rowcount -= 1
            pos = 0
            for tile in row.values():
                if tile["tile"] == "dirt":
                    tileimg = pygame.image.load("assets/dirt.png")
                elif tile["tile"] == "grass":
                    tileimg = pygame.image.load("assets/grass.png")
                elif tile["tile"] == "stone":
                    tileimg = pygame.image.load("assets/stone.png")
                elif tile["tile"] == "win":
                    tileimg = pygame.image.load("assets/win.png") #Flip
                    winbox = getStandardRect(screen,rowcount,direction,scroll,pos) #Win box
                    screen.blit(tileimg, winbox)
                    background.fill((125,125,0),rect = winbox)
                    if bark.isOverlapping(colbox,winbox): #Test flip collision
                        return
                elif tile["tile"] == "flip":
                    tileimg = pygame.image.load("assets/flip.png")
                    flipbox = getStandardRect(screen,rowcount,direction,scroll,pos) #Win box
                    screen.blit(tileimg, flipbox)
                    background.fill((125,125,0),rect = flipbox)
                    if bark.isOverlapping(colbox,flipbox): #Test win collision
                        print("flipping my pancakes")
                        direction = -1
                        
                pos+=1
                if not tile["tile"] == "air" or tile["tile"] == "win":
                    screenrect = getStandardRect(screen,rowcount,direction,scroll,pos) #regular tile
                    screen.blit(tileimg, screenrect)
                    
                    if bark.isOverlapping(footbox,screenrect): #Test if foot touch
                        vel = 0
                        foot_distance -= 1
                    if bark.isOverlapping(colbox,screenrect): #Test collision
                        print(tile["tile"])
                        if not tile["tile"] == "win" :
                            if not tile["tile"] == "flip":
                                dogpos = 0
                                scroll = scrollstart
                                vel = 0
                                foot_distance = 0
    
                
                    
        ###CONTROL###
                    
        for event in pygame.event.get(): #Quit
            if event.type == pygame.QUIT:
                raise Exception('Quitting Game')
            if event.type == pygame.KEYDOWN: #Keydown
                if event.key == pygame.K_SPACE:
                    vel = jump #Jump Strength
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
