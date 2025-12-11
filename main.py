#!/usr/bin/env python3
from stats import countWords
from stats import countChars

#This grabs the book from the filepath and returns its text
def getBookText(filePath):
    bookText = None
    try:
        with open(filePath) as f:
            bookText = f.read()
            return bookText
    except Exception as e:
        return None

def main():
    book = getBookText("./books/frankenstein.txt")
    #print(book)
    if book == None:
        print("main.py: No File found at provided path")
        exit(21)
    wordCount = countWords(book)
    diction = countChars(book)
    characterCounts = sortedDict(diction)
    print(f"Found {wordCount} total words")
    for entry in characterCounts:
        print(f"{entry[char]}: {entry[num]}")
if __name__ == "__main__":
    main()
