#main.py - main file
import stretchgame as stretch
import BARKOS as bark
import pygame

def loadAndPlay(levelname):
    stretch.main(bark.loadLevel(levelname+".bark"))

def mainmenu():
    pygame.init()
    screen = pygame.display.set_mode((400, 300))
    background = pygame.Surface(screen.get_size())
    clock = pygame.time.Clock()
    button = {}
    button["levels"] = {}
    button["levels"][0] = {}
    button["levels"][0]["name"] =  "level1"
    button["levels"][0]["rect"] = pygame.Rect(20,20,50,25)
    button["levels"][1] = {}
    button["levels"][1]["name"] =  "level2"
    button["levels"][1]["rect"] = pygame.Rect(20,60,50,25)

    while True:
        background.fill((255,255,255))
        background.fill((0,0,0),rect = button["levels"][0]["rect"])
        for but in button["levels"].values():
            #print(but)
            background.fill((0,0,0),rect = but["rect"])
            screen.blit(background, (0, 0))
            if pygame.mouse.get_pressed()[0]:
                if but["rect"].collidepoint(pygame.mouse.get_pos()):
                    loadAndPlay(but["name"])
            
        screen.blit(background, (0, 0))
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        pygame.display.flip()
        clock.tick(60)
     #   loadAndPlay("level1")
     #   loadAndPlay("level2")

mainmenu()
