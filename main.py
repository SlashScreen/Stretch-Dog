#main.py - main file
import stretchgame as stretch
import BARKOS as bark
import pygame
coins = 0

def loadAndPlay(levelname,coins):
    c = stretch.main(bark.loadLevel(levelname+".bark"),coins)
    return c

def mainmenu(coins,completed):

    print(coins,completed)

    ###INIT###
    
    pygame.init()
    pygame.font.init()
    pygame.display.set_caption("STRETCHDOG")
    pygame.mixer.pre_init(16500, -16, 2, 2048)
    pygame.mixer.music.load("assets/music/stretch-theme.ogg")
    pygame.mixer.music.play(-1)

    ###VARIABLES###
    
    screen = pygame.display.set_mode((400, 300))
    background = pygame.Surface(screen.get_size())
    clock = pygame.time.Clock()
    myfont = pygame.font.SysFont(pygame.font.get_default_font(), 30)
    button = {}
    width = 100
    height = 30
    offset = 10
    button["levels"] = {}
    llist = bark.getLevelList()
    butimg = pygame.image.load("assets/startbutton.png")
    completeimg = pygame.image.load("assets/startbuttondone.png")
    logo = pygame.image.load("assets/stretchdoglogo.png")

    
    for i in range(len(llist)):
        button["levels"][i] = {}
        button["levels"][i]["file"] =  llist[i]

    ###LOOP##

    while True:
        
        ###START###
        
        background.fill((135,206,235))
        screen.blit(background, (0,0))
        pos = 0

        ###RENDER###
        
        #Render Logo and coins
        
        csurface = myfont.render("Coins: "+str(coins), 1, (255,255,0)) #Text Surface
        lrect = pygame.Rect(0,0,50,screen.get_height())
        screen.blit(pygame.transform.scale(logo,lrect.size),lrect) #logo
        screen.blit(csurface, (55,5)) #text
        
        #Render Buttons
        
        for but in button["levels"].values():
            rect = pygame.Rect((screen.get_size()[0]/2)-(width/2),(pos*75)+offset,width,height) #Create button
            textsurface = myfont.render(but["file"], 1, (255,255,0)) #Text Surface
            if but["file"] in completed:
                screen.blit(pygame.transform.scale(completeimg,rect.size),rect)
            else:
                screen.blit(pygame.transform.scale(butimg,rect.size),rect)
            screen.blit(textsurface, rect) #Blit text
            if pygame.mouse.get_pressed()[0]: #Check if clicked
                if rect.collidepoint(pygame.mouse.get_pos()):
                    try:
                        pygame.mixer.music.stop()
                        coins = loadAndPlay(but["file"],coins) #Play
                        pygame.mixer.music.load("assets/music/stretch-theme.ogg")
                        pygame.mixer.music.play(-1)
                        pygame.display.set_caption("STRETCHDOG")
                        if not but["file"] in completed:
                            completed.append(but["file"])
                        print (coins)
                    except Exception as e:
                        print(e,"error")
                        pygame.quit()
            pos+=1

        ###CONTROLS###
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                bark.save(bark.constructSaveData(coins,completed))
                pygame.quit()
            
        ###SYSTEM STUFF###
            
        pygame.display.flip()
        clock.tick(60)

file = bark.load()
mainmenu(file["c"],file["complete"])
