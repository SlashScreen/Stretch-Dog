#BARKOS
#Used for Stuff that involves the system

#TODO#
#Save, Load

import coin_class as cclass
import ast
import json

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
                leveldata["coins"][cindex] = cclass.coin(-t,k)
                cindex+=1
        t+=1 #index
    #print("leveldata------",leveldata)
    return leveldata

def constructSaveData(coins,levels):
    data = {}
    data["c"] = coins
    data["complete"] = levels
    return data
    print(data)

def save(data):
    print(data)
    f = open("save/save.bark","w+")
    f.write(str(data))
    f.close()

def getLevelList():
    f = open("levellist.bark","r+")
    lst = ast.literal_eval(f.read())
    return lst

def load():
    f = open("save/save.bark")
    data = ast.literal_eval(f.read())
    print(data["c"],data["complete"])
    return data

def isOverlapping (rect1, rect2):
    return rect1.colliderect(rect2)
    
