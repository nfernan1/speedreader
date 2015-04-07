#ICS 32 Lab 1
#Timothy Lee 13587394
#Nicholas Fernando 12659548

import os
import os.path
import shutil

def directory_lookup(directoryname)->[]:
    ListOfElements=(os.listdir(directoryname))
    ListOfAllFilePaths=[]
    
    for Element in ListOfElements:
        FullPathName=os.path.join(directoryname, Element)

        if os.path.isfile(FullPathName):
            ListOfAllFilePaths.append(FullPathName)

        elif os.path.isdir(FullPathName):
            ListOfAllFilePaths.extend(directory_lookup(FullPathName))
            
    return ListOfAllFilePaths




def user_interface():
    while True:
        directoryname=input("What is the root window you want to search through?: ")
        if os.path.lexists(directoryname):
            ListOfAllFiles=directory_lookup(directoryname)
            print("The following directory was found:")
            print(directoryname + "\n")
            break
        else:
            print("No such directory exists. Please try again.")

    ListOfAllImportantFiles=[]


    search_option=(input('''What search criteria do you want to use?
               1: Searches a file by its name.
               2: Searches a file based on the extension.
               3: Searches a file by its size in bytes.
               '''))

    if search_option == '1':
        filename=input('What is the name of the file you would like to search for:' + "\n")
        for file in ListOfAllFiles:
            if filename in file:
                ListOfAllImportantFiles.append(file)
                    
        
           
            
        
    elif search_option == '2':
        extension=input('What is the extension you would like to use to search: ' + "\n")
        for file in ListOfAllFiles:
            if file.endswith(extension):
                ListOfAllImportantFiles.append(file)
                
                
                

        
    elif search_option == '3':
        size= int(input('What is the size in bytes of the file(s) you would like to search for?: ' + "\n"))
        for file in ListOfAllFiles:
            filesize=os.stat(file)
            if filesize.st_size>=size:
                ListOfAllImportantFiles.append(file)

    print("Based on your search, the following files will be considered:" + "\n")
    for file in ListOfAllImportantFiles:
        print (file)

###ACTIONS

    actionmenu=input('''
What actions would you like to take on the file(s)?
    1: Prints the path of the file.
    2: Prints the first line of text from the file(assuming it's a text file).
    3: Makes a copy of the file in the same directory
    4: Modifies the timestamp of the file
    ''')
    

    if actionmenu== '1':
        print("The following directories were found" + "\n")
        for file in ListOfAllImportantFiles:
            print(file)
            
    if actionmenu== '2':
        print("You have chosen to print the first line from the file, assuming it's a text file.")
        try:
            for file in ListOfAllImportantFiles:
                openfile=open(file,'r')
                firstline=openfile.readline()
                print("The first line from {} is:".format(file))
                print(firstline + "\n")
        except UnicodeDecodeError:
            print("The following file could not be read from.")
            print("{}".format(file))

        
    if actionmenu== '3':
        for file in ListOfAllImportantFiles:
            copy_name=file+".dup"
            shutil.copyfile(file,copy_name)
            print("The following file has been copied in the same directory:")
            print("{}".format(file)+"\n")
    
    if actionmenu== '4':
        for file in ListOfAllImportantFiles:
            os.utime(file)
            print("The following file has been touched.")
            print(file + "\n")

if __name__ =='__main__':
    user_interface()
  
