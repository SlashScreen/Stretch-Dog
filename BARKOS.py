#BARKOS
#Used for Stuff that involves the system

#TODO#
#Read Level and construct
#Calculate Stretch
#Save
#Collision

def loadLevel(level):
    ###VARIABLE###
    leveldata = {}
    ###RAD FILE###
    f = open("levels/"+level)
    rows = f.read().splitlines()
    ###READ###
    t=0
    for i in rows: #Separate Rows / Per Row
        leveldata[t]={}
        k = 0
        for c in i: #Separate Letters / Per Character
            leveldata[t][k] = {}
            if c == "d":
                leveldata[t][k]["tile"] = "dirt"
            elif c == "g":
                leveldata[t][k]["tile"] = "grass"
            elif c == "s":
                leveldata[t][k]["tile"] = "stone"
            else:
                leveldata[t][k]["tile"] = "air"
            k+=1 #index
        t+=1 #index
    return leveldata
