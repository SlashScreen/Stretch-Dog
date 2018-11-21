#main.py - main file
import stretchgame as stretch
import BARKOS as bark
import pygame

def loadAndPlay(levelname):
    stretch.main(bark.loadLevel(levelname+".bark"))

def mainmenu():

    ###INIT###
    
    pygame.init()
    pygame.font.init()

    ###VARIABLES###
    
    screen = pygame.display.set_mode((400, 300))
    background = pygame.Surface(screen.get_size())
    clock = pygame.time.Clock()
    myfont = pygame.font.SysFont(pygame.font.get_default_font(), 30)
    button = {}
    width = 100
    height = 30
    button["levels"] = {}
    button["levels"][0] = {}
    button["levels"][0]["file"] =  "level1"
    button["levels"][1] = {}
    button["levels"][1]["file"] =  "level2"

    ###LOOP##

    while True:
        
        ###START###
        
        background.fill((255,255,255))
        pos = 0

        ###RENDER BUTTONS
        
        for but in button["levels"].values():
            pos+=1
            rect = pygame.Rect((screen.get_size()[0]/2)-(width/2),pos*75,width,height) #Create button
            textsurface = myfont.render("Some text!", 1, (255,255,0)) #Text Surface
            background.fill((0,0,0),rect = rect) #Draw button
            screen.blit(background, (0, 0)) #Blit button
            screen.blit(textsurface, (100, 100)) #Blit text
            if pygame.mouse.get_pressed()[0]: #Check if clicked
                if rect.collidepoint(pygame.mouse.get_pos()):
                    loadAndPlay(but["file"]) #Play
        screen.blit(background, (0, 0))

        ###CONTROLS###
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        ###SYSTEM STUFF###
            
        pygame.display.flip()
        clock.tick(60)

mainmenu()
