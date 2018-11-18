import pygame
import BARKOS as bark

pygame.init()
screen = pygame.display.set_mode((400, 300))
foot_distance = 0
gravity = -1
vel = 0
clock = pygame.time.Clock()
width= 15
def main():
    global foot_distance
    global gravity
    global vel
    global clock
    global width
    myimage = pygame.image.load("assets/feetv1.png")
    imagerect = myimage.get_rect()
    background = pygame.Surface(screen.get_size())
    print(screen.get_size())
    background = background.convert()
    background.fill((250, 250, 250))
    level = bark.loadLevel("level1.bark")
    dogpos = 0
    print(level.keys())
    scroll = 0
    while True:
        background.fill((255,255,255))
        vel+=gravity
        foot_distance -= vel
        if foot_distance >= 300:
            foot_distance = 300
            vel = 0
        if foot_distance <= dogpos:
            foot_distance = dogpos+1
        feetrect = pygame.Rect(screen.get_size()[0]/2,15+dogpos,30,foot_distance) ##Where foot is
        background.fill((0,0,0),rect = feetrect)
        myimage = pygame.transform.scale(myimage, (30, foot_distance)) #transform
        #print(vel,foot_distance)
        screen.blit(background, (0, 0))
        screen.blit(myimage, feetrect)
        scroll += 1
        rowcount = 0
        for row in level.values():
            rowcount -= 1
            pos = 0
            for tile in row.values():
                #print(tile,tile["tile"])
                if tile["tile"] == "dirt":
                    tileimg = pygame.image.load("assets/dirt.png")
                elif tile["tile"] == "grass":
                    tileimg = pygame.image.load("assets/grass.png")
                elif tile["tile"] == "stone":
                    tileimg = pygame.image.load("assets/stone.png")
                pos+=1
                if not tile["tile"] == "air":
                    #print(scroll,pos)
                    screenrect = pygame.Rect(rowcount*32+scroll,screen.get_size()[1]-(pos*32),32,32)
                    screen.blit(tileimg, screenrect)
                    
        pygame.display.flip()
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

            
        if dogpos <= 0:
            dogpos = 1

 #       screen.blit(screen, (0, 0))
 #       pygame.display.flip()
        clock.tick(60)
    
main()
