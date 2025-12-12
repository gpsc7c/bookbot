#counts words in a string
def countWords(bk):
    wc = bk.split() #wordcount
    return len(wc)
def countChars(bk):
    countDict = {}
    for char in bk:
        if char.isalpha():
            if char.lower() in countDict:
                countDict[char.lower()] += 1
            else:
                countDict[char.lower()] = 1
    return countDict
#turns a dictionary into an list of dictionaries
def sortedDicts(dicti):
    listionary = []
    for key in dicti:
        listionary.append({"char": key, "num": dicti[key]})
    return listionary

