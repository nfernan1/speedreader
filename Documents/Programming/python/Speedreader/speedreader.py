#Speedreader program
#TODO LIST:
    #Should either be able to upload text file or copy paste text
    #Print a certain amount of words specified by user
    #Make a gui
        #Have a text box that you upload file
        #A lightbox pops up and displays the text
    #make previous words disappear

#Scan
import time

fileToScan = 'inputText1.txt' #input("Scan File: ")
speedOfDisplay = 1.0 #float(input("Enter word speed: "))
amountOfWords = 4 #int(input("Enter amount of words: "))

class Text_Scanner(object):
    
    def __init__(self, fileToScan, speedOfDisplay, amountOfWords):
        self.fileToScan = fileToScan
        self.speedOfDisplay = speedOfDisplay
        self.amountOfWords = amountOfWords

    def scan_file(self):
        
        # Places words in text file into a list
        with open(fileToScan,'r') as readFile:
            wordList = [ word for line in readFile for word in line.split()]                  

        # Print words in certan range
        position = 0
        storedIdx = 0
        while position < len(wordList):
                
            for i in range(position, storedIdx):
                position = i + 1
                try:
                    print(wordList[i], end=" ")
                except IndexError:
                    break
                
            # Delays the time a word will appear
            print(storedIdx)
            time.sleep(speedOfDisplay)
            
            if storedIdx > len(wordList):
                storedIdx = len(wordList)
            else:
                storedIdx += amountOfWords
            
        print(position) #REMOVE
        print(wordList) #REMOVE  



test = Text_Scanner(fileToScan, speedOfDisplay, amountOfWords)
test.scan_file()
