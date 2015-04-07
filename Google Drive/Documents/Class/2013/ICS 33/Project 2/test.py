import test_statement



c1 = """Hello: LET A 8
LET B 9
Hey: LET C 10
ADD A 2
PRINT A
LET C 4
MULT C A
LET D 5
MULT A 4
LET J 4
PRINT A 
END""".splitlines()

c2 ="""LET Z 5
GOTO 7
LET C 4
PRINT C
PRINT Z
END
PRINT C
PRINT Z
GOTO 3""".splitlines()
cl = []
c3= """LET A 1
GOSUB 7
PRINT A
END
LET A 3
RETURN
PRINT A
LET A 2
GOSUB 5
PRINT A
RETURN
.""".splitlines()

class Interpretor:

    def run(self,line):
        ps = test_statement.Parser().parse(line) 
        while ps.end:
            current = ps.Get_current_statement()
            hello = current.execute(ps)

Interpretor().run(c3)




