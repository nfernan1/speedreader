#Speedreader program
#TODO LIST:
    #Print a certain amount of words specified by user
    #Make a gui
    #make previous words disappear 

#Scan
import time

fileToScan = 'inputText1.txt' #input("Scan File: ")
speedOfPrint = 1.0 #float(input("Enter word speed: "))
amountOfWords = 3 #int(input("Enter amount of words: "))

print(fileToScan) # REMOVE

# Prints word by word in the scanned file
with open(fileToScan,'r') as readFile:
    wordList = [ word for line in readFile for word in line.split()]          
        

position = 0
for i in range(position, amountOfWords):
    position = i
    print(wordList[i], end=" ")
    #print_word(position, endPosition)

    # Delays the time a word will appear
    # time.sleep(speedOfPrint)
    
print(position) #REMOVE
print(wordList) #REMOVE



