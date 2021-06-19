import time
listAnalized=[]
linesWOTime=[]
counterShown=0
people=[]
keywords=[["inf","infernus"],["cumpar","cump","buy"]]
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
    for keys in keywords:
        i=0
        while(i<len(keys)):
            if keys[i] in string:
                i=len(keys)
                counter=counter+1
            i=i+1
    if(counter==len(keywords)):
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
    time.sleep(3)
    getLines()
    if(counterShown<len(listAnalized)):
        for i in range(counterShown,len(listAnalized)):
            print(listAnalized[i])
        counterShown=len(listAnalized)
