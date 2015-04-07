import tkinter
import othellogamestate

DEFAULT_FONT= ('Helvetica', 12)
DFONT = ('Helvetica', 10)

class OthelloGui():

    def __init__(self, col=8, row=8, player='b', winning_method='m'):

        self._column = col
        self._row = row
        self._player = player
        self._winning_method = winning_method
        self._move = None
        self._move_played = False

        self._cellsize = 80

        canvas_width = self._column * self._cellsize
        canvas_height = self._row * self._cellsize
        


        
        self._root_window = tkinter.Tk()
        
        self._board_canvas = tkinter.Canvas(self._root_window, bg="#009500",
                                    height = canvas_height,
                                    width = canvas_width)
        
                
        self._board_canvas.bind('<Configure>', self._board_grid)
##        self._board_canvas.bind('<Configure>', self._paint_board)
        self._board_canvas.bind('<Button-1>', self._on_canvas_click)

        self._board_canvas.pack(fill='both',expand=True, padx=45,pady=65)

        self.gs = othellogamestate.Gamestate(self._column, self._row, self._player,
                                              self._winning_method) 

        

    def start(self):
        self._root_window.mainloop()
        
    #ratio 3/8 * pixel width--starting point to ending point
    #remember to bind event

    def _paint_board(self):
        #list of lists
        #paint whats on this list onto the board
        for col in range(self._column):
            for row in range(self._row):
                color = self.gs._board[col][row]
                if color == 'B':
                    board_color = "black"
                elif color == 'W':
                    board_color = "white"
                else:
                    continue
                
                if self.gs._board[col][row] is not self.gs._empty:
                    self._board[col][row] = self._board_canvas.create_oval(
                        row, col, row, col, fill = board_color)



    def _board_grid(self, event: tkinter.Event):

        col_width = event.width//self._column
        row_height = event.height//self._row


        self._board_canvas.delete(tkinter.ALL)


        for col in range(1,self._column): 
            x = col_width*col
            self._board_canvas.create_line(x,0,x,event.height)
            
        for row in range(1, self._row):
            y = row_height*row
            self._board_canvas.create_line(0,y,event.width, y)


    def _on_canvas_click(self, event: tkinter.Event):
        col_width = event.width//self._column
        row_height = event.height//self._row
        
        self._move = ((col_width*canvas_width), (row_height*canvas_height))
        self._move_played = True

        click_coordinate = coord
        x = ((/self._column)*canvas_width)
        y = 
        self._board_canvas.create_oval(,,,)


        
