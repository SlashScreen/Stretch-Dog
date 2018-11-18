#BARK-OS
#Used for Stuff that involves the system

#Read Level and construct
#Calculate Stretch
#Save
#Load

def loadLevel(level):
    leveldata = {}
    f = open("levels/"+level)
    rows = f.read().splitlines()
    t=0
    for i in rows:
        leveldata[t]={}
        k = 0
        for c in i:
            if c == "d":
                leveldata[t][k] = {tile = "dirt"}
            elif c == "g":
                leveldata[t][k] = {tile = "grass"}
            elif c == "s":
                leveldata[t][k] = {tile = "stone"}
            k+=1
        t+=1
    return leveldata
