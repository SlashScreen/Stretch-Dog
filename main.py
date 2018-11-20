#main.py - main file
import stretchgame as stretch
import BARKOS as bark

def loadAndPlay(levelname):
    stretch.main(bark.loadLevel(levelname+".bark"))

loadAndPlay("level1")
loadAndPlay("level2")
