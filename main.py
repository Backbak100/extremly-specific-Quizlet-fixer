global savethati
savethati = -1

def restring(string):
    newstringeng = ""
    newstringltn = ""
    latin = False
    for i in string:
        if i == "\t":
            latin = True
            continue
        if latin == False:
            newstringeng += i
        elif latin == True:
            newstringltn += i
    
    restrung = newstringltn + "\t" + newstringeng
    return restrung

def sectiontxt(largetxt):
    global savethati
    sectionedofftext = ""
    for i in range (savethati+1, len(largetxt)):
        if largetxt[i] == "\n":
            savethati = i
            break
        else:
            sectionedofftext += largetxt[i]
    return sectionedofftext

def findrange(massive):
    counter = 0
    for i in massive:
        if i == "\n":
            counter+=1
    return counter

def main(text):
    counter = 0
    while counter <= findrange(text):
        newtext = sectiontxt(text)
        print(restring(newtext))
        counter+=1

#Different cards must be seperated by a new line, and the term and definition must be seperated by a tab (press export on Quizlet and copy and paste)
#Replace the example text here
text = """Definition - 1	Term - 1
Definition - 2	Term - 2
Definition - 3	Term - 3
"""

main(text)
