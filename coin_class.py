#coin module
import BARKOS as bark
import pygame

class coin:
    def __init__ (self,x,y):
        self.x = x
        self.y = y
        self.visible = True
        self.rect = pygame.Rect(self.x,self.y,32,32)
        self.img = pygame.image.load("assets/coin.png")

    def getVisible(self):
        return self.visible

    def getRect(self):
        return self.rect

    def getPos(self):
        return self.x,self.y

    def getImg(self):
        return self.img

    def reset(self):
        self.visible = True

    def collect(self):
        if self.visible:
            self.visible = False
            #print("collected")

    def isColliding(self,other):
        return bark.isOverlapping(other,self.rect)
