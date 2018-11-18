import pygame


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
    while True:
        background.fill((255,255,255))
        vel+=gravity
        foot_distance -= vel
        if foot_distance >= 300:
            foot_distance = 300
            vel = 0
        feetrect = pygame.Rect(screen.get_size()[0]/2,15,30,foot_distance)
        background.fill((0,0,0),rect = feetrect)
        myimage = pygame.transform.scale(myimage, (30, foot_distance))
        #print(vel,foot_distance)
        screen.blit(background, (0, 0))
        screen.blit(myimage, feetrect)
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            if event.type == pygame.KEYDOWN:
                  if event.key == pygame.K_SPACE:
                    vel = 10 #Jump Strength

 #       screen.blit(screen, (0, 0))
 #       pygame.display.flip()
        clock.tick(60)
    
main()
