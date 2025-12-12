#!/usr/bin/env python3
from stats import countWords
from stats import countChars
from stats import sortedDicts
import sys

#This grabs the book from the filepath and returns its text
def getBookText(filePath):
    bookText = None
    try:
        with open(filePath) as f:
            bookText = f.read()
            return bookText
    except Exception as e:
        return None
def sort_on(items):
    return(items['num'])
def main():
    if len(sys.argv) != 2:
        print("this program takes a filepath to a text file and returns the amount of words and instances of each character in it\n Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book = getBookText(sys.argv[1])
    #print(book)
    if book == None:
        print("main.py: No File found at provided path")
        exit(21)
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    wordCount = countWords(book)
    diction = countChars(book)
    characterCounts = sortedDicts(diction)
    print(f"Found {wordCount} total words")
    print("--------- Character Count -------")
    characterCounts.sort(reverse=True, key=sort_on)
    for entry in range(len(characterCounts)) :
        print(f"{characterCounts[entry]['char']}: {characterCounts[entry]['num']}")
    print("============= END ===============")
if __name__ == "__main__":
    main()
