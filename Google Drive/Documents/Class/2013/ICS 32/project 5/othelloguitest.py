#Nicholas Fernando 12659548

import tkinter
import othellogamestate

DEFAULT_FONT= ('Helvetica', 12)
DFONT = ('Helvetica', 10)
    
        
class OthelloGui():
    '''Othello GUI'''

    def __init__(self, col:int, row:int, player:str, winning_method:str, startpiece:str):
        '''Keeps track of my othellogamestate and gui'''

        self._column = col
        self._row = row
        self._player = player
        self._winning_method = winning_method
        self._startpiece = startpiece

        self._check = False
        self._check2 = False


        self.canvas_width = 600
        self.canvas_height = 500

        self._cellsize = self.canvas_height/self.canvas_width

        
        self._root_window = tkinter.Tk()

        
        self._board_canvas = tkinter.Canvas(self._root_window, bg="#009500",
                                    width = 600,
                                    height = 500)
        self._board_canvas.bind('<Configure>', self.resize)
        self._board_canvas.bind('<Button-1>', self._on_canvas_click)

        self._board_canvas.grid(row=4,column =0, padx=30,pady=55,
                                sticky = tkinter.N + tkinter.E + tkinter.S + tkinter.W)


        self._root_window.rowconfigure(1, weight = 1)
        self._root_window.columnconfigure(0, weight = 1)



        self.gs = othellogamestate.Gamestate(self._column, self._row, self._player,
                                              self._winning_method, self._startpiece)
        self.gs.Board()
       

        # Shows Score and Turns on Root Window
        self._show_on_window()
        
        
    def start(self):
        '''starts the tkinter mainloop'''
        self._root_window.mainloop()

    def resize(self, event: tkinter.Event):
        '''Draws the board and resizes the canvas'''
        self.game_all()
        

    def _draw_piece(self, column, rown, player):
        '''Draws the ovals that are on the board'''
        col_width = self._board_canvas.winfo_width()//self.gs._column
        row_height = self._board_canvas.winfo_height()//self.gs._row
        
        if player:
            color = "black"
        else:
            color = "white"

        self._board_canvas.create_oval(
            column*col_width, rown*row_height,
            (column+1)*col_width,(rown+1)*row_height, fill = color)
        

    def _paint_board(self):
        ''''Checks to see where the pieces are placed on the othellogamestate'''

        for col in range(self.gs._column):
            for row in range(self.gs._row):
                color = self.gs._board[col][row]
                if color == 'B':
                    self._draw_piece(col, row, True)
                elif color == 'W':
                    self._draw_piece(col, row, False)
                    
        self._score.set(self.gs.Score())
        self._turn.set(self.gs.Turn())



                

    def _board_grid(self):
        '''Draws the board grid'''

        col_width = self._board_canvas.winfo_width()//self._column
        row_height = self._board_canvas.winfo_height()//self._row

        col_w = self._board_canvas.winfo_width()
        row_h = self._board_canvas.winfo_height()
        
        for col in range(1,self._column): 
            self._board_canvas.create_line(col*(col_w//self._column),0,col*(col_w//self._column),row_h)
            
        for row in range(1, self._row):
            self._board_canvas.create_line(0,row*(row_h//self._row),col_w, row*(row_h//self._row))




    def _on_canvas_click(self, event: tkinter.Event):
        '''Flips pieces when a player clicks on the grid'''

        col_width = self._board_canvas.winfo_width()//self._column
        row_height = self._board_canvas.winfo_height()//self._row


        col = event.x//col_width
        row = event.y//row_height
        
    
        self.gs.Flip_piece(col,row)
        self.play()
           
        self.game_all()


        
    def game_all(self):
        '''Constantly redraws the board'''
        self._board_canvas.delete(tkinter.ALL)
        self._board_grid()
        self._paint_board()



    def _show_on_window(self):
        '''Shows the text/score/turn on the root window'''
        game_label = tkinter.Label(
            self._root_window, text = 'Reversi/Othello',
            font = ('Helvetica', 30))

        game_label.grid(
            row = 2, column = 0, columnspan = 2, padx = 10, pady = 12,
            sticky = tkinter.N)

        #score
        self._score = tkinter.StringVar()
        self._score.set(self.gs.Score())
        self.score_label = tkinter.Label(master=self._root_window, textvariable = self._score,
                                    font = ('Helvetica', 30))
        
        self.score_label.grid(row = 3, column = 0,columnspan = 1, padx=10, pady=10, sticky = tkinter.S)




        #Turn
        self._turn = tkinter.StringVar()
        self._turn.set(self.gs.Turn())
        self._turn_label = tkinter.Label(self._root_window,textvariable = self._turn,
                                         font = ('Helvetica',30))
        
        self._turn_label.grid(row = 4, column = 0, padx = 10, pady =10, sticky = tkinter.S)
        

    def play(self):
        '''Plays the othello game'''

        self._pmoves = self.gs.Possible_move_list()


        if self._pmoves != []:
            if self.gs.Turn() == 'Turn: Black':
                if self._pmoves == []:
                    self._check = True
         

            if self.gs._opposite(self.gs.Turn()) == 'Turn: White':
                if self._pmoves == []:
                    self._check2 = True

                
        elif self._pmoves == []:

            #Pops who the winner is on top of the root window
            self.who = tkinter.StringVar(value = self.gs._win())
            who_label = tkinter.Label(
            self._root_window, textvariable = self.who,
            font = ('Helvetica', 30)).grid(row = 0, column = 0, padx = 10, pady=10,
                                        sticky = tkinter.N)

     

  


    
