#Speedreader program
#Scan
import time


fileToScan = input("Scan File: ")
speedOfPrint = float(input("Enter word speed: "))
print(fileToScan) # REMOVE

# Prints word by word in the scanned file
with open(fileToScan,'r') as readFile:
    for line in readFile:
        for word in line.split():
            print(word)

            # Delays the time a word will appear
            time.sleep(speedOfPrint)


hello this is an edit
