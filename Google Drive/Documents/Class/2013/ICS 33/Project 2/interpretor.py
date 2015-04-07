#Nicholas Fernando 12659548
import statement


def runbumpkin():
    'Runs bumpkin interpretor'
    exact = True
    while exact:
        command = input('> ').upper().split()
        if command[0] == 'RUN':
            Interpretor().run(openfile(command[1]))
        elif command[0] == 'TRACE':
            ps = statement.Parser().parse(openfile(command[1]))
            while ps.end:
                current = ps.Get_current_statement()
                current.Trace(ps)
        elif command[0] == 'EXIT':
            exact = False


def openfile(textfile: 'File'):
    'Opens and closes a specified file'
    with open(str(textfile), 'r') as B:
        content = B.readlines()
        lineofcontent = [line.strip() for line in content]

    return lineofcontent

    

class Interpretor:
    'Parses text file'
    def run(self,line:'List of string'):
        ps = statement.Parser().parse(line) 
        while ps.end:
            current = ps.Get_current_statement()
            hello = current.execute(ps)


if __name__=='__main__':
    runbumpkin()
      
