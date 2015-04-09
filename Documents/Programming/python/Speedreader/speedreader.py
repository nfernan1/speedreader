#Speedreader program
#Scan 
fileToScan = input("Scan File: ")
print(fileToScan)

with open(fileToScan,'r') as readFile:
    for line in readFile:
        for word in line.split():
            print(word)


