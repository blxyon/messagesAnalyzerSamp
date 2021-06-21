import time
import winsound


listAnalized=[]
linesWOTime=[]
counterShown=0
people=[]
keywords=[[["inf","infernus"],["cumpar","buy","cump"]],
          [["inf","infernus"],["vand","vind","sell","v/t"]],
          [["mave","mav","maverick"],["vand","v/t","vind","sell"]]]
def getLines():
    f = open('chatlog.txt')
    line = f.readline()
    while line:
        line = f.readline()
        line=line.lower()
        splitLine=line.split(" ",1)
        if(len(splitLine)>1):
            line2=splitLine[1]
        if(not(line in listAnalized)) and (analyseForKeywords(keywords,line)) and not(checkDuplicate(line2)):
            listAnalized.append(line)
            linesWOTime.append(line2)
            #messagebox.showinfo("Title", line)
    f.close()

def analyseForKeywords(keywords, string):
    i=0
    counter=0
    tempPosibilityLen=0
    for possibility in keywords:
        if(counter==len(possibility)):
            return True
        counter=0
        for keys in possibility:
            i=0
            while(i<len(keys)):
                if keys[i] in string:
                    i=len(keys)
                    counter=counter+1
                i=i+1
        tempPosibilityLen=len(possibility)
    if(counter==len(keywords[0])):
        return True
    else:
        return False
def checkDuplicate(line):
    #print(line)
    if not(line in linesWOTime):
        return False
    else:
        return True
getLines()

while(True):
    time.sleep(30)
    getLines()
    if(counterShown<len(listAnalized)):
        for i in range(counterShown,len(listAnalized)):
            print(listAnalized[i])
            winsound.PlaySound("sound2.wav",winsound.SND_ASYNC)
        counterShown=len(listAnalized)
