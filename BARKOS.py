#BARKOS
#Used for Stuff that involves the system

#TODO#
#Save, Load

def loadLevel(level):
    
    ###VARIABLE###
    
    leveldata = {}
    leveldata["level"] = {}
    
    ###RAD FILE###
    
    f = open("levels/"+level)
    rows = f.read().splitlines()
    
    ###READ###
    leveldata["name"] = rows.pop(0)
    leveldata["next"] = rows.pop(0)
    print(leveldata["name"],leveldata["next"])

    t=0
    for i in rows: #Separate Rows / Per Row
        leveldata["level"][t]={}
        k = 0
        for c in i: #Separate Letters / Per Character
            leveldata["level"][t][k] = {}
            if c == "d":
                leveldata["level"][t][k]["tile"] = "dirt"
            elif c == "g":
                leveldata["level"][t][k]["tile"] = "grass"
            elif c == "s":
                leveldata["level"][t][k]["tile"] = "stone"
            elif c == "f":
                leveldata["level"][t][k]["tile"] = "win"
            else:
                leveldata["level"][t][k]["tile"] = "air"
            k+=1 #index
        t+=1 #index
    return leveldata

def isOverlapping (rect1, rect2):
    return rect1.colliderect(rect2)
    
