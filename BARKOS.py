#BARKOS
#Used for Stuff that involves the system

#TODO#
#Save, Load

import coin_class as cclass

def loadLevel(level):
    
    ###VARIABLE###
    
    leveldata = {}
    leveldata["level"] = {}
    leveldata["coins"] = {}
    
    ###READ FILE###
    
    f = open("levels/"+level)
    rows = f.read().splitlines()
    
    ###READ###
    leveldata["name"] = rows.pop(0)
    leveldata["next"] = rows.pop(0)
    print(leveldata["name"],leveldata["next"])

    t=0
    cindex = 0
    for i in rows: #Separate Rows / Per Row
        leveldata["level"][t]={}
        k = 0
        for c in i: #Separate Letters / Per Character
            if not c == "c":
                leveldata["level"][t][k] = {}
                if c == "d":
                    leveldata["level"][t][k]["tile"] = "dirt"
                    k+=1 #index
                elif c == "g":
                    leveldata["level"][t][k]["tile"] = "grass"
                    k+=1 #index
                elif c == "s":
                    leveldata["level"][t][k]["tile"] = "stone"
                    k+=1 #index
                elif c == "f":
                    leveldata["level"][t][k]["tile"] = "win"
                    k+=1 #index
                elif c == "l":
                    leveldata["level"][t][k]["tile"] = "flip"
                    k+=1 #index
                else:
                    leveldata["level"][t][k]["tile"] = "air"
                    k+=1 #index
                k+=1
            else:
                leveldata["coins"][cindex] = cclass.coin(t,k)
                cindex+=1
        t+=1 #index
    print("leveldata------",leveldata)
    return leveldata

def isOverlapping (rect1, rect2):
    return rect1.colliderect(rect2)
    