"""
class InputBox:

    def __init__(self):#, col: int, row: int, player: str, winning_method: str):


        self._dialog_window = tkinter.Toplevel()
        self._dialog_window.title('Input Options')
        
        var = tkinter.IntVar()
        strang = tkinter.StringVar()


        #important options
        option_label = tkinter.Label(
            self._dialog_window, text = 'Input Important Options',
            font = DEFAULT_FONT)

        option_label.grid(
            row = 0, column = 0, columnspan = 2, padx = 10, pady = 12,
            sticky = tkinter.W)

        #column size   
        column_label = tkinter.Label(self._dialog_window, text = 'Select a Column Size:',
                                    font = DFONT)

        column_label.grid(
            row = 1, column = 0, columnspan = 1, padx = 10, pady = 10,
            sticky = tkinter.W)
##        
##        tkinter.Radiobutton(self._dialog_window, text = '4', padx=20, variable = var,
##                                command = var.get(), value = 4).pack(anchor = 'w')
##        tkinter.Radiobutton(self._dialog_window, text = '6', padx=20, variable = var,
##                                command = var.get(), value = 6).pack(anchor = 'w')
##        tkinter.Radiobutton(self._dialog_window, text = '8', padx=20, variable = var,
##                                command = var.get(), value = 8).pack(anchor = 'w')
##        tkinter.Radiobutton(self._dialog_window, text = '10', padx=20, variable = var,
##                                command = var.get(), value = 10).pack(anchor = 'w')
##        tkinter.Radiobutton(self._dialog_window, text = '12', padx=20, variable = var,
##                                command = var.get(), value = 12).pack(anchor = 'w')
##        tkinter.Radiobutton(self._dialog_window, text = '14', padx=20, variable = var,
##                                command = var.get(), value = 14).pack(anchor = 'w')
##        tkinter.Radiobutton(self._dialog_window, text = '16', padx=20, variable = var,
##                                command = var.get(), value = 16).pack(anchor = 'w')
##


        #row size
        row_label = tkinter.Label(
            self._dialog_window, text = 'Select a Row size: ',
            font = DFONT)

        row_label.grid(
            row = 1, column = 1, columnspan = 1, padx = 10, pady = 10,
            sticky = tkinter.E)

##        tkinter.Radiobutton(self._dialog_window, text = '4', padx=20, variable = var,
##                                command = var.get(), value = 4).pack(anchor = 'e')
##        tkinter.Radiobutton(self._dialog_window, text = '6', padx=20, variable = var,
##                                command = var.get(), value = 6).pack(anchor = 'e')
##        tkinter.Radiobutton(self._dialog_window, text = '8', padx=20, variable = var,
##                                command = var.get(), value = 8).pack(anchor = 'e')
##        tkinter.Radiobutton(self._dialog_window, text = '10', padx=20, variable = var,
##                                command = var.get(), value = 10).pack(anchor = 'e')
##        tkinter.Radiobutton(self._dialog_window, text = '12', padx=20, variable = var,
##                                command = var.get(), value = 12).pack(anchor = 'e')
##        tkinter.Radiobutton(self._dialog_window, text = '14', padx=20, variable = var,
##                                command = var.get(), value = 14).pack(anchor = 'e')
##        tkinter.Radiobutton(self._dialog_window, text = '16', padx=20, variable = var,
##                                command = var.get(), value = 16).pack(anchor = 'e')


        #player choice
        player_label = tkinter.Label(
            self._dialog_window, text = 'Select a Player: ',
            font = DFONT)

        player_label.grid(
            row = 2, column = 0, columnspan = 1, padx = 10, pady = 10,
            sticky = tkinter.W)

##        tkinter.Radiobutton(self._dialog_window, text = 'B', padx=20, variable =  strang,
##                                command = strang.get(), value = 1).pack(anchor = 'w')
##        tkinter.Radiobutton(self._dialog_window, text = 'W', padx=20, variable = var,
##                                command = strang.get(), value = 2).pack(anchor = 'w')

        

        #winning_method choice
        winningmethod_label = tkinter.Label(
            self._dialog_window, text = '''Select a Winning Method:
        [M]ost or [L]east Discs''',
            font = DFONT)

        winningmethod_label.grid(
            row = 2, column = 1, columnspan = 1, padx = 10, pady = 10,
            sticky = tkinter.E)

##        tkinter.Radiobutton(self._dialog_window, text = 'M', padx=20, variable = strang,
##                                command = strang.get(), value = 'M').pack(anchor = 'e')
##        tkinter.Radiobutton(self._dialog_window, text = 'L', padx=20, variable = var,
##                                command = strang.get(), value = 'L').pack(anchor = 'e')

        

        #starting tile placement
        starttileplace_label = tkinter.Label(
            self._dialog_window, text = 'Select Tile Color in left corner: ',
            font = DFONT)

        starttileplace_label.grid(
            row = 3, column = 0, columnspan = 1, padx = 10, pady = 10,
            sticky = tkinter.W)

##        tkinter.Radiobutton(self._dialog_window, text = 'B', padx=20, variable = var,
##                                command = var.get(), value = 'B').pack(anchor = 'w')
##        tkinter.Radiobutton(self._dialog_window, text = 'W', padx=20, variable = var,
##                                command = var.get(), value = 'W').pack(anchor = 'w')
##
        
        button_frame = tkinter.Frame(self._dialog_window)

        button_frame.grid(
            row = 3, column = 0, columnspan = 2, padx = 10, pady = 20,
            sticky = tkinter.E + tkinter.S)


        ok_button = tkinter.Button(
            button_frame, text = 'OK', font = DEFAULT_FONT,
            command = self._on_ok)



        ok_button.grid(row = 0, column = 0, padx = 10)


        cancel_button = tkinter.Button(
            button_frame, text = 'Cancel', font = DEFAULT_FONT,
            command = self._on_cancel)



        cancel_button.grid(row = 0, column = 1, padx = 10)

        self._dialog_window.rowconfigure(3, weight = 1)
        self._dialog_window.columnconfigure(1, weight = 1)

        self._ok_clicked = False
    
    def show(self):

        self._dialog_window.grab_set()
        self._dialog_window.wait_window()

    def was_ok_clicked(self):

        return self._ok_clicked

        
    def _on_ok(self):

        self._ok_clicked = True
##        self._first_name = self._first_name_entry.get()
##        self._last_name = self._last_name_entry.get()

        self._dialog_window.destroy()




    def _on_cancel(self):

        self._dialog_window.destroy()

        
    def start(self):
        self._dialog_window.mainloop()

class StartGameApplication:
    def __init__(self):
        self._root = tkinter.Tk()

        startgame_button = tkinter.Button(
            self._root, text = 'Click Here to Start Game', font = DEFAULT_FONT,
            command = self._startg)

        startgame_button.grid(
            row = 0, column = 0, padx = 10, pady = 10,
            sticky = tkinter.N)



        self._root.rowconfigure(0, weight = 1)
        self._root.rowconfigure(1, weight = 1)
        self._root.columnconfigure(0, weight = 1)

    def start(self):
        self._root.mainloop()

    def _startg(self):

        self._root.destroy()
        choice = InputBox()
        choice.show()

##        if choice.was_ok_clicked():
##
##            self.



if __name__ == '__main__':

    StartGameApplication().start()

"""
    
if __name__=='__main__':
    
    othellogui = OthelloGui()
    othellogui.start()
