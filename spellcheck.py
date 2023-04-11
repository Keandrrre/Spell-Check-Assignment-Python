# Spell Check Starter
# This start code creates two lists
# 1: dictionary: a list containing all of the words from "dictionary.txt"
# 2: aliceWords: a list containing all of the words from "AliceInWonderland.txt"

import re  # Needed for splitting text with a regular expression
import time
import os

# Binary Search


def binarySearch(anArray, item):
    low_i = 0
    high_i = len(anArray)

    while low_i <= high_i:
        mid_i = low_i + ((low_i + high_i) // 2)
        if anArray[mid_i] == item:
            return mid_i
        elif anArray[mid_i] > item:
            high_i = mid_i - 1
        else:
            low_i = mid_i + 1
    return -1

# Linear Search


def linearSearch(anArray, item):
    for i in range(len(anArray)):
        if anArray[i] == item:
            return i
    return -1


def main():
    # Load data files into lists
    dictionary = loadWordsFromFile("data-files/dictionary.txt")
    aliceWords = loadWordsFromFile("data-files/AliceInWonderLand.txt")

    # Print first 50 values of each list to verify contents
#   print(dictionary[0:50])
#   print(aliceWords[0:50])

    # Menu Display
    loop = True
    while loop == True:
        print("Main Menu \n\t1. Spell Check a Word (Linear Search) \n\t2. Spell Check a Word (Binary Search) \n\t3. Spell Check Alice In Wonderland (Linear Search) \n\t4. Spell Check Alice In Wonderland (Binary Search) \n\t5. Exit")
        # Input Menu Option
        selected = int(input("Enter menu selection (1-5): "))

        if selected == 1:
            user_word = input("Please enter a word: ")
            start = time.time()
            result = linearSearch(dictionary, user_word)
            end = time.time()
            if result > -1:
                print(user_word + " is IN the dictionary at position " +
                      str(result) + ". (" + str((end-start)) + " s)")
            else:
                print(str(user_word) + " Was NOT found in the dictionary. " +
                      "(" + str((end-start)) + " s)")
        elif selected == 2:
            user_word = input("Please enter a word: ")
            start = time.time()
            result = binarySearch(dictionary, user_word)
            end = time.time()
            if result > -1:
                print(user_word + " is IN the dictionary at position " +
                      str(result) + ". (" + str((end-start)) + " s)")
            else:
                print(str(user_word) + " Was NOT found in the dictionary. " +
                      "(" + str((end-start)) + " s)")
        elif selected == 3:
            start = time.time()
            count = 0
            for i in range(len(aliceWords)):
                result = linearSearch(dictionary, aliceWords[i])
                if result < 0:
                    count = count + 1
            end = time.time()
            print("Toatal # of words not found in dictionary:" +
                  str(count) + ". (" + str((end-start)) + ")")
        elif selected == 4:
            start = time.time()
            count = 0
            for i in range(len(aliceWords)):
                result = binarySearch(dictionary, aliceWords[i])
                if result < 0:
                    count = count + 1
            end = time.time()
            print("Toatal # of words not found in dictionary:" +
                  str(count) + ". (" + str((end-start)) + ")")
        elif selected == 5:
            loop = False
            os.system('cls')
# end main()


def loadWordsFromFile(fileName):
    # Read file as a string
    fileref = open(fileName, "r")
    textData = fileref.read()
    fileref.close()

    # Split text by one or more whitespace characters
    return re.split('\s+', textData)
# end loadWordsFromFile()


# call main
main()
