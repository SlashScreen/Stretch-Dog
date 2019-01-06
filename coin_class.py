#coin module
import BARKOS as bark

class coin:
    def __init__ (self,x,y):
        self.x = x
        self.y = y
        self.visible = True
        self.rect = pygame.Rect(self.x,self.y,32,32)

    def collect(self):
        self.visible = False

    def isColliding(self,other):
        return bark.isOverlapping(other,self.rect)
